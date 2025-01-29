from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Definição dos Agentes
scrum_master = Agent(
    role='Scrum Master',
    goal='Facilitar a equipe de desenvolvimento, remover impedimentos e garantir a aplicação do Scrum',
    backstory='Você é um Scrum Master experiente que guia o time no uso das práticas ágeis.',
    verbose=False,
    allow_delegation=False,
    max_iter=5,
    llm=ChatOpenAI(model_name='ollama/llama3.1', base_url="http://localhost:11434/v1", api_key="nada", temperature=0.1)
)

product_owner = Agent(
    role='Product Owner',
    goal='Gerenciar o backlog do produto e garantir que as prioridades de negócio sejam atendidas',
    backstory='Você entende profundamente as necessidades do cliente e prioriza funcionalidades.',
    verbose=False,
    allow_delegation=False,
    max_iter=5,
    llm=ChatOpenAI(model_name='ollama/llama3.1', base_url="http://localhost:11434/v1", api_key="nada", temperature=0.1)
)

dev_team = Agent(
    role='Equipe de Desenvolvimento',
    goal='Criar e entregar incrementos funcionais do produto',
    backstory='Vocês são desenvolvedores experientes responsáveis por implementar as funcionalidades do produto.',
    verbose=False,
    allow_delegation=False,
    max_iter=5,
    llm=ChatOpenAI(model_name='ollama/llama3.1', base_url="http://localhost:11434/v1", api_key="nada", temperature=0.1)
)

# Definição das Tarefas
task1 = Task(
    description='Facilitar a reunião diária, remover impedimentos e garantir alinhamento da equipe.',
    agent=scrum_master,
    expected_output='Resumo da Daily Scrum informando os desafios e status das tarefas.'
)

task2 = Task(
    description='Priorizar o backlog e refinar histórias para a próxima Sprint.',
    agent=product_owner,
    expected_output='Lista de histórias refinadas e priorizadas com critérios de aceitação.'
)

task3 = Task(
    description='Desenvolver e entregar uma funcionalidade do backlog.',
    agent=dev_team,
    expected_output='Código funcional revisado e pronto para deployment.'
)

# Criando o Crew (Time Scrum)
scrum_team = Crew(
    agents=[scrum_master, product_owner, dev_team],
    tasks=[task1, task2, task3],
    verbose=True
)

# Executando a Simulação
result = scrum_team.kickoff()
print(result)
