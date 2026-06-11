# ClinIQ — Software Engineering Documentation
## AI Disease Detection & Clinic Management System

**Student:** Hafsa Ashraf
**Subject:** Software Engineering — CEP Project
**Project:** ClinIQ (AI-powered Pneumonia & Jaundice Detection)
**Version:** 1.0.0

---

# ITEM 1 — Development Model

## We Used: Incremental Model

The **Incremental Model** means we build the project in small steps. Each step adds new features to the existing working system.

**Why we chose it:**
- We did not know all requirements at the start
- We could test each feature before building the next one
- If AI part failed, rest of the system still worked
- Easy to add new diseases in future versions

**Our 4 Increments:**

| Version | What We Built |
|---|---|
| v1.0.0 | User registration, login, basic dashboards |
| v1.0.1 | AI symptom checker (Pneumonia + Jaundice) |
| v1.0.2 | Appointment booking + Doctor module |
| v1.1.0 | Prescriptions + Admin panel + Reports |

**Why NOT Waterfall?**
Waterfall needs all requirements at start. We discovered AI requirements during development, so waterfall did not work for us.

---

# ITEM 2 — User Stories

A user story explains **who** needs something, **what** they need, and **why**.

## Story 1 — Patient Registration and Login
> "I am Sara. I am a patient. I want to make an account on ClinIQ so I can check my symptoms and book doctor appointments. I open the app, fill my name, email, and password, choose 'Patient' role, and click Register. After that I can log in and see my dashboard."

## Story 2 — AI Symptom Check (Pneumonia)
> "I am Ali. I have chest pain, high fever, and I cannot breathe properly for 3 days. I log in to ClinIQ, go to AI Symptom Checker, click on symptoms like Chest Pain, High Fever, and Difficulty Breathing. The AI tells me I have Pneumonia (Moderate). It says see a doctor in 24 hours. I click Book Appointment."

## Story 3 — AI Symptom Check (Jaundice)
> "I am Mariam. My skin and eyes look yellow. My urine is dark. I feel weak. I open the Symptom Checker, click Yellow Skin, Yellow Eyes, Dark Urine, and General Weakness. The AI says Jaundice Detected. It gives me precautions: drink water, avoid oily food, see a liver doctor."

## Story 4 — Book Appointment
> "I am a patient. After AI told me I have Pneumonia, I go to my dashboard, click Book Appointment. I choose Dr. Ahmed Khan, select June 20 at 10:00 AM, write reason 'Chest pain and fever', and submit. My appointment shows as Pending."

## Story 5 — Doctor Approves Appointment
> "I am Dr. Ahmed Khan. I log in and see 3 pending appointments. I read Ali's reason — chest pain. I click Approve. The appointment is now Approved. After meeting Ali, I click Complete, then write a prescription."

## Story 6 — Write Prescription
> "I am Dr. Ahmed. I click Prescribe for Ali. I see his age (25, Male). I write: Diagnosis: Pneumonia, Medicines: Amoxicillin 500mg 3 times a day for 7 days, Instructions: Rest, drink water. Ali can now see this prescription in his dashboard."

## Story 7 — Admin Manages System
> "I am Admin. I log in and see total users: 8. I see 2 AI diagnoses today. I find a fake test account. I click Delete and remove it from the system."

---

# ITEM 3 — Test Cases

A test case checks **if a feature works correctly**.

## Test Case 1 — Register Account

| Field | Info |
|---|---|
| Test ID | TC-001 |
| Feature | Patient Registration |
| Input | Name: Ali, Email: ali@test.com, Password: ali123, Role: Patient |
| Expected Result | Account created, redirect to login page |
| Actual Result | ✅ Account created, redirected to login |
| Status | **PASS** |

## Test Case 2 — Login

| Field | Info |
|---|---|
| Test ID | TC-002 |
| Feature | Login |
| Input (Correct) | admin@cliniq.com / admin123 |
| Expected | Dashboard opens |
| Input (Wrong) | admin@cliniq.com / wrongpass |
| Expected | Error: "Invalid email or password" |
| Status | **PASS** |

