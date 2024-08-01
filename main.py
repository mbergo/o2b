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
        "description": "Extrair informações de email de modo a poder sugerir melhorias e outros quesitos.",
        "parameters": {
            "type": "object",
            "properties": {
                "From": {
                    "type": "string",
                    "description": "Nome do remetente."
                },
                "AssuntoDaReuniao": {
                    "type": "string",
                    "description": "Uma breve descrição do tópico principal discutido."
                },
                "ProblemasIdentificados": {
                    "type": "string",
                    "description": "Lista dos problemas discutidos e detalhamento dos mesmos."
                },
                "SolucoesPropostas": {
                    "type": "string",
                    "description": "Soluções sugeridas para cada problema identificado."
                },
                "TarefasAtribuidas": {
                    "type": "string",
                    "description": "Tarefas que foram delegadas, incluindo quem é responsável e o prazo para conclusão de cada tarefa."
                },
                "DecisoesTomadas": {
                    "type": "string",
                    "description": "Principais decisões inferidas baseadas na conversação durante a reunião."
                },
                "AcoesPendentes": {
                    "type": "string",
                    "description": "Ações que ainda precisam ser concluídas e quem está responsável por elas."
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
                "DataDaProximaReuniao": {
                    "type": "string",
                    "description": "Agendamento da proxima reunião, se tiver sido mencionado."
                },
                "Participantes": {
                    "type": "string",
                    "description": "Nome dos participantes da reunião."
                },
                "DocumentosAnexados": {
                    "type": "string",
                    "description": "Documentos anexados ou mencionados."
                },
                "Status": {
                    "type": "string",
                    "description": "Status atual do projeto, se possível inferir baseado na assertividade da conversa."
                },
                "NotasAdicionais": {
                    "type": "string",
                    "description": "Qualquer informação adicional relevante que não se enquadre em outros itens."
                },
                "Processos": {
                    "type": "string",
                    "description": "Alguma mudança ou criação de processo dentro da empresa? Caso sim, explique."
                },
                "Educacao": {
                    "type": "string",
                    "description": "Qual o participante que menos se manteve no contexto técnico, falava de forma abritária e interrompia mais?"
                },
                "Personalidade": {
                    "type": "string",
                    "description": "Dê um adjetivo para a personalidade de cada participante, considerando o contexto, o que foi falado, a forma de falar, os momentos, etc e a maneira de ser falado."
                }
            },
            "required": [
                "From",
                "AssuntoDaReuniao",
                "ProblemasIdentificados",
                "SoluçoesPropostas",
                "TarefasAtribuidas",
                "DecisoesTomadas",
                "AçoesPendentes",
                "FeedbackDoCliente",
                "Follow-upNecessario",
                "RecursosNecessarios",
                "PontosDeAtencao",
                "DataDaProximaReuniao",
                "Participantes",
                "DocumentosAnexados",
                "Status",
                "NotasAdicionais",
                "Processos",
                "Educacao",
                "Personalidade"
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
    query = f"Por favor, extraia as informaçoes do email: {content} "

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions = function_descriptions,
        function_call="auto"
    )

    arguments = response.choices[0]["message"]["function_call"]["arguments"]
    clientName = eval(arguments).get("clientName")
    From = eval(arguments).get("From")
    AssuntoDaReuniao = eval(arguments).get("AssuntoDaReuniao")
    ProblemasIdentificados = eval(arguments).get("ProblemasIdentificados")
    SolucoesPropostas = eval(arguments).get("SolucoesPropostas")
    TarefasAtribuidas = eval(arguments).get("TarefasAtribuidas")
    DecisoesTomadas = eval(arguments).get("DecisoesTomadas")
    AcoesPendentes = eval(arguments).get("AcoesPendentes")
    FeedbackDoCliente = eval(arguments).get("FeedbackDoCliente")
    FollowUpNecessario = eval(arguments).get("FollowUpNecessario")
    RecursosNecessarios = eval(arguments).get("RecursosNecessarios")
    PontosDeAtençao = eval(arguments).get("PontosDeAtençao")
    DataDaProximaReuniao = eval(arguments).get("DataDaProximaReuniao")
    Participantes = eval(arguments).get("Participantes")
    DocumentosAnexados = eval(arguments).get("DocumentosAnexados")
    Status = eval(arguments).get("Status")
    NotasAdicionais = eval(arguments).get("NotasAdicionais")
    Processos = eval(arguments).get("Processos")
    Educacao = eval(arguments).get("Educacao")
    Personalidade = eval(arguments).get("Personalidade")


    return {
        "From": From,
        "AssuntoDaReuniao": AssuntoDaReuniao,
        "ProblemasIdentificados": ProblemasIdentificados,
        "SolucoesPropostas": SolucoesPropostas,
        "TarefasAtribuidas": TarefasAtribuidas,
        "DecisoesTomadas": DecisoesTomadas,
        "AcoesPendentes": AcoesPendentes,
        "FeedbackDoCliente": FeedbackDoCliente,
        "FollowUpNecessario": FollowUpNecessario,
        "RecursosNecessarios": RecursosNecessarios,
        "PontosDeAtençao": PontosDeAtençao,
        "DataDaProximaReuniao": DataDaProximaReuniao,
        "Participantes": Participantes,
        "DocumentosAnexados": DocumentosAnexados,
        "Status": Status,
        "NotasAdicionais": NotasAdicionais,
        "Processos": Processos,
        "Educacao": Educacao,
        "Personalidade": Personalidade
    }
