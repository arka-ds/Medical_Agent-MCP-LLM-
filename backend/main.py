#------------------------------------------------------Run the Medical Agent----------------------------------------------------------------------
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio
from backend.agent import agent
from llm_parser import extract_intent_and_payload

async def main():
    print("Medical Assistant started. Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        parsed = extract_intent_and_payload(user_input)

        #print("\nDEBUG: Parsed intent and payload:")
        #print(parsed)

        result = await agent.handle(
            parsed["intent"],
            parsed["payload"]
        )

        print("\nAgent:", result)
        print("-" * 100)
        print("-" * 100)

if __name__ == "__main__":
    asyncio.run(main())
