## Test Case 3 — Pneumonia Detection

| Field | Info |
|---|---|
| Test ID | TC-003 |
| Feature | AI Symptom Check |
| Input | "chest pain, high fever, cough, difficulty breathing" |
| Expected | Disease: Pneumonia, Severity shown |
| Actual | ✅ Pneumonia Detected with analysis |
| Status | **PASS** |

## Test Case 4 — Jaundice Detection

| Field | Info |
|---|---|
| Test ID | TC-004 |
| Input | "yellow skin, yellow eyes, dark urine, nausea" |
| Expected | Disease: Jaundice, Precautions shown |
| Actual | ✅ Jaundice Detected with precautions |
| Status | **PASS** |

## Test Case 5 — Book Appointment

| Field | Info |
|---|---|
| Test ID | TC-005 |
| Input | Doctor: Dr. Ahmed, Date: June 20, Time: 10AM |
| Expected | Appointment created, Status: Pending |
| Status | **PASS** |

## Test Case 6 — Doctor Approves

| Field | Info |
|---|---|
| Test ID | TC-006 |
| Action | Click Approve button |
| Expected | Status changes to Approved |
| Status | **PASS** |

## Test Case 7 — Write Prescription

| Field | Info |
|---|---|
| Test ID | TC-007 |
| Input | Diagnosis: Pneumonia, Medicines: Amoxicillin 500mg |
| Expected | Prescription saved, visible to patient |
| Status | **PASS** |

## Test Case 8 — Admin Delete User

| Field | Info |
|---|---|
| Test ID | TC-008 |
| Action | Admin clicks Delete on a user |
| Expected | User removed from system |
| Status | **PASS** |

---

# ITEM 4 — Functional Requirements

Functional requirements = **what the system must DO**.

| ID | Requirement |
|---|---|
| FR-01 | Users can register with role: Patient, Doctor, or Admin |
| FR-02 | Users can login with email and password |
| FR-03 | Each role sees different features |
| FR-04 | Patients can type their symptoms |
| FR-05 | System sends symptoms to Gemini AI |
| FR-06 | System detects Pneumonia from symptoms |
| FR-07 | System detects Jaundice from symptoms |
| FR-08 | System shows severity level (Mild, Moderate, Severe) |
| FR-09 | System shows urgency and recommendation |
| FR-10 | Patients can book doctor appointments |
| FR-11 | Doctors can approve, cancel, or complete appointments |
| FR-12 | Doctors can write digital prescriptions |
| FR-13 | Patients can view their prescriptions |
| FR-14 | Admin can add and delete users |
| FR-15 | All AI diagnoses are saved with date and time |
| FR-16 | Each dashboard shows useful stats and numbers |

---

# ITEM 5 — Non-Functional Requirements

Non-functional requirements = **how WELL the system must work**.

| ID | Type | Requirement |
|---|---|---|
| NFR-01 | Speed | Pages open in less than 3 seconds |
| NFR-02 | Speed | AI gives result in less than 10 seconds |
| NFR-03 | Security | Passwords are never stored as plain text |
| NFR-04 | Security | Only logged-in users can see pages |
| NFR-05 | Security | API key is hidden in .env file |
| NFR-06 | Usability | Anyone can use it without training |
| NFR-07 | Usability | All forms show success or error messages |
| NFR-08 | Reliability | If AI fails, rule-based backup still works |
| NFR-09 | Reliability | System works 99% of the time |
| NFR-10 | Maintenance | Code is organized in separate files |
| NFR-11 | Scalability | Database can be changed from SQLite to MySQL |
| NFR-12 | Compatibility | Works on Chrome, Firefox, and Edge |

---

# ITEM 6 — NFR Metrics Table

This table shows **how we measure** each non-functional requirement.

