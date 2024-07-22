import os
import yaml
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from models.agent import create_agent_leitor, create_agent_revisor
from models.task import leitor_task, revisor_task
from models.crew import create_crew
from utils.pdf_search_tool import PDFSearchTool
from utils.config import solicitacoes, template, restricoes, controles
from utils.config_llm import LLM_MODEL  # Importando o modelo do arquivo de configuração

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def log_message(message, debug=False):
    if debug and not st.session_state.get("debug_mode", False):
        return
    st.write(message)

def execute_analysis(pdf_folder):
    if not os.path.exists(pdf_folder):
        raise FileNotFoundError(f"O diretório especificado não foi encontrado: {pdf_folder}")

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    all_articles = []

    log_message("Iniciando a análise dos PDFs...")

    for pdf_file_name in pdf_files:
        log_message(f"Processando o arquivo: {pdf_file_name}", debug=True)

        # criando a mente dos agentes
        gpt = ChatOpenAI(model=LLM_MODEL)  # Usando o modelo do arquivo de configuração

        pdf = os.path.join(pdf_folder, pdf_file_name)

        pdf_tool = PDFSearchTool(pdf)

        # LEITOR
        log_message("Criando o agente leitor...", debug=True)
        agent_leitor = create_agent_leitor(gpt, pdf_tool, solicitacoes, template, restricoes, controles)
        task_leitor = leitor_task(agent_leitor, solicitacoes, template)

        # REVISOR
        log_message("Criando o agente revisor...", debug=True)
        agent_revisor = create_agent_revisor(gpt, solicitacoes, template)
        task_revisor = revisor_task(agent_revisor, solicitacoes, template)

        crew = create_crew(agent_leitor, agent_revisor, task_leitor, task_revisor)

        ipt = {
            'solicitacoes': solicitacoes,
            'template': template,
            'restricoes': restricoes,
            'controles': controles
        }

        log_message("Iniciando a execução da crew...", debug=True)
        results = crew.kickoff(inputs=ipt)

        # Inspecionar o resultado
        log_message("Estrutura completa do resultado: ", debug=True)
        log_message(str(results.__dict__), debug=True)  # Imprimir a estrutura completa do objeto CrewOutput

        # Ajustar a extração dos dados com base na estrutura inspecionada
        try:
            if hasattr(results, 'tasks_output'):
                for task_output in results.tasks_output:
                    # Verificar se o task_output contém 'raw' com o conteúdo YAML
                    if task_output.output_format == 'raw' and 'ARTIGO:' in task_output.raw:
                        yaml_content = task_output.raw
                        log_message(f"Conteúdo YAML: {yaml_content}", debug=True)

                        # Substituir "nome do arquivo.pdf" pelo nome real do arquivo PDF
                        yaml_content = yaml_content.replace("nome do arquivo.pdf", pdf_file_name)

                        # Remover possíveis caracteres inválidos
                        yaml_content = yaml_content.strip('`')

                        # Verificar se o conteúdo é um YAML válido antes de prosseguir
                        try:
                            article_data = yaml.safe_load(yaml_content)
                            all_articles.append(article_data)
                        except yaml.YAMLError as e:
                            log_message(f"Erro ao carregar YAML: {e}", debug=True)
                    else:
                        log_message(f"Ignorando resultado irrelevante: {task_output.description}", debug=True)
            else:
                log_message(f"Erro: 'tasks_output' não encontrado em CrewOutput: {results}", debug=True)
        except Exception as e:
            log_message(f"Erro ao processar os resultados: {e}")

    # Estrutura final para o arquivo YAML
    final_output = {'artigos': all_articles}

    # Verificar se o conteúdo final é válido antes de salvar
    try:
        yaml.safe_load(yaml.dump(final_output))
    except yaml.YAMLError as e:
        log_message(f"Erro ao validar YAML final: {e}")
        return None, {}

    # Definir o nome do arquivo onde o YAML será salvo
    file_name = 'output.yaml'

    # Salvar o objeto Python em um arquivo YAML
    with open(file_name, 'w') as file:
        yaml.dump(final_output, file, default_flow_style=False, allow_unicode=True)

    log_message("Análise concluída. Dados salvos em output.yaml")
    return file_name, final_output
