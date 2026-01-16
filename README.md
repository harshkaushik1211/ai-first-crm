# AI-First CRM – HCP Interaction Logging (Task 1)

## 📌 Overview
This project implements **Task 1: AI-First CRM – HCP Log Interaction Screen**.

The goal is to replace traditional form-based CRM interaction logging with an **AI-first, chat-based experience**, where a sales representative can describe a doctor interaction in natural language and the system automatically extracts structured CRM data.

The solution uses **FastAPI**, **LangGraph**, and a **Large Language Model (LLM)** to orchestrate multiple AI tools in a single workflow and persist results into a database.

---

## 🎯 Problem Statement
Traditional CRM systems require manual data entry after each HCP visit, which is:
- Time-consuming
- Error-prone
- Inconsistent across users

This project demonstrates how **AI can act as the primary interface**, converting free-text interactions into structured CRM records automatically.

---

## 🧱 High-Level Architecture

### Frontend
- Built with **React**
- Chat-based interface for logging interactions
- Sends natural language input to backend APIs

### Backend
- Built with **FastAPI**
- Uses **LangGraph** for AI workflow orchestration
- Integrates an **LLM** for information extraction
- Persists data using **SQLAlchemy + SQLite**

### Database
- SQLite (used for simplicity and local development)
- Easily replaceable with MySQL or PostgreSQL

---

## 🧠 AI Workflow Using LangGraph

The backend uses **LangGraph** to define a multi-step AI workflow.
Each user interaction flows through **five logical stages**:

### LangGraph Tools / Nodes

1. **log_interaction**
   - Uses the LLM to extract structured fields from raw text
   - Example: HCP name, interaction summary

2. **sentiment_tool**
   - Determines sentiment of the interaction (Positive / Neutral / Negative)

3. **followup_tool**
   - Recommends next actions based on context and sentiment

4. **material_tool**
   - Suggests supporting sales material (e.g., brochure, comparison study)

5. **END**
   - Aggregates final structured output and returns the response

All tools operate on a **shared state** and are executed sequentially within a **single request**.

---

## 🚀 Features
- Chat-based CRM interaction logging
- AI-powered structured data extraction
- Sentiment analysis
- Follow-up recommendations
- Material suggestions
- Database persistence
- Clean and minimal UI

---

## 🧪 Example Interaction

### Input
Met Dr Anil Kumar at Apollo Clinic. Discussed Product X in detail.
Doctor showed strong interest, appreciated the clinical results,
and requested a digital brochure and follow-up visit next month.


### Output
```json
{
  "hcp_name": "Dr. Anil Kumar",
  "summary": "Positive discussion about Product X",
  "sentiment": "Positive",
  "follow_up": "Schedule follow-up visit",
  "material": "Product brochure"
}
```



🛠️ Tech Stack
Frontend

React

Axios

CSS (index.css, App.css)

Backend

FastAPI

LangGraph

Groq LLM

SQLAlchemy

Database

SQLite



## Running the Project Locally :-

Backend Setup
  cd backend
  python -m venv venv
  venv\Scripts\activate   # Windows
  pip install -r requirements.txt
  uvicorn app.main:app --reload

Frontend Setup
  cd frontend
  npm install
  npm start


## Environment Variables

  - Secrets are managed using environment variables.

  - Create a local .env file inside backend/:

     GROQ_API_KEY=your_actual_api_key


  - A sample file is provided:

     backend/.env.example

  - Note: .env files are excluded from version control for security.


## Design Decisions

Chat-based UI chosen to emphasize AI-first CRM experience

LangGraph used for modular, explainable AI workflows

SQLite used for simplicity and ease of evaluation

UI kept minimal to focus on AI logic and architecture


## Author

Harsh Kaushik
B.Tech Computer Science (AI & ML)