| ID | What We Measure | Target Value | How We Test |
|---|---|---|---|
| NFR-01 | Page load time | Less than 3 seconds | Browser DevTools |
| NFR-02 | AI response time | Less than 10 seconds | Stopwatch test |
| NFR-03 | Password storage | PBKDF2-SHA256 hash | Check database |
| NFR-04 | Protected routes | 100% of routes | Manual testing |
| NFR-05 | Keys in code | 0 keys visible | Search code files |
| NFR-06 | First task time | Under 5 minutes | User test |
| NFR-07 | Actions with feedback | 100% | Manual testing |
| NFR-08 | AI fallback works | Yes | Remove API key and test |
| NFR-09 | System uptime | 99% or more | Monitor server |
| NFR-10 | Long files | 0 files over 500 lines | Code review |
| NFR-11 | DB switch effort | Less than 1 hour | Code review |
| NFR-12 | Browsers tested | 3 browsers | Cross-browser test |

---

# ITEM 7 — Requirements Per Module

## Module 1: Login and Registration
- User must fill name, email, password, phone, and role
- Password must be hidden (hashed) before saving
- Wrong login must show error message
- All pages need login to access (except login/register page)

## Module 2: AI Symptom Checker
- Patient can type symptoms in a text box
- Patient can click symptom tag buttons
- System sends symptoms to Gemini AI
- If AI fails, rule-based backup runs automatically
- Result is saved in the database with timestamp

## Module 3: Appointment Booking
- Patient selects doctor, date, time, and reason
- New appointment always starts as "Pending"
- Doctor can approve, cancel, or complete it
- Both patient and doctor can see appointment history

## Module 4: Prescription Module
- Doctor writes: diagnosis, medicines, instructions, follow-up date
- Prescription is linked to one patient and one doctor
- Patient sees all prescriptions on their dashboard

## Module 5: Admin Module
- Admin can see all users (patients, doctors)
- Admin can delete any user except themselves
- Admin can see all AI diagnoses and appointment stats

---

# ITEM 8 — Structured Requirements

This shows the **exact inputs and outputs** of the AI function.

```
FUNCTION NAME: analyze_symptoms

INPUTS:
  symptoms    = text written by patient
  patient_age = patient's age (number)
  patient_gender = Male / Female / Other

STEPS:
  1. Build a message for Gemini AI with symptoms and patient info
  2. Send message to Gemini AI API
  3. Wait for JSON response
  4. If response is wrong → use rule-based checker instead
  5. Save result to database

OUTPUT:
  disease_detected = "Pneumonia" or "Jaundice" or "Both" or "Neither"
  severity         = "Mild" or "Moderate" or "Severe"
  see_doctor       = true or false
  urgency          = time to see doctor
  recommendation   = what to do
  precautions      = list of safety tips

RULES:
  - Must always give a result (never crash)
  - Must finish in 10 seconds or less
```

---

# ITEM 9 — Tabular Computation

## How the System Decides the Disease

| Symptoms Present | Pneumonia Points | Jaundice Points | Decision | Severity |
|---|---|---|---|---|
| Chest pain + Fever + Cough + No breathing | 4 | 0 | Pneumonia | Severe |
| Chest pain + Fever + Cough | 3 | 0 | Pneumonia | Moderate |
| Fever + Fatigue only | 2 | 0 | Neither | Mild |
| Yellow skin + Dark urine + Nausea + Pain | 0 | 4 | Jaundice | Severe |
| Yellow eyes + Nausea | 0 | 2 | Jaundice | Mild |
| Chest pain + Yellow skin + Fever | 2 | 2 | Both | Moderate |

## Keyword Scoring Table (Rule-Based Backup)

| Keyword Found in Symptoms | Disease | Points Added |
|---|---|---|
| chest pain | Pneumonia | +1 |
| fever | Pneumonia | +1 |
| cough | Pneumonia | +1 |
| breathing, breath | Pneumonia | +1 |
| fatigue, tired | Pneumonia | +1 |
| chills, sweating | Pneumonia | +1 |
| yellow | Jaundice | +1 |
| dark urine | Jaundice | +1 |
| nausea, vomit | Jaundice | +1 |
| abdominal, stomach | Jaundice | +1 |
| weakness, appetite | Jaundice | +1 |

