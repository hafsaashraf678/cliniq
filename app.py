import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'cliniq-secret-key-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cliniq.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configure Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
try:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
    AI_AVAILABLE = True
except:
    gemini_client = None
    AI_AVAILABLE = False

# ─────────────────────────────────────────
# DATABASE MODELS
# ─────────────────────────────────────────

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # patient, doctor, admin
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    patient_profile = db.relationship('Patient', backref='user', uselist=False, cascade='all, delete-orphan')
    doctor_profile = db.relationship('Doctor', backref='user', uselist=False, cascade='all, delete-orphan')

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    blood_group = db.Column(db.String(5))
    address = db.Column(db.Text)
    emergency_contact = db.Column(db.String(20))
    medical_history = db.Column(db.Text)
    appointments = db.relationship('Appointment', backref='patient', lazy=True, cascade='all, delete-orphan')
    diagnoses = db.relationship('Diagnosis', backref='patient', lazy=True, cascade='all, delete-orphan')
    prescriptions = db.relationship('Prescription', backref='patient', lazy=True, cascade='all, delete-orphan')

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    specialization = db.Column(db.String(100))
    license_number = db.Column(db.String(50))
    experience_years = db.Column(db.Integer)
    available_days = db.Column(db.String(100), default='Mon,Tue,Wed,Thu,Fri')
    appointments = db.relationship('Appointment', backref='doctor', lazy=True, cascade='all, delete-orphan')
    prescriptions = db.relationship('Prescription', backref='doctor', lazy=True, cascade='all, delete-orphan')

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(10), nullable=False)
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, approved, completed, cancelled
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    ai_result = db.Column(db.Text)
    disease_detected = db.Column(db.String(100))
    severity = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    diagnosis = db.Column(db.Text)
    medicines = db.Column(db.Text)
    instructions = db.Column(db.Text)
    follow_up_date = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ─────────────────────────────────────────
# AI SYMPTOM CHECKER
# ─────────────────────────────────────────

def analyze_symptoms_ai(symptoms, patient_name, age, gender):
    prompt = f"""
You are a medical AI assistant at ClinIQ clinic. Analyze the following patient symptoms and provide a structured medical assessment.

Patient Info:
- Name: {patient_name}
- Age: {age}
- Gender: {gender}
- Reported Symptoms: {symptoms}

Focus specifically on detecting whether the patient may have:
1. PNEUMONIA - (check for: chest pain, fever, cough, breathing difficulty, fatigue, shortness of breath, chills, sweating)
2. JAUNDICE - (check for: yellow skin, yellow eyes, dark urine, pale stools, nausea, abdominal pain, weakness, loss of appetite)

Respond ONLY in this exact JSON format:
{{
  "disease_detected": "Pneumonia" or "Jaundice" or "Both" or "Neither",
  "severity": "Mild" or "Moderate" or "Severe",
  "confidence": "High" or "Medium" or "Low",
  "matched_symptoms": ["symptom1", "symptom2"],
  "missing_symptoms": ["symptom1", "symptom2"],
  "recommendation": "Brief recommendation in 2-3 sentences",
  "see_doctor": true or false,
  "urgency": "Immediate" or "Within 24 hours" or "Within a week" or "Not urgent",
  "precautions": ["precaution1", "precaution2", "precaution3"]
}}
"""
    try:
        import json
        response = gemini_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        text = response.text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text.strip())
    except Exception as e:
        return rule_based_checker(symptoms)

