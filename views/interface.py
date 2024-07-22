import streamlit as st
from controllers.main_controller import execute_analysis
import yaml

def run_app():
    st.set_page_config(layout="wide")

    st.sidebar.title("Configurações")
    pdf_folder = st.sidebar.text_input("Caminho da pasta contendo os PDFs:", "PDFs")

    if st.sidebar.button("Executar Análise"):
        with st.spinner("Executando análise..."):
            try:
                file_name, final_output = execute_analysis(pdf_folder)
                
                if not file_name or not final_output:
                    st.error("Erro ao processar a análise. Verifique os logs para mais detalhes.")
                    return

                st.success(f"Dados salvos em {file_name}")
                with open(file_name, 'r') as file:
                    st.download_button("Download YAML", data=file.read(), file_name=file_name)

                st.subheader("Resultado da Análise")
                for artigo in final_output['artigos']:
                    st.write("---")
                    artigo_data = artigo.get('ARTIGO', {})
                    if isinstance(artigo_data, list):
                        for entry in artigo_data:
                            for key, value in entry.items():
                                if key == 'TÍTULO':
                                    st.markdown(f"### {key}: {value}")
                                else:
                                    st.markdown(f"**{key}:** {value}")
                    else:
                        for key, value in artigo_data.items():
                            if key == 'TÍTULO':
                                st.markdown(f"### {key}: {value}")
                            else:
                                st.markdown(f"**{key}:** {value}")

            except FileNotFoundError as e:
                st.error(f"Erro: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    run_app()