**Rule:** If Pneumonia score ≥ 3 → Pneumonia detected. If Jaundice score ≥ 2 → Jaundice detected.

---

# ITEM 10 — Detailed Scenarios

## Scenario 1: Sara Checks for Pneumonia

Sara is a 22-year-old female. She has had chest pain, high fever, and coughing for 4 days.

1. Sara opens browser and goes to `http://localhost:5000`
2. She clicks "Get Started" and fills the registration form as a Patient
3. She logs in and sees her patient dashboard
4. She clicks "🤖 AI Symptom Checker" from the menu
5. She clicks these symptom tags: **Chest Pain, High Fever, Persistent Cough, Difficulty Breathing**
6. She writes: "I have had these for 4 days"
7. She clicks "Analyze with AI" — a spinner shows for 3 seconds
8. Result appears: **Pneumonia Detected, Severity: Moderate, See Doctor: Yes (within 24 hours)**
9. Precautions shown: Stay warm, Use humidifier, Complete bed rest, Avoid cold drinks
10. Sara clicks "Book Doctor Appointment"
11. She selects **Dr. Ahmed Khan (Pulmonologist)**, picks June 21 at 10:00 AM
12. Appointment created — Status: **Pending**
13. Dr. Ahmed logs in, sees Sara's appointment, clicks **Approve**
14. Status changes to **Approved**
15. After meeting, Dr. Ahmed clicks **Complete** then **Prescribe**
16. He writes: Amoxicillin 500mg 3x daily, rest, drink water
17. Sara sees prescription on her dashboard

## Scenario 2: Dr. Ahmed Manages His Patients

Dr. Ahmed Khan is a Pulmonologist. He logs in after a busy morning.

1. He logs in with doctor@cliniq.com
2. Dashboard shows: Total Appointments: 5, Pending: 2 (shown in amber)
3. He sees Sara's request (Reason: "AI detected Pneumonia")
4. He clicks **✅ Approve** → Status: Approved
5. He sees another patient — Reason: "Yellow eyes and weakness" (Jaundice)
6. He thinks it needs a Hepatologist, so he clicks **❌ Cancel**
7. After Sara's consultation, he clicks **✔ Done** → Status: Completed
8. He clicks **💊 Prescribe** → fills diagnosis, medicines, instructions
9. Sara sees the prescription in her account

---

# ITEM 11–16 — USE CASE DIAGRAMS

## Master Use Case Diagram

![Master Use Case Diagram — ClinIQ System showing Patient, Doctor, Admin, and Gemini AI actors with all use cases](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\usecase_diagram_1781199355284.png)

**Explanation:** This diagram shows all the things users can do in ClinIQ.
- **Patient** can: Register, Login, Check Symptoms, Book Appointment, View Prescriptions
- **Doctor** can: Login, Approve/Cancel/Complete Appointments, Write Prescriptions
- **Admin** can: Login, Manage Users, View Reports
- **Gemini AI** is an external service used by the Symptom Checker

## Use Case Table

| Use Case | Who Does It | Steps | Result |
|---|---|---|---|
| Register | Guest | Fill form → Submit | Account created |
| Login | All Users | Enter email+password → Submit | Dashboard opens |
| Check Symptoms | Patient | Enter symptoms → AI analyzes | Diagnosis shown |
| Book Appointment | Patient | Choose doctor/date/time → Submit | Appointment pending |
| Approve Appointment | Doctor | Click Approve | Status = Approved |
| Write Prescription | Doctor | Fill form → Save | Patient gets Rx |
| View Prescriptions | Patient | Open dashboard | Rx list shown |
| Delete User | Admin | Click Delete → Confirm | User removed |

---

# ITEM 12 — Context Diagram

**What it shows:** ClinIQ in the middle, all outside people/systems around it, and what data flows between them.

> Note: See Architecture Diagram below for visual system boundary.

