import requests
import json

print(
    requests.post(
        "https://o2b.onrender.com/",
        json={
            "from_email": "John@o2b.com.br",
            "content": """
            Hi Jane, I hope you are doing well. 
            I wanted to discuss the issues we are facing with the current setup. 
            The server is down and we are unable to access the files. 
            We need to fix this as soon as possible. We also need to plan for the upcoming meeting. 
            We need to discuss the new project and the timeline for completion. 
            We also need to finalize the budget for the project. 
            I suggest we improve the communication between the team members. 
            We need to have regular meetings to discuss the progress of the project. 
            I think the next step is to schedule a meeting to discuss the issues and plan for the project. 
            I would rate this email 8 out of 10 in terms of productivity. 
            
            Best, John
            """                
        }
    ).json()
)