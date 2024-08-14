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
        "description": "Extrair informações do email para tirar dados e formular insights.",
        "parameters": {
            "type": "object",
            "properties": {
                "Participantes": {
                    "type": "string",
                    "description": "Nome dos Participantes da reunião."
                },
                "AssuntoDaReuniao": {
                    "type": "string",
                    "description": "Uma breve descrição do tópico principal discutido."
                },
                "ProblemasIdentificados": {
                    "type": "string",
                    "description": "Lista dos problemas, gaps ou necessidades expressadas na reunião."
                },
                "Solucoes": {
                    "type": "string",
                    "description": "Soluções sugeridas para cada item identificado identificado."
                },
                "Acordados": {
                    "type": "string",
                    "description": "Principais acordos ou tarefas definidas durante a reunião."
                },
                "AcoesPendentes": {
                    "type": "string",
                    "description": "Ações que possam ser extraidas dentro do que foi descutido no formato: <pessoa>:<ação>."
                },
                "FeedbackDoCliente": {
                    "type": "string",
                    "description": "Comentários e feedback do cliente sobre a reunião e os tópicos discutidos."
                },
                "Follow-upNecessario": {
                    "type": "string",
                    "description": "Pontos que precisam de acompanhamento; cite as etapas."
                },
                "RecursosNecessarios": {
                    "type": "string",
                    "description": "Recursos adicionais que serão necessários para resolver os problemas ou completar as tarefas. Pode ser um processo novo, ajuste de processo, reorganização, etc..."
                },
                "PontosDeAtencao": {
                    "type": "string",
                    "description": "Deduza questoes que precisam de atenção especial no presente e/ou podem se tornar problemas no futuro."
                },
            },
            "required": [
                "Participantes",
                "AssuntoDaReuniao",
                "ProblemasIdentificados",
                "Solucoes",
                "Acordados",
                "AcoesPendentes",
                "FeedbackDoCliente",
                "Follow-upNecessario",
                "RecursosNecessarios",
                "PontosDeAtencao"
            ]
        }
    }
]

class Email(BaseModel):
    from_email: str
    content: str
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse_email(email: Email):
    """
    Analyzes an email and extracts relevant information using OpenAI's GPT-4 model.

    Args:
        email (Email): The email to be analyzed.

    Returns:
        dict: A dictionary containing the extracted information from the email. The keys are:
            - "From" (str): The sender of the email.
            - "AssuntoDaReuniao" (str): The subject of the meeting mentioned in the email.
            - "ProblemasIdentificados" (str): The identified problems mentioned in the email.
            - "SoluçõesPropostas" (str): The proposed solutions mentioned in the email.
            - "TarefasAtribuídas" (str): The assigned tasks mentioned in the email.
            - "DecisõesTomadas" (str): The taken decisions mentioned in the email.
            - "AçõesPendentes" (str): The pending actions mentioned in the email.
            - "FeedbackDoCliente" (str): The client feedback mentioned in the email.
            - "FollowUpNecessario" (bool): Whether a follow-up is necessary mentioned in the email.
            - "RecursosNecessarios" (str): The necessary resources mentioned in the email.
            - "PontosDeAtençao" (str): The points of attention mentioned in the email.
            - "DataDaProximaReuniao" (str): The date of the next meeting mentioned in the email.
            - "Participantes" (str): The participants mentioned in the email.
            - "DocumentosAnexados" (str): The attached documents mentioned in the email.
            - "Status" (str): The status mentioned in the email.
            - "NotasAdicionais" (str): Additional notes mentioned in the email.
            - "Processos" (str): The processes mentioned in the email.
            - "Educacao" (str): The education mentioned in the email.
            - "Personalidade" (str): The personality mentioned in the email.

    Raises:
        None
    """
    content = email.content
    query = f"Por favor, extraia as informaçoes do texto: {content} "

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions = function_descriptions,
        function_call="auto"
    )

    arguments = response.choices[0]["message"]["function_call"]["arguments"]
    participantes = eval(arguments).get("Participantes")
    assunto_da_reuniao = eval(arguments).get("AssuntoDaReuniao")
    problemas_identificados = eval(arguments).get("ProblemasIdentificados")
    solucoes = eval(arguments).get("Solucoes")
    acordados = eval(arguments).get("Acordados")
    acoes_pendentes = eval(arguments).get("AcoesPendentes")
    feedback_do_cliente = eval(arguments).get("FeedbackDoCliente")
    follow_up_necessario = eval(arguments).get("Follow-upNecessario")
    recursos_necessarios = eval(arguments).get("RecursosNecessarios")
    pontos_de_atencao = eval(arguments).get("PontosDeAtencao")


    return {
        "Participantes": participantes,
        "AssuntoDaReuniao": assunto_da_reuniao,
        "ProblemasIdentificados": problemas_identificados,
        "Solucoes": solucoes,
        "Acordados": acordados,
        "AcoesPendentes": acoes_pendentes,
        "FeedbackDoCliente": feedback_do_cliente,
        "Follow-upNecessario": follow_up_necessario,
        "RecursosNecessarios": recursos_necessarios,
        "PontosDeAtencao": pontos_de_atencao
    }
