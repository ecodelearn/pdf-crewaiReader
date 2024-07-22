from crewai import Task

def leitor_task(agent_leitor, solicitacoes, template):
    return Task(
        description="Leia o PDF e responda em YAML às solicitações definidas em <solicitacoes> "
            "usando o modelo definido em <template>. "
            "{solicitacoes} {template}",
        expected_output="YAML com as respostas às solicitações definidas em "
                        "<solicitacoes>, usando o modelo definido em <template>.",
        agent=agent_leitor
    )

def revisor_task(agent_revisor, solicitacoes, template):
    return Task(
        description=
            "Revise o YAML produzido pelo agente leitor para garantir que ele esteja de acordo com o template definido em <template> "
            "e contenha todas as informações solicitadas em <solicitacoes>. {solicitacoes} {template}",
        expected_output="YAML revisado que esteja de acordo com o template definido em <template> "
        "e contenha todas as informações solicitadas em <solicitacoes>. {solicitacoes} {template}",
        agent=agent_revisor
    )
