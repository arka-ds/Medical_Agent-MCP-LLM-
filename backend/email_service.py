#---------------------------------Email Service--------------------------------------
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_booking_email(to_email: str, message: str) -> bool:
    try:
        msg = EmailMessage()
        msg["Subject"] = "Appointment Confirmation"
        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg.set_content(
            f"""
Hello,

{message}

Thank you,
Medical Assistant
"""
        )

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)

        #print("📧 Gmail SMTP email sent")
        return True

    except Exception as e:
        #print("Email failed:", str(e))
        return False
