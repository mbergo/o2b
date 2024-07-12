import openai
import os
from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
app = FastAPI()

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


function_descriptions = [
    {

        "name": "Extract insights from meetings",
        "description": "Extract insights from meetings",
        "parameters": {
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
    }
]
                    
class Meet(BaseModel):
    meeting: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.post("/")
def analyse(meet: Meet):
    content = meet.content
    query = f"Please extract insights from this meeting {content}"
    
    messages = [{
        "role": "user",}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=function_descriptions,
        function_call="auto",
    )
    # return response
    
    arguments = response.choices[0]["message"]["function_call"]["arguments"]
    meeting = eval(arguments).get("meeting")
    agenda = eval(arguments).get("agenda")
    gaps = eval(arguments).get("gaps")
    improvements = eval(arguments).get("improvements")
    lost_personas = eval(arguments).get("lost_personas")
    
    return {"meeting": meeting, "agenda": agenda, "gaps": gaps, "improvements": improvements, "lost_personas": lost_personas}   
