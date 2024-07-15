import openai
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

function_descriptions = [
    {
        "name": "extract_meeting_insights",
        "description": "Extract insights from meetings",
        "parameters": {
            "type": "object",
            "properties": {
                "meeting": {
                    "description": "The meeting objectives",
                    "type": "string",
                },
                "agenda": {
                    "description": "The meeting agenda",
                    "type": "string",
                },
                "gaps": {
                    "description": "The meeting gaps, regarding good agile process. For example, lack of prior knowledge, objective not being met, etc.",
                    "type": "string",
                },
                "improvements": {
                    "description": "The meeting improvements, regarding good agile process. What should be improved for a good project management. What should be different for a good timely delivery.",
                    "type": "string",
                },
                "lost_personas": {
                    "description": "The meeting lost personas, regarding good agile process. Who appeared to be more lost in the context of the meeting.",
                    "type": "string",
                },
            },
            "required": ["meeting", "agenda", "gaps", "improvements", "lost_personas"],
        },
    }
]

class Email(BaseModel):
    from_email: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse(email: Email):
    content = email.content
    query = f"Please extract insights from this meeting {content}"

    messages = [{
        "role": "user",
        "content": query
    }]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions=function_descriptions,
        function_call={"name": "extract_meeting_insights"}
    )

    function_call = response.choices[0].message.function_call
    arguments = json.loads(function_call.arguments)

    meeting = arguments.get("meeting")
    agenda = arguments.get("agenda")
    gaps = arguments.get("gaps")
    improvements = arguments.get("improvements")
    lost_personas = arguments.get("lost_personas")

    return {
        "meeting": meeting,
        "agenda": agenda,
        "gaps": gaps,
        "improvements": improvements,
        "lost_personas": lost_personas
    }
