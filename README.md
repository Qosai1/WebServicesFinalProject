# 🕊️ Human Rights Monitor MIS

A secure, data-driven web application for documenting, tracking, and analyzing human rights violations. Developed using **FastAPI**, **MongoDB**, and a modern frontend (e.g., React or Streamlit).

## 📚 Project Overview

This system empowers human rights organizations to:

- 📌 **Document violations** like arbitrary detention and forced displacement.
- 🧑‍🤝‍🧑 **Securely manage victim/witness records** with optional anonymity.
- 📤 **Receive incident reports** from web, mobile, or NGO sources.
- 📊 **Visualize data** to identify patterns, trends, and legal evidence.

## 🧩 System Modules

### 1️⃣ Case Management Module
- Track case lifecycles (new → investigation → resolved).
- CRUD operations for human rights cases.
- Status history, attachments, and advanced filtering.

### 2️⃣ Incident Reporting Module
- Public form for reporting violations with anonymous option.
- Geolocation tagging and media attachments.
- Analytics by violation type, location, and time.

### 3️⃣ Victim/Witness Database
- Secure storage of victim/witness data with role-based access.
- Risk level tracking (low, medium, high).
- Support for pseudonyms and secure messaging.

### 4️⃣ Data Visualization & Analytics
- Dashboards for case/report trends, violation heatmaps, and time-series graphs.
- Export reports in PDF and Excel.
- Filtering by date, region, or violation type.

## 🛠️ Tech Stack

| Layer           | Technology               |
|----------------|--------------------------|
| Backend         | Python + FastAPI         |
| Database        | MongoDB Atlas            |
| Frontend        | React / Streamlit        |
| Visualization   | Plotly / Matplotlib / D3 |
| Geolocation     | Google Maps / Leaflet.js |
| Authentication  | JWT / OAuth2             |

## 🚀 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/human-rights-monitor.git
   cd human-rights-monitor
Backend Setup

bash
Copy
Edit
cd backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Setup

bash
Copy
Edit
cd frontend
npm install
npm start
Environment Variables
Create a .env file for the backend:

env
Copy
Edit
MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/hrm
SECRET_KEY=your_secret_key
📬 API Endpoints
Module	Endpoint Example	Method
Case Management	/cases/, /cases/{id}	GET/POST/PATCH/DELETE
Incident Reports	/reports/analytics, /reports/	GET/POST
Victim Database	/victims/case/{id}	GET/PATCH
Analytics	/analytics/violations	GET

👉 Full documentation available via /docs (Swagger UI)

📊 Sample Dashboard Preview
Add screenshot here showing data visualizations

📁 Folder Structure
pgsql
Copy
Edit
📦human-rights-monitor
 ┣ 📂backend
 ┃ ┣ 📜main.py
 ┃ ┣ 📜routers/
 ┃ ┣ 📜models/
 ┃ ┣ 📜schemas/
 ┃ ┗ 📜.env
 ┣ 📂frontend
 ┃ ┣ 📜App.js
 ┃ ┣ 📜components/
 ┃ ┗ 📜public/
 ┗ 📜README.md
👥 Team Members
Qosai Badaha – Case Management & Data Analytics

Gazal AbuFarha – Incident Reporting & Frontend

Shahd Adawi – Victim Database & Security