**Data Flows:**
- **Patient → ClinIQ:** Login info, symptoms, appointment request
- **ClinIQ → Patient:** Dashboard, AI result, prescriptions
- **Doctor → ClinIQ:** Login, approval decision, prescription
- **ClinIQ → Doctor:** Appointment lists, patient info
- **Admin → ClinIQ:** Login, user management actions
- **ClinIQ → Gemini AI:** Symptom text prompt
- **Gemini AI → ClinIQ:** JSON diagnosis result

---

# ITEM 17 — Sequence Diagrams

## Sequence 1: AI Symptom Check

![Sequence Diagram showing Patient, Browser, Flask Server, Gemini AI, and Database interaction during symptom analysis](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\sequence_diagram_1781199400574.png)

**Step-by-Step Explanation:**
1. Patient types symptoms and clicks "Analyze"
2. Browser sends the symptoms to Flask server
3. Flask builds an AI prompt with patient info + symptoms
4. Flask calls Gemini AI API
5. Gemini AI returns JSON result
6. Flask reads the JSON (disease, severity, recommendation)
7. Flask saves the result to the database
8. Flask sends the HTML page back to browser
9. Patient sees the AI result card on screen

## Sequence 2: Login Flow (Text)

| Step | Who | Action |
|---|---|---|
| 1 | User | Types email and password, clicks Sign In |
| 2 | Browser | Sends POST /login request |
| 3 | Flask | Looks up user in database by email |
| 4 | Database | Returns user record |
| 5 | Flask | Checks if password matches |
| 6a | Flask | If correct → creates session, redirects to dashboard |
| 6b | Flask | If wrong → shows error message |

## Sequence 3: Book Appointment (Text)

| Step | Who | Action |
|---|---|---|
| 1 | Patient | Selects doctor, date, time, reason |
| 2 | Browser | Sends POST /book-appointment |
| 3 | Flask | Checks patient is logged in |
| 4 | Flask | Creates appointment in database (status=pending) |
| 5 | Database | Saves appointment |
| 6 | Flask | Shows success message, redirects to dashboard |
| 7 | Patient | Sees appointment with "Pending" badge |

---

# ITEMS 18–21 — CLASS DIAGRAMS

## Full Class Diagram

![UML Class Diagram showing User, Patient, Doctor, Appointment, Diagnosis, and Prescription classes with relationships](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\class_diagram_1781199363922.png)

**What this shows:** All the data classes in ClinIQ and how they are connected.

## Generalization (Inheritance) — Item 20

![Generalization Hierarchy showing User as parent class with Patient, Doctor, and Admin as child classes](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\generalization_diagram_1781199436410.png)

**Simple explanation:** User is the parent class. Patient, Doctor, and Admin all inherit from User. This means they all have email, password, and name — but each also has its own special attributes.

## Class Descriptions Table

| Class | What It Stores | Main Actions |
|---|---|---|
| **User** | id, name, email, password, role, phone | login, logout, register |
| **Patient** | age, gender, medical history | book appointment, check symptoms |
| **Doctor** | specialization, license number | approve appointment, write prescription |
| **Appointment** | patient, doctor, date, time, status | approve, cancel, complete |
| **Diagnosis** | symptoms, AI result, disease found | save, analyze |
| **Prescription** | medicines, instructions, follow-up date | create, view |

## Associations (Item 18)
- One **User** has one **Patient** or **Doctor** profile
- One **Patient** has many **Appointments**
- One **Doctor** has many **Appointments**
- One **Patient** has many **Diagnoses**
- One **Patient** receives many **Prescriptions**
- One **Doctor** writes many **Prescriptions**

## Aggregation (Item 21)
The **ClinIQ System** is made up of:
- Many Patients
- Many Doctors
- Many Appointments
- Many Diagnoses
- Many Prescriptions

If ClinIQ system stops, all these parts also stop — that is aggregation.

---

# ITEMS 22–23 — ACTIVITY DIAGRAM

## Activity Diagram: AI Symptom Check

![Activity Diagram for AI Symptom Check showing start, patient steps, AI decision, fallback, database save, and end](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\activity_diagram_1781199436410.png)

