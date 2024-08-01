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
                "Assunto da Reunião": {
                    "type": "string",   
                    "description": "Uma breve descrição do tópico principal discutido."
                },
                "Problemas Identificados": {
                    "type": "string",
                    "description": "Interprete com o que foi conversado entre os participantes os problemas identificados e detalhamento dos mesmos."
                },
                "Soluções Propostas": {
                    "type": "string",
                    "description": "Soluções sugeridas para cada problema identificado."
                },
                "Tarefas Atribuídas": {
                    "type": "string",
                    "description": "Tarefas que foram delegadas, incluindo quem é responsável e o prazo para conclusão."
                },
                "Decisões Tomadas": {
                    "type": "string",
                    "description": "Principais decisões feitas durante a reunião."
                },
                "Ações Pendentes": {
                    "type": "string",
                    "description": "Ações que ainda precisam ser concluídas e quem está responsável por elas."
                },
                "Feedback do Cliente": {
                    "type": "string",
                    "description": "Comentários e feedback do cliente sobre a reunião e os tópicos discutidos."
                },
                "Follow-up Necessario": {
                    "type": "string",
                    "description": "Pontos que precisam de acompanhamento e provém de etapas."
                },
                "Recursos Necessarios": {
                    "type": "string",
                    "description": "Recursos adicionais que serão necessários para resolver os problemas ou completar as tarefas."
                },
                "Pontos de Atencao": {
                    "type": "string",
                    "description": "Deduza questoes que precisam de atenção especial no presente e/ou podem se tornar problemas no futuro."
                },
                "Data da Proxima Reuniao": {
                    "type": "string",
                    "description": "Agendamento da último reunião, se tiver sido mencionado."
                },
                "Participantes": {
                    "type": "string",
                    "description": "Nome dos participantes."
                },
                "Documentos Anexados": {
                    "type": "string",
                    "description": "Documentos anexados ou mencionados."
                },
                "Status": {
                    "type": "string",
                    "description": "Status atual do projeto, se possível inferir."
                },
                "Notas Adicionais": {
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
                    "description": "Dê um adjetivo para cada participante acerca de sua personalidade, combine todo o contexto, o que foi falado, os momentos, etc e de uma opinão?"
                }
            },
            "required": [ 
                "From", "Assunto da Reunião", "Problemas Identificados", "Soluções Propostas", "Tarefas Atribuídas", "Decisões Tomadas", "Ações Pendentes", "Feedback do Cliente", "Follow-up Necessario", "Recursos Necessarios", "Pontos de Atencao", "Data da Proxima Reuniao", "Participantes", "Documentos Anexados", "Status", "Notas Adicionais", "Processos", "Educacao", "Personalidade"   
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
    content = email.content
    query = f"Por favor, extraia as informações do email: {content} "

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions = function_descriptions,
        function_call="auto"
    )

    arguments = response.choices[0]["message"]["function_call"]["arguments"]
<<<<<<< HEAD
    clientName = eval(arguments).get("clientName")
    From = eval(arguments).get("From")
    AssuntoDaReunião = eval(arguments).get("AssuntoDaReunião")
    ProblemasIdentificados = eval(arguments).get("ProblemasIdentificados")
    SoluçõesPropostas = eval(arguments).get("SoluçõesPropostas")
    TarefasAtribuídas = eval(arguments).get("TarefasAtribuídas")
    DecisõesTomadas = eval(arguments).get("DecisõesTomadas")
    AçõesPendentes = eval(arguments).get("AçõesPendentes")
    FeedbackDoCliente = eval(arguments).get("FeedbackDoCliente")
    FollowUpNecessario = eval(arguments).get("FollowUpNecessario")
    RecursosNecessarios = eval(arguments).get("RecursosNecessarios")
    PontosDeAtenção = eval(arguments).get("PontosDeAtenção")
    DataDaProximaReunião = eval(arguments).get("DataDaProximaReunião")
    Participantes = eval(arguments).get("Participantes")
    DocumentosAnexados = eval(arguments).get("DocumentosAnexados")
    Status = eval(arguments).get("Status")
    NotasAdicionais = eval(arguments).get("NotasAdicionais")
    Processos = eval(arguments).get("Processos")
    Educacao = eval(arguments).get("Educacao")
    Personalidade = eval(arguments).get("Personalidade")


    return {
        "From": From,
        "AssuntoDaReunião": AssuntoDaReunião,
        "ProblemasIdentificados": ProblemasIdentificados,
        "SoluçõesPropostas": SoluçõesPropostas,
        "TarefasAtribuídas": TarefasAtribuídas,
        "DecisõesTomadas": DecisõesTomadas,
        "AçõesPendentes": AçõesPendentes,
        "FeedbackDoCliente": FeedbackDoCliente,
        "FollowUpNecessario": FollowUpNecessario,
        "RecursosNecessarios": RecursosNecessarios,
        "PontosDeAtenção": PontosDeAtenção,
        "DataDaProximaReunião": DataDaProximaReunião,
        "Participantes": Participantes,
        "DocumentosAnexados": DocumentosAnexados,
        "Status": Status,
        "NotasAdicionais": NotasAdicionais,
        "Processos": Processos,
        "Educacao": Educacao,
        "Personalidade": Personalidade
=======
    sender = eval(arguments).get("sender")
    summary = eval(arguments).get("summary")
    importance = eval(arguments).get("importance")

    return {
        "sender": sender,
        "summary": summary,
        "importance": importance
>>>>>>> 9501921 (Using to read emails)
    }
