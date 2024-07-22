solicitacoes = """
<solicitacoes>
1 - TÍTULO - Nas primeiras palavras do PDF, o Título normalmente vem em uma frase com palavras onde cada palavra tem inicio com caixa Alta. É bem provável ser a primeira frase do PDF.  Se precisar leia o artigo todo e veja se consegue uma referencia com o nome do artigo ou busque na web referencia para extrair o Título.
2 - OBJETIVOS - Identificação dos Objetivos: Realize uma análise cuidadosa do conteúdo do trabalho para extrair os objetivos principais. Resuma esses objetivos em um parágrafo claro e conciso, capturando a essência das metas e intenções do estudo.
3 - GAP - Identificação do GAP: Analise o conteúdo do trabalho para identificar o GAP científico que ele aborda, mesmo que não esteja explicitamente mencionado. Formule um parágrafo conciso, focando em destacar a questão central que o estudo procura resolver ou elucidar.
4 - METODOLOGIA - Extração Detalhada da Metodologia do Trabalho: Identificação e Descrição da Metodologia: Proceda com uma análise minuciosa do trabalho para identificar a metodologia utilizada. Detalhe cada aspecto da metodologia, incluindo o desenho do estudo, as técnicas e ferramentas empregadas, os procedimentos de coleta e análise de dados, os passos do método e quaisquer metodologias específicas ou inovadoras adotadas. Formule uma descrição compreensiva em texto corrido, limitando-se a um máximo de 250 palavras para manter a concisão sem sacrificar detalhes importantes.
5 - DATASET - Identifique os datasets usados no trabalho. Descreva-os brevemente em texto corrido, limitando-se a 40 palavras. Quero somente o nome dos dataset na mesma linha e separados por vírgula. Se o dataset foi criado pelos autores escreve "OWN DATASET"
6 - RESULTADOS - Escreva em um parágrafo os resultados obtidos no estudo dando ênfase a dados quantitativos, quero dados numéricos explicitamente. Nesse parágrafo também dê ênfase à comparação ao melhor trabalho anterior em relação ao trabalho proposto. Não use superlativos. Deixe o tom neutro e científico.
7 - LIMITAÇÕES - Produza um texto parafraseado das limitações do trabalho.
8 - CONCLUSÃO - Resuma as conclusões dos autores em relação ao trabalho.
9 - FUTURO - Extraia as Recomendações para Pesquisa Futura: Aponte recomendações para futuras investigações baseadas nas conclusões do artigo.
10 - AVALIAÇÃO - Faça uma avaliação crítica ao trabalho. Não seja generalista faça uma crítica aprofundada.
</solicitacoes>
"""

controles = """
<controle>
NÍVEIS DE CONTROLE:
1. Entonação:Formal Científico.
2. Foco de Tópico: Você deve responder sempre com alto foco no texto do artigo científico.
3. Língua: Responda sempre em Português do Brasil como os Brasileiros costumam escrever textos científicos aderindo aos padrões de redação científica do país a não ser o que será especificado para não traduzir.
4. Controle de Sentimento: Neutro e científico. Evite superlativos como: inovador, revolucionário etc.
5. Nível Originalidade: 10, onde 1 é pouco original e 10 é muito original. Em hipótese alguma copie frases do texto original.
6. Nível de Abstração: 1, onde 1 é muito concreto e real e 10 é muito abstrato e irreal.
7. Tempo Verbal: Escreva no passado.
</controle>
"""

restricoes = """
<restricoes>
O QUE NÃO DEVE SER TRADUZIDO DO INGLÊS PARA PORTUGUÊS:
1. Termos técnicos em inglês amplamente aceitos e usados nos textos em português.
2. Nome de algoritmos de machine learning.
3. Métricas usadas no trabalho.
4. Nome dos datasets.
5. Não envolva o retorno do YAML com ```yaml.
6. Não coloque ``` nem ``` no texto de retorno.
</restricoes>
"""

template = """
<template>
ARTIGO:
  - TÍTULO: "Título do artigo"
  - ARQUIVO: "nome do arquivo.pdf"
  - OBJETIVOS: "Objetivo geral e específicos"
  - GAP: "Gap científico"
  - METODOLOGIA: "Metodologia"
  - DATASET: "Datasets utilizados"
  - RESULTADOS: "Resultados do artigo"
  - LIMITAÇÕES: "Limitações do artigo científico"
  - CONCLUSÃO: "Conclusões"
  - AVALIAÇÃO: "Análise do artigo"
</template>
"""

