# Bangkok Concierge – AI Travel Planner Agent

An AI-powered concierge and travel planner designed for travelers visiting Bangkok.  
This project demonstrates multi-agent orchestration, structured planning, tool usage, and optional API deployment.  
Created as a Capstone Project submission for the **Kaggle AI Agents Intensive Course**.

---

## ✨ Features

### 🧠 1. Travel Planning Agent
- Generates **day-by-day** itinerary customized to user interests.
- Handles preferences such as cafés, shopping, food, night markets, temples.
- Produces clean structured output (JSON or Markdown).
- Supports revisions (shorter, longer, more cafés, less walking…).

### 🤖 2. Multi-Agent Architecture
- **Planner Agent (Core)**
- **Restaurant Agent**
- **Shopping Agent**
- **Transport Agent**
- Optional routing logic determines which agent handles each task.

### 🛠 3. Tools & Concepts Demonstrated
- Multi-agent system  
- Sequential + parallel agent workflows  
- Context engineering  
- Tool calling  
- Memory / session state (optional)  
- Optional deployment (Cloud Run)

---

## 🏆 Problem Statement

Travelers visiting **Bangkok** often face overwhelming choices—hundreds of malls, markets, cafés, temples, night activities, and transport systems.  
Manual planning is time-consuming, and itineraries online are generic.

This project solves that by providing:
- **Personalized**, **practical**, and **structured** travel plans
- Immediate adjustments based on user preferences
- Multi-agent orchestration for different information domains

---

## 🤖 Why Agents?

Agents are ideal because:
- Travel planning is a **multi-step reasoning** process
- Different sub-domains require **different experts** (restaurants, shopping, transport)
- A Planner Agent can coordinate other agents to create a well-structured final itinerary
- Agents can call tools, evaluate options, and revise results in loops

---

## 🧱 What I Created – Architecture

A simple multi-agent architecture:
User
↓
Frontend (Kaggle Notebook / Chat Interface)
↓
Planner Agent (Core)
├── Restaurant Agent
├── Shopping Agent
└── Transport Agent
↓
Structured Plan Output (JSON / Markdown)

Visual architecture diagram (“architecture_flowchart.png”) included in the repository.

---

## 🎬 Demo

Example user prompt:
I’m going to Bangkok for 3 days.
I love cafés, shopping malls, and night markets.
Please plan my itinerary.

Example output (shortened):
Day 1
	•	Morning: ICONSIAM
	•	Afternoon: Roast Coffee
	•	Evening: Jodd Fairs Night Market

Day 2
	•	Morning: Wat Arun
	•	Lunch: Krua Apsorn
  …
Full demo included in `main.ipynb`.

---

## 🔧 The Build – Tools & Technologies Used

- Python (Kaggle Notebook)
- Google Gemini (for LLM-powered agents)
- Multi-agent routing logic
- Tool invocation
- Context engineering
- Optional Cloud Run deployment for API endpoint
- Markdown documentation for evaluation

---

## ☁️ Optional Deployment (Bonus)

Below are instructions to deploy the Planner Agent as an API on **Google Cloud Run**.

### Build Docker image
gcloud builds submit –tag gcr.io/PROJECT_ID/bangkok-planner
### Deploy
gcloud run deploy bangkok-planner 
–image gcr.io/PROJECT_ID/bangkok-planner 
–platform managed 
–allow-unauthenticated 
–memory 1Gi
### Use API
POST https://your-cloudrun-url/run
{
“preferences”: {
“days”: 3,
“interests”: [“shopping”, “cafes”, “night markets”]
}
}
---

## 🔮 If I Had More Time…

- Add real-time restaurant & event lookup  
- Add Google Maps routing integration  
- Add memory for traveler profiles  
- Add a UI web frontend  
- Deploy as a chatbot for LINE / WhatsApp  
- Improve long-horizon planning chain quality  

---

## 📎 Attachments (Links for Kaggle Submission)

> Add these links into the “Attachments” section of the Kaggle Capstone form.  
> These are also included in the README for clarity.

### 🔗 GitHub Repository  
👉 https://github.com/ejaup6/bangkok-concierge  
*(Replace with your actual repo link)*

### 🔗 Demo (Optional)
- Colab demo: _link here (optional)_  
- Cloud Run API: _link here (optional)_  
- Architecture diagrams: included in project repo  
- Video demo (YouTube, optional): _link here_

---

## 📁 Project Structure
/project
├── main.ipynb               # Main demo notebook
├── planner/
│     ├── agent_planner.py
│     ├── router.py
│     ├── tools.py
│     └── utils.py
├── api/
│     ├── app.py             # For Cloud Run (optional)
│     └── requirements.txt
├── architecture_flowchart.png
├── README.md
---

## 📄 License
MIT License.

---

## 👤 Author
Lin Chiu Min
Bangkok Concierge – AI Travel Planner Agent  
Capstone Project for Kaggle AI Agents Intensive Course
