
from fastmcp import FastMCP
from core import book_appointment_core, get_doctor_availability_core, get_doctor_schedule_core, get_appointment_details_core
from datetime import date
mcp = FastMCP("Doctor Appointment MCP")


#----------------------- BOOK APPOINTMENT TOOL ----------------
@mcp.tool()
async def book_appointment(
    patient: str,
    doctor_name: str,
    date_time: str,
    notes: str = ""
) -> str:
    return await book_appointment_core(
        patient, doctor_name, date_time, notes
    )



#----------------------- GET DOCTOR AVAILABILITY TOOL ----------------

@mcp.tool()
async def get_doctor_availability(
    doctor_name: str,
    day: str
) -> str:
    """
    Check doctor's availability on a given date.
    day format: YYYY-MM-DD
    """
    parsed_day = date.fromisoformat(day)

    return await get_doctor_availability_core(
        doctor_name=doctor_name,
        day=parsed_day
    )


#----------------------------Doctor Daily schedule Tool-----------------------

@mcp.tool()
async def get_doctor_daily_schedule(
    doctor_name: str,
    day: str
) -> str:
    """
    Get full schedule of a doctor for a given day.
    day format: YYYY-MM-DD
    """
    parsed_day = date.fromisoformat(day)

    return await get_doctor_schedule_core(
        doctor_name=doctor_name,
        day=parsed_day
    )


#----------------------------Appointment Details Tool-----------------------


@mcp.tool()
async def get_appointment_details(
    appointment_id: int
) -> str:
    """
    Retrieve appointment details using appointment ID.
    """
    return await get_appointment_details_core(
        appointment_id=appointment_id
    )





















































