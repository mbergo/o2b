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
        "description": "Extract key info from an email, such as goals, planning or technical problems or warnings, client name, meeting agenda, summary, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "clientName": {
                    "type": "string",
                    "description": "the name of the client in each context of the email."
                },                                        
                "problems": {
                    "type": "string",
                    "description": "Try to identify any problems with the client's current setup or any technical problems they are facing or about what was planned."
                },
                "agenda":{
                    "type": "string",
                    "description": "Try to identify the the topic that were discussed in the email and a brief summary of each topic."
                },
                "improvements": {
                    "type": "string",
                    "description": "Try to suggest any improvements that could be made to the client's current setup or any technical problems they are facing. Suggest changes in process or technology. Be creative."
                },
                "planningNext":{
                    "type": "string",
                    "description": "What is the suggested next step to avoid those mistakes to happen again."
                },
                "productivity": {
                    "type": "string",
                    "description": "Try to give a productivity score to this email based on how likely this email will leads to a good business opportunity, from 0 to 10; 10 most important"
                },
            },
            "required": ["clientName", "problems", "agenda", "improvements", "planningNext", "productivity"]
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
    clientName = eval(arguments).get("clientName")
    problems = eval(arguments).get("problems")
    agenda = eval(arguments).get("agenda")
    improvements = eval(arguments).get("improvements")
    planningNext = eval(arguments).get("planningNext")
    productivity = eval(arguments).get("productivity")

    return {
        "clientName": clientName,
        "problems": problems,
        "agenda": agenda,
        "improvements": improvements,
        "planningNext": planningNext,
        "productivity": productivity
    }
