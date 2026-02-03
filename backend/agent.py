#-----------------------Defining Agents Intent--------------------------------------------------

import asyncio
from backend.core import (
    book_appointment_core,
    get_doctor_availability_core,
    get_doctor_schedule_core,
    get_appointment_details_core,
)
from datetime import date
from backend.email_service import send_booking_email

REQUIRED_SLOTS = {
    "book_appointment": ["doctor_name", "date_time"],
    "daily_schedule": ["doctor_name", "day"],
}

def get_missing_slots(intent: str, payload: dict):
    required = REQUIRED_SLOTS.get(intent, [])
    return [slot for slot in required if not payload.get(slot)]



class MedicalAgent:
    """
    Simple deterministic agent.
    Decides which action to take based on intent.
    """
    def __init__(self):
        self.pending_email_booking = None
        self.pending_doctor_schedule = None
#------------------------Trigger this if the user input is incomplete----------------------------------
    async def handle(self, intent: str, payload: dict) -> str:
        if payload:
            if "doctor" in payload and "doctor_name" not in payload:
                payload["doctor_name"] = payload.pop("doctor")

            if "date" in payload and payload.get("time"):
                payload["date_time"] = f"{payload['date']}T{payload['time']}"

#------------------------Only use when need to book appoinments-----------------------------------------
        if intent == "book_appointment":
            

            if not payload.get("doctor_name"):
                return "Which doctor would you like to book an appointment with ?"

            if not payload.get("date_time"):
                return "Please tell me the exact date and time for the appointment."

            

            result = await book_appointment_core(
                patient=payload.get("patient", "Unknown"),
                doctor_name=payload["doctor_name"],
                date_time=payload["date_time"],
                notes=payload.get("notes", "")
            )
            if result.startswith("Appointment booked successfully"):
                self.pending_email_booking = {
                    "message" : result
                }

                return (
                    f"{result}\n\n"
                    "Please provide your email id to receive the appoinment confirmation. Make sure you just entering the exact email id"
                )
            return result
        



#-----------------------Use only when query is regarding the doctor's availbility-------------------
        elif intent == "check_availability":
            return await get_doctor_availability_core(
                doctor_name=payload["doctor_name"],
                day=payload["day"]
            )
        






#-------------------------Use only when doctor wants to know about the daily schedule----------------
        elif intent == "daily_schedule":

            if not payload.get("doctor_name"):
                return "Can you please mention the doctor's name ?"
            
            if not payload.get("day"):
                return "Can you please mention the exact date in DD-MM-YYYY format ?"
            

            schedule = await get_doctor_schedule_core(
                doctor_name=payload["doctor_name"],
                day=payload["day"]
            )
            self.pending_doctor_schedule = {
                "doctor_name": payload["doctor_name"],
                "day": payload["day"],
                "schedule": schedule
            }
            return (
                f"{schedule}\n\n"
                "Please provide your email to receive the daily schedule."
            )
        





#----------Use only when question regarding appoinment details from user end----------------------
        elif intent == "appointment_details":
             return await get_appointment_details_core(
                appointment_id=payload["appointment_id"]
            )
#----------------Email service---------------------------------------        

        elif intent == "collect_email":
            
            email = payload["email"]

            if self.pending_email_booking:
                send_booking_email(
                    to_email=email,
                    message=self.pending_email_booking["message"]
                )

                self.pending_email_booking = None
                return "Appointment confirmation email sent !!"
            
            if self.pending_doctor_schedule:
                send_booking_email(
                    to_email=email,
                    message=(
                        f"Schedule for {self.pending_doctor_schedule['doctor_name']}"
                        f"on {self.pending_doctor_schedule['day']}:\n\n"
                        f"{self.pending_doctor_schedule['schedule']}"
                    )
                )
                self.pending_doctor_schedule = None
                return "Doctor Schedule Email sent !!"
            
            return "There is nothing that requires an email"
            
        elif intent == "chat":
            return payload["message"]

        else:
            return (
                "Sorry, I didn't understand your request."
                " Please try again."
                "You can ask me to :\n"
                "- Book an appointment\n"
                "- Check doctor availability\n"
                "- Check daily schedule\n"
                "- Get appointment details\n"
                "How can I assist you today?"
            )


#agent instance
agent = MedicalAgent()



















































































































































































































































