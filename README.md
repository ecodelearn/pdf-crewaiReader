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
Executando a Aplicação
Certifique-se de que você está no diretório do projeto e que o ambiente virtual está ativado.

Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```
Abra seu navegador e acesse http://localhost:8501 para visualizar a aplicação.

Estrutura do Projeto
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
Descrição dos Arquivos

app.py: Arquivo principal que inicia a aplicação Streamlit.
controllers/main_controller.py: Controlador principal que executa a análise dos PDFs.
models/agent.py: Define os agentes utilizados na análise.
models/crew.py: Define a crew de agentes.
models/task.py: Define as tarefas dos agentes.
utils/config.py: Configurações e parâmetros da aplicação.
utils/config_llm.py: Configuração do modelo LLM.
utils/pdf_search_tool.py: Ferramenta de busca em PDFs.

Funcionamento
A aplicação permite configurar o caminho para a pasta contendo os PDFs a serem analisados e executar a análise. O resultado da análise é exibido na interface do Streamlit e também pode ser baixado como um arquivo YAML.

Problemas Comuns
Erro de Importação
Se você encontrar um erro de importação, verifique se todas as dependências estão corretamente instaladas e se o ambiente virtual está ativado.

Erro ao Processar Resultados
Se ocorrer um erro ao processar os resultados, verifique os logs para mais detalhes e certifique-se de que os PDFs estão no formato correto.

Contato
Para quaisquer dúvidas ou problemas, sinta-se à vontade para abrir uma issue no repositório ou enviar um email para ecodelearn@outlook.com
