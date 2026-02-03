# Medical Appointment Booking Agent (LLM + MCP)

A conversational **medical appointment assistant** that uses a **Large Language Model (Claude)** for intent extraction and a **deterministic Python backend** for reliable execution.

This project demonstrates how LLMs can be safely integrated into real systems by clearly separating **understanding (LLM)** from **execution (backend logic)**.

---

##  What This Project Does

The agent allows users to interact in natural language to perform medical appointment–related tasks.

### Patient Capabilities
- Book medical appointments with doctors
- Provide missing details through follow-up questions
- Receive booking confirmation via email
- Retrieve appointment details using appointment ID

### Doctor Capabilities
- View daily schedules for a specific date
- Receive daily schedules via email




## Architecture Overview

User Input
↓
Claude (Intent & Payload Extraction)
↓
MCP Agent
↓
Deterministic Core Logic
↓
PostgreSQL Database
↓
Email Notification Service



## File Structure

Doctor_Appoinment/
│
├── backend/
│ ├── agent.py
│ ├── core.py
│ ├── llm_parser.py
│ ├── llm_router.py
│ ├── prompts.py
│ ├── database.py
│ ├── email_service.py
│ ├── run_agent_once.py # CLI entry point
│ └── init.py
|---- frontend #Not prrepared
|---- requirement.txt
|---- README.md


## Tech Stack

- **Python 3.12**
- **Anthropic Claude API**
- **MCP**
- **PostgreSQL**
- **SQLAlchemy**
- **SendGrid (Email)**



Arka
B.Tech CSE (Data Science)
Brainware University
Interested in applied AI, RAG, Agentic AI