**Steps explained simply:**
1. Patient logs in → Opens Symptom Checker
2. Clicks symptom tags or types description
3. Clicks "Analyze with AI"
4. **Decision:** Is AI available?
   - YES → Call Gemini AI → Is response valid?
     - YES → Read disease/severity/recommendation
     - NO → Use rule-based backup
   - NO → Use rule-based backup
5. Save result to database
6. Show result to patient
7. **Decision:** Does patient need a doctor?
   - YES → Show "Book Appointment" button
   - NO → Show precautions only

## Process Diagram: Appointment Lifecycle (Item 23)

**Steps:** Patient Books → Pending → Doctor Reviews → Approved or Cancelled → If Approved: Consultation → Completed → Doctor Prescribes → Patient gets Prescription

---

# ITEMS 24–25 — STATE DIAGRAMS

## State Diagram: Appointment Status

![State Diagram for Appointment showing Pending, Approved, Completed, and Cancelled states with transitions](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\state_diagram_1781199426847.png)

**States explained:**
- 🔴 **Start** → Patient books
- 🟡 **Pending** → Waiting for doctor's decision
- 🟢 **Approved** → Doctor said yes
- 🔵 **Completed** → Consultation done
- 🔴 **Cancelled** → Doctor or patient cancelled

## Structured State Table (Item 25)

| State | How to Enter | What You Can Do | How to Leave |
|---|---|---|---|
| Pending | Patient submits booking | Doctor: Approve or Cancel | Doctor takes action |
| Approved | Doctor approves | Doctor: Complete, Prescribe; Patient: Cancel | Consultation done or cancelled |
| Completed | Doctor marks done | Doctor: Write Prescription | Terminal — no exit |
| Cancelled | Anyone cancels | Nothing | Terminal — no exit |

---

# ITEMS 26–28 — ARCHITECTURE DIAGRAMS

## Software Architecture — 3 Layers (Item 26)

![3-Tier Architecture Diagram showing Presentation, Application, Data layers and External Services](C:\Users\hafsa ashraf\.gemini\antigravity\brain\c5aad03c-8281-4b10-aec2-2f2f9d8e92c9\architecture_diagram_1781199373845.png)

**Layer 1 — Presentation (Frontend):**
What the user sees: HTML pages, CSS design, JavaScript buttons

**Layer 2 — Application (Backend):**
The brain: Flask handles requests, checks login, calls AI, runs business logic

**Layer 3 — Data:**
The storage: SQLAlchemy talks to SQLite database, saves and reads all data

**External Service:**
Google Gemini AI API — only called when patient runs symptom checker

## High-Level Architecture (Item 28)

```
[User's Browser]  →  HTTP Request  →  [Flask App (app.py)]
[Flask App]       →  SQL Query     →  [SQLite Database]
[Flask App]       →  API Call      →  [Gemini AI]
[Gemini AI]       →  JSON Result   →  [Flask App]
[Flask App]       →  HTML Page     →  [User's Browser]
```

---

# ITEM 29 — All Object Classes

| Class Name | All Attributes | All Methods |
|---|---|---|
| User | id, name, email, password_hash, role, phone, created_at | login(), logout(), register(), get_id() |
| Patient | id, user_id, age, gender, blood_group, medical_history | getAppointments(), getDiagnoses(), getPrescriptions() |
| Doctor | id, user_id, specialization, license_number, experience_years | approveAppointment(), writePrescription(), getPatients() |
| Appointment | id, patient_id, doctor_id, date, time, reason, status, notes, created_at | approve(), cancel(), complete() |
| Diagnosis | id, patient_id, symptoms, ai_result, disease_detected, severity, confidence, created_at | analyzeSymptoms(), save() |
| Prescription | id, patient_id, doctor_id, diagnosis, medicines, instructions, follow_up_date, created_at | create(), view() |

---

# ITEM 30 — Detailed Usage Scenario

## Complete Story: From Symptom to Cure

**Characters:** Sara (Patient), Dr. Ahmed Khan (Pulmonologist)
**Date:** June 20, 2026