def rule_based_checker(symptoms):
    symptoms_lower = symptoms.lower()
    pneumonia_keywords = ['chest pain', 'fever', 'cough', 'breathing', 'breath', 'fatigue', 'chills', 'sweating', 'shortness']
    jaundice_keywords = ['yellow', 'jaundice', 'dark urine', 'nausea', 'abdominal', 'stomach', 'weakness', 'appetite', 'pale']

    pneumonia_score = sum(1 for kw in pneumonia_keywords if kw in symptoms_lower)
    jaundice_score = sum(1 for kw in jaundice_keywords if kw in symptoms_lower)

    if pneumonia_score >= 3 and jaundice_score >= 3:
        disease = "Both"
    elif pneumonia_score >= 3:
        disease = "Pneumonia"
    elif jaundice_score >= 2:
        disease = "Jaundice"
    else:
        disease = "Neither"

    severity = "Mild" if max(pneumonia_score, jaundice_score) <= 3 else "Moderate" if max(pneumonia_score, jaundice_score) <= 5 else "Severe"

    return {
        "disease_detected": disease,
        "severity": severity,
        "confidence": "Medium",
        "matched_symptoms": [],
        "missing_symptoms": [],
        "recommendation": "Please consult a doctor for a proper diagnosis. This is an AI-based assessment only.",
        "see_doctor": True,
        "urgency": "Within 24 hours" if disease != "Neither" else "Not urgent",
        "precautions": ["Stay hydrated", "Get adequate rest", "Avoid self-medication"]
    }

# ─────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        phone = request.form.get('phone')

        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'error')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_pw, role=role, phone=phone)
        db.session.add(user)
        db.session.flush()

        if role == 'patient':
            patient = Patient(user_id=user.id, age=request.form.get('age'), gender=request.form.get('gender'))
            db.session.add(patient)
        elif role == 'doctor':
            doctor = Doctor(user_id=user.id, specialization=request.form.get('specialization', 'General'), license_number=request.form.get('license', 'N/A'))
            db.session.add(doctor)

        db.session.commit()
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password!', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        total_users = User.query.count()
        total_patients = Patient.query.count()
        total_doctors = Doctor.query.count()
        total_appointments = Appointment.query.count()
        pending_appointments = Appointment.query.filter_by(status='pending').count()
        recent_diagnoses = Diagnosis.query.order_by(Diagnosis.created_at.desc()).limit(5).all()
        doctors = Doctor.query.all()
        patients = Patient.query.all()
        users = User.query.order_by(User.created_at.desc()).limit(10).all()
        return render_template('dashboard_admin.html',
            total_users=total_users, total_patients=total_patients,
            total_doctors=total_doctors, total_appointments=total_appointments,
            pending_appointments=pending_appointments,
            recent_diagnoses=recent_diagnoses, doctors=doctors,
            patients=patients, users=users)

    elif current_user.role == 'doctor':
        doctor = current_user.doctor_profile
        if not doctor:
            flash('Doctor profile incomplete.', 'error')
            return redirect(url_for('index'))
        appointments = Appointment.query.filter_by(doctor_id=doctor.id).order_by(Appointment.created_at.desc()).all()
        pending = Appointment.query.filter_by(doctor_id=doctor.id, status='pending').count()
        approved = Appointment.query.filter_by(doctor_id=doctor.id, status='approved').count()
        prescriptions = Prescription.query.filter_by(doctor_id=doctor.id).order_by(Prescription.created_at.desc()).all()
        return render_template('dashboard_doctor.html',
            doctor=doctor, appointments=appointments,
            pending=pending, approved=approved, prescriptions=prescriptions)

    else:  # patient
        patient = current_user.patient_profile
        if not patient:
            flash('Patient profile incomplete.', 'error')
            return redirect(url_for('index'))
        appointments = Appointment.query.filter_by(patient_id=patient.id).order_by(Appointment.created_at.desc()).all()
        diagnoses = Diagnosis.query.filter_by(patient_id=patient.id).order_by(Diagnosis.created_at.desc()).all()
        prescriptions = Prescription.query.filter_by(patient_id=patient.id).order_by(Prescription.created_at.desc()).all()
        doctors = Doctor.query.all()
        return render_template('dashboard_patient.html',
            patient=patient, appointments=appointments,
            diagnoses=diagnoses, prescriptions=prescriptions, doctors=doctors)

