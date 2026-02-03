import os
import json
from anthropic import Anthropic
from llm_router import choose_prompt
from dotenv import load_dotenv



load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

MODEL = "claude-sonnet-4-20250514"


def extract_intent_and_payload(user_input: str) -> dict:
    prompt_template = choose_prompt(user_input)
    prompt = prompt_template.format(user_input=user_input)

    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        temperature=0,
        system=(
            
                "You are a medical assistant and strict JSON generator.\n\n"
                "IMPORTANT NORMALIZATION RULES:\n"
                "- Doctor names must be returned in proper title case.\n"
                "- Always prefix doctor names with 'Dr.' (capital D, lowercase r, dot).\n"
                "- If user writes 'dr', 'doctor', or omits punctuation, normalize it to 'Dr.'.\n"
                "- Example: 'dr ahuja', 'doctor ahuja', 'Ahuja' → 'Dr. Ahuja'.\n\n"
                "If the user input is ambiguous or missing information, make your best guess based on context.\n\n" \
                "If the user just says he or she want want to book and appoinment but does not provide details then ask for that specific details and then pass that to agent not before that.\n\n"
                "-Example : User: I want to book an appointment with Dr. Sharma next Monday -> ask for the specific date and time.\n"
                "Return ONLY valid JSON. No explanation. No markdown."
        ),


        
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    content = response.content[0].text.strip()

    #print("DEBUG : Raw Claude response:")
    #print(content)

    try:
        data = json.loads(content)

        if not isinstance(data, dict):
            raise ValueError("Claude response is not a JSON object")
        
        if "intent" not in data:
            raise ValueError("Claude response missing 'intent field")
        
        if "payload" not in data or not isinstance(data["payload"], dict):
            data["payload"] = {}

        return data
    
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from Claude:\n{content}")