---

**Day 1 — Sara feels sick:**

Sara has chest pain and fever for 4 days. She opens ClinIQ on her browser at 9:00 PM.

She is new, so she:
1. Clicks "Get Started"
2. Chooses Patient role
3. Fills: Name: Sara Ahmed, Email: sara@cliniq.com, Age: 22, Gender: Female
4. Clicks Register → Success message → Login page
5. Enters email and password → Dashboard opens

**Stats on her dashboard:** 0 Appointments, 0 AI Checks, 0 Prescriptions

---

**Sara uses AI Symptom Checker:**

6. Clicks "🤖 AI Symptom Checker"
7. Clicks symptoms: Chest Pain ✓, High Fever ✓, Persistent Cough ✓, Difficulty Breathing ✓
8. Also types: "I have had these for 4 days, my temperature is 103°F"
9. Clicks "Analyze with AI" — spinner shows for 3 seconds

**AI Result:**
- 🫁 **Pneumonia Detected**
- Severity: **Moderate**
- Urgency: **Within 24 hours**
- Recommendation: "Strong signs of pneumonia. See a pulmonologist immediately. Start antibiotics."
- Precautions: Stay warm, Use humidifier, Bed rest, Avoid cold drinks, Check temperature every 4 hours

---

**Sara books appointment:**

10. Clicks "Book Doctor Appointment"
11. Goes to dashboard, selects Dr. Ahmed Khan (Pulmonologist)
12. Picks June 21, 10:00 AM
13. Writes reason: "AI says Pneumonia — chest pain and breathing difficulty"
14. Clicks Book → **Appointment: PENDING**

---

**Day 2 — Dr. Ahmed acts:**

15. Dr. Ahmed logs in with doctor@cliniq.com
16. Sees dashboard: 1 Pending appointment (Sara)
17. Reads Sara's reason, clicks **✅ Approve**
18. Sara's appointment: **APPROVED**

---

**After consultation:**

19. Dr. Ahmed meets Sara, examines her
20. Clicks **✔ Done** → appointment: COMPLETED
21. Clicks **💊 Prescribe**
22. Sees Sara's profile (22F)
23. Fills prescription:
    - Diagnosis: Community-acquired Pneumonia
    - Medicines: Amoxicillin 500mg 3x daily × 7 days; Paracetamol 500mg as needed
    - Instructions: Complete bed rest, drink 2L water daily, avoid cold drinks
    - Follow-up: June 28, 2026
24. Clicks Save

---

**Sara sees her prescription:**

25. Sara logs back in → My Prescriptions tab
26. Sees: **Dr. Ahmed Khan → Amoxicillin 500mg... Follow-up: June 28**

✅ **Complete journey done!**

---

# ITEM 31 — Reliability Terms

| Word | Simple Meaning | In ClinIQ |
|---|---|---|
| **Availability** | System is working and ready to use | ClinIQ should be up 99% of the time |
| **MTBF** | Average time between crashes | Expected: more than 720 hours |
| **MTTR** | How fast we fix a crash | Target: under 30 minutes |
| **Fault Tolerance** | System keeps working even if one part fails | If AI fails, rule-based backup runs |
| **Redundancy** | Having a backup system | Rule-based checker is the AI backup |
| **Graceful Degradation** | Reduced function instead of full stop | AI fails → still gives result using rules |
| **Error Handling** | Catching problems before they crash the app | Try-except around all AI calls |
| **Data Integrity** | Data saved correctly without corruption | SQLAlchemy database transactions |
| **Recovery** | Getting back to normal after a problem | Database file can be restored from backup |
| **Robustness** | System handles bad/unexpected input | Forms are validated before processing |

---

# ITEM 32 — Safety Terms