@app.route('/symptom-checker', methods=['GET', 'POST'])
@login_required
def symptom_checker():
    if current_user.role != 'patient':
        flash('Only patients can use the symptom checker.', 'error')
        return redirect(url_for('dashboard'))

    result = None
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        patient = current_user.patient_profile
        result = analyze_symptoms_ai(symptoms, current_user.name,
                                     patient.age if patient else 'Unknown',
                                     patient.gender if patient else 'Unknown')
        diagnosis = Diagnosis(
            patient_id=patient.id,
            symptoms=symptoms,
            ai_result=str(result),
            disease_detected=result.get('disease_detected', 'Unknown'),
            severity=result.get('severity', 'Unknown')
        )
        db.session.add(diagnosis)
        db.session.commit()

    return render_template('symptom_checker.html', result=result)

@app.route('/book-appointment', methods=['POST'])
@login_required
def book_appointment():
    patient = current_user.patient_profile
    doctor_id = request.form.get('doctor_id')
    date = request.form.get('date')
    time = request.form.get('time')
    reason = request.form.get('reason')

    appt = Appointment(patient_id=patient.id, doctor_id=doctor_id,
                       date=date, time=time, reason=reason, status='pending')
    db.session.add(appt)
    db.session.commit()
    flash('Appointment booked successfully! Waiting for doctor approval.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/update-appointment/<int:appt_id>/<string:status>')
@login_required
def update_appointment(appt_id, status):
    appt = Appointment.query.get_or_404(appt_id)
    appt.status = status
    db.session.commit()
    flash(f'Appointment {status}!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/write-prescription/<int:patient_id>', methods=['GET', 'POST'])
@login_required
def write_prescription(patient_id):
    if current_user.role != 'doctor':
        return redirect(url_for('dashboard'))
    patient_obj = Patient.query.get_or_404(patient_id)
    doctor = current_user.doctor_profile
    if request.method == 'POST':
        pres = Prescription(
            patient_id=patient_id,
            doctor_id=doctor.id,
            diagnosis=request.form.get('diagnosis'),
            medicines=request.form.get('medicines'),
            instructions=request.form.get('instructions'),
            follow_up_date=request.form.get('follow_up_date')
        )
        db.session.add(pres)
        db.session.commit()
        flash('Prescription written successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('write_prescription.html', patient=patient_obj)

@app.route('/admin/delete-user/<int:user_id>')
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/api/check-symptoms', methods=['POST'])
@login_required
def api_check_symptoms():
    data = request.get_json()
    symptoms = data.get('symptoms', '')
    patient = current_user.patient_profile
    result = analyze_symptoms_ai(symptoms, current_user.name,
                                 patient.age if patient else 'Unknown',
                                 patient.gender if patient else 'Unknown')
    return jsonify(result)

# ─────────────────────────────────────────
# INIT DB + SEED ADMIN
# ─────────────────────────────────────────

def seed_db():
    if not User.query.filter_by(role='admin').first():
        admin = User(name='Admin', email='admin@cliniq.com',
                     password=generate_password_hash('admin123'), role='admin')
        db.session.add(admin)

    if not User.query.filter_by(email='doctor@cliniq.com').first():
        doc_user = User(name='Dr. Ahmed Khan', email='doctor@cliniq.com',
                        password=generate_password_hash('doctor123'), role='doctor', phone='0300-1234567')
        db.session.add(doc_user)
        db.session.flush()
        doctor = Doctor(user_id=doc_user.id, specialization='Pulmonologist',
                        license_number='PMC-12345', experience_years=10)
        db.session.add(doctor)

    if not User.query.filter_by(email='doctor2@cliniq.com').first():
        doc_user2 = User(name='Dr. Sara Ali', email='doctor2@cliniq.com',
                         password=generate_password_hash('doctor123'), role='doctor', phone='0321-7654321')
        db.session.add(doc_user2)
        db.session.flush()
        doctor2 = Doctor(user_id=doc_user2.id, specialization='Hepatologist',
                         license_number='PMC-67890', experience_years=8)
        db.session.add(doctor2)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_db()
    app.run(debug=True, port=5000)
