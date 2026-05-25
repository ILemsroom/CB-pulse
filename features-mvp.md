My bad! Let’s strip out the setup and focus purely on the core product specs.

To build a high-utility, scalable Computer-Based Testing (CBT) platform for Nigerian medical and nursing students, you must avoid over-engineering. An MVP should only contain features that directly help them pass their professional board exams (NMCN, MDCN, or internal MBBS blocks) and features that let you collect payments.

Here is the exact feature list required for the MVP, broken down by user flow.

---

## 1. Core CBT Examination Engine

The main interface must mimic the simplicity of actual professional examination software (like JAMB or the council interfaces) to reduce student anxiety.

* **Timed Mock Exams:** A countdown timer that automatically freezes the exam and submits the student's answers when the time runs out (typically 60 to 180 minutes depending on the paper).
* **Grid Navigation Layout:** A grid panel of question numbers (e.g., 1 to 100) that shifts color based on state:
* *Green:* Answered.
* *Grey:* Unanswered.
* *Purple/Flagged:* Flagged for review (allowing students to quickly jump back to difficult questions before final submission).


* **Instant Scoring & Performance Breakdown:** The moment a student clicks "Submit," they receive an aggregate percentage score (e.g., 68%).

## 2. Post-Exam "Explanations & Rationales" (The Core Value)

Medical and nursing students do not just buy past questions to find out *what* they got wrong; they buy them to learn *why* they got it wrong so they don't repeat the mistake on the real field.

* **Detailed Answer Explanations (Rationales):** For every reviewed question, display the correct answer alongside a clinical rationale explaining the pathology, drug mechanism, or nursing care plan behind it.
* **Reference Tracking:** Include the specific textbook chapter or council guideline standard (e.g., *“According to the NMCN Guideline...”* or *“Brunner & Suddarth's Medical-Surgical Nursing”*) to build institutional credibility.

## 3. Basic Category Filtering

Medical exams are strictly modular. A student studying for a specific posting or block shouldn’t be forced to take a generic mixed exam.

* **Specialty/Subject Filtering:** Allow users to filter practice questions by specific boards or subjects:
* *Nursing:* Medical-Surgical, Pediatrics, Mental Health, Midwifery.
* *Medicine:* Pharmacology, Anatomy, Obstetrics & Gynecology, Pathology.


* **Year-Based Selectors:** Ability to select specific past council exam papers (e.g., "MDCN April 2024 Diet").

## 4. Frictionless "Naija-Style" Billing Paywall

Because card failure rates can be high and students are highly collaborative, the paywall needs to be solid but highly accessible.

* **Freemium Lock Mechanism:** Access to 1 partial mock exam (e.g., 20 questions) is completely free to prove the system works. All full-length past papers and rationales are blurred behind a "Unlock Full Exam Pack" overlay.
* **Multi-Channel Payment Gateway Integration (Paystack/Flutterwave):** A checkout modal allowing payment via:
* *Direct Bank Transfer:* The most trusted payment method for Nigerian students.
* *USSD & Card:* For quick automated processing.


* **Webhook-Driven Access Activation:** An automated listener that instantly flips the user's account to "Premium" status the exact second a payment is confirmed, removing human intervention entirely.

## 5. Lean Admin Interface (For Content Upload)

You need a quick, structured way to populate your platform without touching code or editing database rows directly.

* **Bulk Question Ingestion (Excel/CSV Upload):** A private admin page where you can upload an Excel template containing columns for `Question_Text`, `Option_A`, `Option_B`, `Option_C`, `Option_D`, `Correct_Option`, and `Rationale`. This allows you to scale your question bank rapidly.