| Word | Simple Meaning | In ClinIQ |
|---|---|---|
| **Medical Disclaimer** | Warning that AI is not a real doctor | "For information only" shown on AI results |
| **AI Accuracy Risk** | AI can sometimes be wrong | Doctor must confirm before treatment |
| **Data Privacy** | Patient health info must be kept safe | Passwords hashed, API keys hidden |
| **Informed Consent** | User knows AI limitations before using | Disclaimer shown before symptom check |
| **Fail-Safe Default** | When in doubt, choose the safest option | AI failure → always recommend seeing doctor |
| **Human Override** | Doctor can change AI's decision | Doctor writes their own prescription |
| **Critical Function** | Functions that must never fail | Login and AI fallback always work |
| **Error Propagation** | One error should not cause more errors | AI error is caught and handled alone |
| **Auditability** | Track who did what and when | All diagnoses saved with timestamp and patient ID |
| **Risk Mitigation** | Reducing the chance of harm | Multiple disclaimers + doctor workflow required |

---

# ITEM 33 — Security Terms

| Word | Simple Meaning | In ClinIQ |
|---|---|---|
| **Authentication** | Proving who you are | Email + password login |
| **Authorization** | Checking what you are allowed to do | Patients cannot access doctor pages |
| **Password Hashing** | Turning password into unreadable code | Werkzeug PBKDF2-SHA256 hashing |
| **Session Management** | Remembering you are logged in | Flask secure sessions |
| **API Key Security** | Hiding the Gemini AI key | Stored in .env file, not in code |
| **SQL Injection Prevention** | Stopping hackers from breaking the database | SQLAlchemy uses safe parameterized queries |
| **Access Control** | Only right people see right pages | @login_required on every page |
| **Data Encryption** | Scrambling data so hackers cannot read it | HTTPS/TLS in production deployment |
| **Input Validation** | Checking that form data is correct | HTML required fields + Flask checks |
| **Least Privilege** | Users only get what they need | Patients cannot see admin features |
| **Audit Logging** | Recording every action | Flask logs every HTTP request |
| **Secrets Management** | Keeping passwords and keys safe | python-dotenv + .gitignore |
| **Dependency Security** | Using safe, updated libraries | requirements.txt with pinned versions |
| **CSRF Prevention** | Stopping fake form submissions | Flask secret key + can add Flask-WTF |

---

# SUMMARY — All 33 Items

| # | Item | ✅ Done |
|---|---|---|
| 1 | Development Model (Incremental) | ✅ |
| 2 | User Stories (7 stories) | ✅ |
| 3 | Test Cases (8 test cases) | ✅ |
| 4 | Functional Requirements (16) | ✅ |
| 5 | Non-Functional Requirements (12) | ✅ |
| 6 | NFR Metrics Table | ✅ |
| 7 | Requirements Per Module | ✅ |
| 8 | Structured Requirements | ✅ |
| 9 | Tabular Computation | ✅ |
| 10 | Detailed Scenarios | ✅ |
| 11 | Use Case Diagram | ✅ With Image |
| 12 | Context Diagram | ✅ |
| 13 | Process Model | ✅ |
| 14 | Individual Use Cases | ✅ |
| 15 | Use Case Table | ✅ |
| 16 | Per-Actor Use Cases | ✅ |
| 17 | Sequence Diagrams (3) | ✅ With Image |
| 18 | Class Associations | ✅ With Image |
| 19 | Class Model | ✅ With Image |
| 20 | Generalization Hierarchy | ✅ With Image |
| 21 | Aggregation | ✅ |
| 22 | Activity Diagram | ✅ With Image |
| 23 | Application Processes | ✅ |
| 24 | State Diagrams | ✅ With Image |
| 25 | Structured State Table | ✅ |
| 26 | Software Architecture | ✅ With Image |
| 27 | Context Diagram | ✅ |
| 28 | High-Level Architecture | ✅ |
| 29 | All Object Classes | ✅ |
| 30 | Detailed Usage Scenario | ✅ |
| 31 | Reliability Terms (10) | ✅ |
| 32 | Safety Terms (10) | ✅ |
| 33 | Security Terms (14) | ✅ |

---

*ClinIQ v1.0.0 — SE CEP Documentation — Hafsa Ashraf*
*Bahria University — Software Engineering*
