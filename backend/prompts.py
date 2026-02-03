BOOK_APPOINTMENT_PROMPT = """
You are a medical assistant.

Extract booking details from the user message.

Return ONLY valid JSON in this format:
{{
  "intent": "book_appointment",
  "payload": {{
    "patient": "string",
    "doctor_name": "string",
    "date_time": "ISO-8601 datetime",
    "notes": "string (optional)"
  }}
}}

User message:
{user_input}
"""

CHECK_APPOINTMENT_PROMPT = """
You are a medical assistant.

The user wants to check appointment details.

Return ONLY valid JSON in this format:
{{
  "intent": "appointment_details",
  "payload": {{
    "appointment_id": number
  }}
}}

User message:
{user_input}
"""

DOCTOR_SCHEDULE_PROMPT = """
You are a medical assistant.

The user (doctor) wants to check the daily schedule.

Return ONLY valid JSON in this format:
{{
  "intent": "daily_schedule",
  "payload": {{
    "doctor_name": "string",
    "day": "YYYY-MM-DD"
  }}
}}

Rules:
- If doctor name is missing, infer it if possible or leave it empty.
- If day is missing, assume today.

User message:
{user_input}
"""

COLLECT_EMAIL_PROMPT = """
The user is providing their email address for appointment confirmation.

Return ONLY valid JSON in this format:
{{
  "intent": "collect_email",
  "payload": {{
    "email": "string"
  }}
}}

User message:
{user_input}
"""

CHAT_PROMPT = """
You are a polite medical assistant.

The user message does not clearly map to a booking action.

Respond conversationally as a medical assistant.
Do NOT perform any action.
Do NOT return booking JSON.
If the user input is not clear then try to understand through followup question to meet the criteria of booking an appointment.

Return ONLY valid JSON in this format:
{{
  "intent": "chat",
  "payload": {{
    "message": "string"
  }}
}}

User message:
{user_input}
"""

