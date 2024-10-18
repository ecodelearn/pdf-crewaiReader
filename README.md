# Escolha o Idioma | Choose the Language

- [Português](#análise-de-pdfs-com-streamlit-e-crewai)
- [English](#pdf-analysis-with-streamlit-and-crewai)

---

# Análise de PDFs com Streamlit e CrewAI

Este projeto é uma aplicação Streamlit que analisa arquivos PDF e gera um resumo em formato YAML. Utiliza a biblioteca CrewAI para orquestrar agentes de leitura e revisão.

## Créditos

O prompt inicial foi extraído de um vídeo do [Canal Sandeco no YouTube](https://www.youtube.com/@canalsandeco).

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Ambiente virtual (virtualenv ou venv)

## Configuração do Ambiente

Clone o repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

Crie e ative um ambiente virtual:

Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

MacOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configuração das Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e adicione suas chaves de API e outras variáveis de ambiente necessárias:
```bash
# Configuração das chaves de API (substitua com suas chaves reais)
OPENAI_API_KEY=your_openai_api_key
```

## Executando a Aplicação
Certifique-se de que você está no diretório do projeto e que o ambiente virtual está ativado.

Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

Abra seu navegador e acesse http://localhost:8501 para visualizar a aplicação.

## Estrutura do Projeto
```bash
├── app.py
├── controllers
│   └── main_controller.py
├── models
│   ├── agent.py
│   ├── crew.py
│   └── task.py
├── utils
│   ├── config.py
│   ├── config_llm.py
│   └── pdf_search_tool.py
├── .env
├── requirements.txt
└── README.md
```

### Descrição dos Arquivos

- **app.py**: Arquivo principal que inicia a aplicação Streamlit.
- **controllers/main_controller.py**: Controlador principal que executa a análise dos PDFs.
- **models/agent.py**: Define os agentes utilizados na análise.
- **models/crew.py**: Define a crew de agentes.
- **models/task.py**: Define as tarefas dos agentes.
- **utils/config.py**: Configurações e parâmetros da aplicação.
- **utils/config_llm.py**: Configuração do modelo LLM.
- **utils/pdf_search_tool.py**: Ferramenta de busca em PDFs.

### Funcionamento
A aplicação permite configurar o caminho para a pasta contendo os PDFs a serem analisados e executar a análise. O resultado da análise é exibido na interface do Streamlit e também pode ser baixado como um arquivo YAML.

### Problemas Comuns
#### Erro de Importação
Se você encontrar um erro de importação, verifique se todas as dependências estão corretamente instaladas e se o ambiente virtual está ativado.

#### Erro ao Processar Resultados
Se ocorrer um erro ao processar os resultados, verifique os logs para mais detalhes e certifique-se de que os PDFs estão no formato correto.

### Contato
Para quaisquer dúvidas ou problemas, sinta-se à vontade para abrir uma issue no repositório ou enviar um email para ecodelearn@outlook.com

---

# PDF Analysis with Streamlit and CrewAI

This project is a Streamlit application that analyzes PDF files and generates a summary in YAML format. It uses the CrewAI library to orchestrate reading and reviewing agents.

## Credits

The initial prompt was extracted from a video by [Canal Sandeco on YouTube](https://www.youtube.com/@canalsandeco).

## Prerequisites

Make sure you have the following tools installed:

- Python 3.8 or higher
- Pip (Python package manager)
- Virtual environment (virtualenv or venv)

## Setting Up the Environment

Clone the repository:

```bash
git clone https://github.com/your_user/your_repo.git
cd your_repo
```

Create and activate a virtual environment:

Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

MacOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables Configuration
Create a .env file in the root of the project and add your API keys and other required environment variables:
```bash
# API Key configuration (replace with your actual keys)
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application
Make sure you are in the project directory and the virtual environment is activated.

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser and go to http://localhost:8501 to view the application.

## Project Structure
```bash
├── app.py
├── controllers
│   └── main_controller.py
├── models
│   ├── agent.py
│   ├── crew.py
│   └── task.py
├── utils
│   ├── config.py
│   ├── config_llm.py
│   └── pdf_search_tool.py
├── .env
├── requirements.txt
└── README.md
```

### File Descriptions

- **app.py**: Main file that launches the Streamlit app.
- **controllers/main_controller.py**: Main controller that handles PDF analysis.
- **models/agent.py**: Defines the agents used in the analysis.
- **models/crew.py**: Defines the agent crew.
- **models/task.py**: Defines the agent tasks.
- **utils/config.py**: Application settings and parameters.
- **utils/config_llm.py**: LLM model configuration.
- **utils/pdf_search_tool.py**: PDF search tool.

### How It Works
The application allows you to set the path to the folder containing the PDFs to be analyzed and run the analysis. The result is displayed on the Streamlit interface and can also be downloaded as a YAML file.

### Common Issues
#### Import Error
If you encounter an import error, check if all dependencies are installed correctly and if the virtual environment is activated.

#### Error Processing Results
If an error occurs when processing the results, check the logs for more details and make sure the PDFs are in the correct format.

### Contact
For any questions or issues, feel free to open an issue in the repository or send an email to ecodelearn@outlook.com
