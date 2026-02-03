# core.py
from datetime import datetime, date
from database import SessionLocal, Doctor, Appointment
from sqlalchemy import Date



#--------------------- BOOK APPOINTMENT ----------------
async def book_appointment_core(
    patient: str,
    doctor_name: str,
    date_time: str,
    notes: str = ""
) -> str:
    db = SessionLocal()
    try:
        doctor = db.query(Doctor).filter(Doctor.name == doctor_name).first()
        if not doctor:
            return f"No doctor found with name {doctor_name}"

        appt = Appointment(
            patient_name=patient,
            doctor_name=doctor_name,
            appointment_date=datetime.fromisoformat(date_time),
            notes=notes
        )

        db.add(appt)
        db.commit()
        db.refresh(appt)

        return f"Appointment booked successfully with ID: {appt.id}"
    finally:
        db.close()



# ---------------- CHECK AVAILABILITY ----------------

async def get_doctor_availability_core(
    doctor_name: str,
    day: date
) -> str:
    db = SessionLocal()
    try:
        doctor = db.query(Doctor).filter(Doctor.name == doctor_name).first()
        if not doctor:
            return f"No doctor found with name {doctor_name}"

        appointments = db.query(Appointment).filter(
            Appointment.doctor_name == doctor_name,
            Appointment.appointment_date.cast(date) == day
        ).all()

        if not appointments:
            return f"Dr. {doctor_name} is fully available on {day}"

        times = [a.appointment_date.strftime("%H:%M") for a in appointments]
        return f"Dr. {doctor_name} has appointments at: {', '.join(times)}"
    finally:
        db.close()



# ---------------- Daily Schedule--------------------------

async def get_doctor_schedule_core(
    doctor_name: str,
    day: date
) -> str:
    db = SessionLocal()
    try:
        doctor = db.query(Doctor).filter(Doctor.name == doctor_name).first()
        if not doctor:
            return f"No doctor found with name {doctor_name}"

        appointments = db.query(Appointment).filter(
            Appointment.doctor_name == doctor_name,
            Appointment.appointment_date.cast(Date) == day
        ).all()

        if not appointments:
            return f"Dr. {doctor_name} has no appointments on {day}"

        return "\n".join(
            f"{a.appointment_date.strftime('%H:%M')} - {a.patient_name}"
            for a in appointments
        )
    finally:
        db.close()





# ---------------- Appointment Details --------------------------
async def get_appointment_details_core(
    appointment_id: int
) -> str:
    db = SessionLocal()
    try:
        appt = db.query(Appointment).filter(
            Appointment.id == appointment_id
        ).first()

        if not appt:
            return f"No appointment found with ID {appointment_id}"

        return (
            f"Appointment {appt.id}: "
            f"{appt.patient_name} with Dr. {appt.doctor_name} "
            f"on {appt.appointment_date}"
        )
    finally:
        db.close()

