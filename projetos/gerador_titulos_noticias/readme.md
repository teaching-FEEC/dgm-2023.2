# `Gerador de títulos de notícias do mercado financeiro`
# `Stock market news headlines generator`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Especialização|
|--|--|--|
| Mário Mitsuo Akita  | 082246  | Ciência da Computação/Tecnologia|
| Victor Gomes Moreno   | 272318  | Eng. de Computação|


## Descrição Resumida do Projeto
O objetivo do projeto é gerar títulos de notícias com vieses positivos e negativos para posterior utilização
em projetos de Processamento de Linguagem Natural (PLN) no escopo de análise de sentimentos aplicada ao 
mercado financeiro.

A ideia é prover uma base de dados que possibilite a comparação de diferentes arquiteturas e abordagens para
problemas relacionados à análise de sentimentos de maneira mais padronizada e normalizada, eliminando o esforço
e custo da coleta de grandes quantidades de dados em API de notícias ou redes sociais, ou ainda a contrução de
scapers de dados.

Como resultado, o objetivo é ter uma coleção de títulos de notícias gerados sinteticamente que possam ser úteis
em tarefas de aprendizado de máquina na área de Análise de Sentimentos.

**Vídeo descritivo:** [Vídeo](https://drive.google.com/drive/folders/1iUkC0U0VpS7tMlUG3911w4Mu8GstKf0A?usp=sharing)

## Metodologia Proposta

O desenvolvimento do projeto se dará através de base de dados disponível em: https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/GFJHFK
A partir daí, a ideia do projeto é treinar modelos gerativos pré-treinados (T-PTLMs) ou outros modelos
que apresentem desempenho equivalente ao estado da arte para obterem o vocabulário específico da área
e gerarem textos de melhor qualidade.

As bases serão, então, submetida a várias métricas de desempenho e qualidade a serem especificadas
conforme o avançar dos trabalhos sendo possíveis atividades a classificação dos títulos gerados em positivos e negativos,
utilização de modelos de machine learning para prever cotações de ações baseado nas notícias reais e sintéticas e
análise qualitativa dos títulos gerados.

A expectativa é que sejam gerados dados utilizáveis em uma ampla gama de tarefas da área de PLN em mercado de ações.

## Cronograma
|Etapa  | 09-S2 | 09-S3 | 09-S4 | 10-S1 | 10-S2 | 10-S3 | 10-S4 | 11-S1 | 11-S2 | 11-S3 | 11-S4 |
|--|--|--|--|--|--|--|--|--|--|--|--|
| Estudo de modelos pré-treinados | X | X | | | | | | | | | |
| Treinamento de modelos e geração dos primeiros resultados |  |  | X | X | X | | | | | | |
| **Entrega 2** | | | | | | **X** | | | | | |
| Estudo de métricas quantitativas e qualitativas para avaliação de dados gerados | | | | | | X | X | | | |
| Retreinamentos e fine tuning dos modelos | | | | | | | | X | X | | |
| Reavaliação dos novos dados gerados e conclusões | | | | | | | | | X | X | |
| **Entrega 3** | | | | | | | | | | | **X** |


## Referências Bibliográficas
Touseef Iqbal, Shaima Qureshi. The survey: Text generation models in deep learning. In: Journal of King Saud University - Computer and Information Sciences, Volume 34, Issue 6, Part A. 2022. Pages 2515-2528. ISSN 1319-1578. https://doi.org/10.1016/j.jksuci.2020.04.001. Disponível em: https://www.sciencedirect.com/science/article/pii/S1319157820303360

Katikapalli Subramanyam Kalyan and Ajit Rajasekharan and Sivanesan Sangeetha.AMMUS : A Survey of Transformer-based Pretrained Models in Natural Language Processing. 2021. Disponível em: https://arxiv.org/abs/2108.05542

CAROSIA, Arthur Emanuel de Oliveira. Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações. 2022. 1 recurso online (129 p.) Tese (doutorado) - Universidade Estadual de Campinas, Faculdade de Tecnologia, Limeira, SP.
