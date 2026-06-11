# 🏥 ClinIQ — AI Disease Detection & Clinic Management System

> **SE CEP Project** | Bahria University | Software Engineering

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple)](https://ai.google.dev)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](https://github.com)

---

## 📌 What is ClinIQ?

ClinIQ is an **AI-powered web application** that detects **Pneumonia** and **Jaundice** from patient symptoms using **Google Gemini AI**. It also provides complete clinic management including appointments, prescriptions, and role-based dashboards.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 AI Symptom Checker | Detects Pneumonia & Jaundice using Gemini AI |
| 👥 3 User Roles | Patient, Doctor, Admin with separate dashboards |
| 📅 Appointment System | Book, approve, cancel, complete appointments |
| 💊 Digital Prescriptions | Doctors write Rx, patients view them |
| 👨‍💼 Admin Panel | Full user management and system stats |
| 🎨 Dark UI | Professional glassmorphism design |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS (Dark glassmorphism), JavaScript
- **Database:** SQLite (via Flask-SQLAlchemy)
- **AI:** Google Gemini AI (gemini-1.5-flash)
- **Auth:** Flask-Login + Werkzeug password hashing

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cliniq.git
cd cliniq
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key_here
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 👤 Demo Accounts

| Role | Email | Password |
|---|---|---|
| 👨‍💼 Admin | admin@cliniq.com | admin123 |
| 👨‍⚕️ Doctor | doctor@cliniq.com | doctor123 |
| 🤒 Patient | Register yourself | — |

---

## 📁 Project Structure

```
cliniq/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── .gitignore
├── static/
│   └── css/
│       └── style.css       # Professional dark theme CSS
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard_patient.html
    ├── dashboard_doctor.html
    ├── dashboard_admin.html
    ├── symptom_checker.html
    └── write_prescription.html
```

---

## 🏗️ Development Model

This project uses the **Incremental Development Model**:

- **v1.0.0** — Authentication + Basic dashboards
- **v1.0.1** — AI Symptom Checker (Pneumonia + Jaundice)
- **v1.0.2** — Appointment booking + Doctor module
- **v1.1.0** — Prescriptions + Admin panel

---

## 👩‍💻 Developer

**Hafsa Ashraf**
Bahria University
Software Engineering — CEP Project
June 2026

---

## ⚠️ Disclaimer

ClinIQ AI is for **informational purposes only**. It does not replace professional medical advice. Always consult a qualified doctor for medical concerns.
