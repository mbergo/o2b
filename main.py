import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()




function_descriptions = [
    {
        "name": "extract_info_from_email",
        "description": "Extract key info from an email, and identify if the email will bring some important information or enact some action from me.",
        "parameters": {
            "type": "object",
            "properties": {
                "sender": {
                    "type": "string",
                    "description": "The sender of the email."
                },                                        
                "summary": {
                    "type": "string",
                    "description": "A brief summary of the email."
                },
                "importance": {
                    "type": "string",
                    "description": "Try to give an importance to this email based on if do I need to know that? Do I need to act upon? Do I need to reply? Do I need to schedule a meeting? etc."
                },
            },
            "required": ["sender", "summary", "importance"]
        }
    }
]

# email = """
# From: John Doe <
# To: Jane Doe <

# Hi Jane,

# I hope you are doing well. I wanted to discuss the issues we are facing with the current setup. The server is down and we are unable to access the files. We need to fix this as soon as possible.

# We also need to plan for the upcoming meeting. We need to discuss the new project and the timeline for completion. We also need to finalize the budget for the project.

# I suggest we improve the communication between the team members. We need to have regular meetings to discuss the progress of the project.

# I think the next step is to schedule a meeting to discuss the issues and plan for the project.

# I would rate this email 8 out of 10 in terms of productivity.

# Best,

# John
# """

class Email(BaseModel):
    from_email: str
    content: str
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse_email(email: Email):
    content = email.content
    query = f"Please extract key information from this email: {content} "

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions = function_descriptions,
        function_call="auto"
    )

    arguments = response.choices[0]["message"]["function_call"]["arguments"]
    sender = eval(arguments).get("sender")
    summary = eval(arguments).get("summary")
    importance = eval(arguments).get("importance")

    return {
        "sender": sender,
        "summary": summary,
        "importance": importance
    }
