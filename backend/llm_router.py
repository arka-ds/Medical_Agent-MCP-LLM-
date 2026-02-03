from prompts import (
    BOOK_APPOINTMENT_PROMPT, 
    CHECK_APPOINTMENT_PROMPT, 
    DOCTOR_SCHEDULE_PROMPT,
    COLLECT_EMAIL_PROMPT,
    CHAT_PROMPT
)

def choose_prompt(user_input: str) -> str:
    text = user_input.lower()

    if "book" in text:
        return BOOK_APPOINTMENT_PROMPT
    if "@" in text or "email" in text:
        return COLLECT_EMAIL_PROMPT

    if "schedule" in text or "availability" in text or "my schedule" in text:
        return DOCTOR_SCHEDULE_PROMPT

    if "id" in text or "appointment" in text or "booking number" in text or "reference number" in text or "booking id" in text or "reference id" in text or "appointment id" in text:
        return CHECK_APPOINTMENT_PROMPT

    if "email" in text:
        return COLLECT_EMAIL_PROMPT
    if "hello" in text or "hi" in text or "thanks" in text:
        return CHAT_PROMPT

    #raise ValueError("Could not determine intent from user input")
    return CHAT_PROMPT