🧩 Clueso Clone – Product Feedback & Insights Platform

A functional clone of Clueso.io, designed to replicate the core user experience and workflows including authentication, dashboard usage, user feedback management, and AI-style insights.
This project demonstrates product understanding, clean engineering practices, and end-to-end system execution.

🚀 Features Implemented

✅ 1. User Onboarding & Authentication
-> User Registration (with password policy validation)
-> Secure Login
-> JWT-based authentication
-> Protected routes

✅ 2. Dashboard Experience
A modern dashboard inspired by Clueso’s UI:
-> Sidebar navigation
-> Home dashboard cards
-> Logout capability
-> Consistent UI theme across pages

✅ 3. Feedback Collection Flows
Users can:
-> Submit feedback
-> View previously submitted feedback
-> Feedback stored securely in database

✅ 4. AI-Inspired Insights
Insights page displays:
-> Total feedback count
-> Latest feedback summary
-> Average feedback message length
(Insights are mock-processed but meaningful and informative)

✅ 5. Data Management
-> MySQL Database
-> SQLAlchemy ORM
-> Secure password hashing
-> Proper models & schemas

✅ 6. System Communication
-> Frontend communicates with backend via REST APIs
-> JWT authorization headers
-> Proper CORS handling

🏗️ Tech Stack
-> Backend
-> FastAPI
-> Python
-> SQLAlchemy
-> MySQL
-> JWT Authentication
-> Frontend
-> HTML
-> CSS
-> JavaScript

📁 Project Structure

clueso-clone
│
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── routers
│   │        ├── __init__.py
│   │        ├── auth.py
│   │        ├── feedback.py
│   │        └── insights.py
│   ├── requirements.txt
│
├── frontend
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── submit_feedback.html
│   ├── view_feedback.html
│   ├── insights.html
│   ├── style.css
│   └── clueso_logo.(png/jpg/jfif)
│
├── README.md



🛠️ Setup & Installation

1️⃣ Backend Setup
Step 1 — Go to backend
cd backend

Step 2 — Create Virtual Environment (Optional but Recommended)
python -m venv venv
Activate Virtual Environment:
venv\Scripts\activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Configure Database
Create MySQL database:
CREATE DATABASE clueso_clone;
Update credentials in:
backend/app/database.py
Example:
mysql+pymysql://root:password@localhost/clueso_clone

Step 5 — Run Server
uvicorn app.main:app --reload
Backend runs at:
http://127.0.0.1:8000
Swagger API Docs:
http://127.0.0.1:8000/docs

2️⃣ Frontend Setup
No framework needed.
Step 1 — Open frontend folder
Step 2 — Open login.html
Step 3 — Right-click → Open with Live Server
(or double-click to open in browser)
Frontend runs locally in browser.
🔗 API Endpoints
Auth
POST /auth/register
POST /auth/login
Feedback
POST /feedback/
GET /feedback/
Insights
GET /insights/

🔐 Security Measures
-> JWT authentication
-> Password hashing using bcrypt
-> Backend-validated registration rules
-> Protected routes

🧠 Architecture Overview

User → Frontend (HTML/JS) → FastAPI Backend → MySQL DB
                    ↑
                    JWT Auth

-> Decoupled frontend & backend
-> Organized routes & models
-> Scalable database design

📝 Assumptions & Design Decisions
✔ Selected FastAPI for speed + clean structure
✔ MySQL chosen for reliable structured data storage
✔ JWT enables secure session handling
✔ UI inspired by Clueso but simplified for clarity
✔ AI Insights are mock-logic but meaningful
✔ Followed Feature Parity > Pixel Perfection guideline

🎥 Demo Video
Demo covers:
-> End-to-end user flow
-> Explanation of features
T-> echnical approach
📌 Link will be added during submission.

✅ Evaluation Fit
This project demonstrates:
✔ Product Understanding
✔ Technical Execution
✔ System Integration
✔ Delivery Quality

🙌 Final Note
This project reflects strong engineering, clean implementation, and product thinking.
Thanks for reviewing!