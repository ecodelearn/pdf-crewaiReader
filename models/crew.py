from crewai import Crew, Process

def create_crew(agent_leitor, agent_revisor, task_leitor, task_revisor):
    return Crew(
        agents=[agent_leitor, agent_revisor],
        tasks=[task_leitor, task_revisor],
        process=Process.sequential
    )
