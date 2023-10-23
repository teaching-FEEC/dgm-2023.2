# `Gerador de títulos de notícias do mercado financeiro [AKA: Estagiário da Folha]`
# `Stock market news headlines generator`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Especialização|
|--|--|--|
| Mário Mitsuo Akita  | 082246  | Ciência da Computação/Tecnologia|
| Victor Gomes Moreno   | 272318  | Eng. de Computação|


## Abstract
Para tomar decisões de investimento de sucesso no mercado financeiro, é relevante analisar as principais notícias em tempo real. Muitas empresas buscam automatizar essa abordagem utilizando modelos de Análise de Sentimentos baseados em Processamento de Linguagem Natural (PLN) para extrair os vieses das notícias mais recentes. Essas informações alimentam algoritmos de previsão de preços futuros de ações, fundamentando assim a decisão de compra ou venda de ativos financeiros. É crucial, portanto, a utilização de conjuntos de dados que incluem uma ampla variedade de títulos de notícias, bem como a análise de seus sentimentos correspondentes. Entretanto, a disponibilidade de conjuntos de dados padronizados para a análise de sentimentos no contexto do mercado financeiro, especialmente em língua portuguesa, é limitada. Além disso, criar bases de dados reais é uma tarefa custosa devido à necessidade de integração com APIs de redes sociais, agregadores de notícias e desenvolvimento de scrapers para coletar dados em sites especializados.

Este projeto tem como objetivo criar uma base de dados pública em língua portuguesa que contenha títulos de notícias sintéticos, acompanhados da classificação de seu sentimento correspondente. Para alcançar esse fim, utilizaremos técnicas de PLN e análise de sentimentos em texto. Além disso, realizaremos testes quantitativos, qualitativos e de benchmarking da nova base de dados para avaliar sua qualidade. Os resultados serão disponibilizados para comunidade, a fim de colaborar com outros projetos da área. 


**Vídeo descritivo:** [Vídeo](https://youtu.be/eHPE9ebIPyA)

## Motivação
A crescente digitalização e automatização da compra e venda de ativos financeiros diferentes abordagens têm sido desenvolvidas com o intuito de maximizar os ganhos financeiros advindos das estratégias de trocas de ações. Neste contexto, a análise de sentimentos extraídos de textos como postagens em redes sociais ou notícias da seção de economia vêm ganhando destaque ao correlacionar a variação no preços de ativos financeiros com o tom presente nos textos analisados.

O desenvolvimento de modelos computacionais baseado em redes neurais profundas e similares, tem como prerequisito a aquisição de grandes massas de dados para treinamento, atividade que vem sendo dificultada pelo [fechamento de API's antes abertas e gratuitas](https://olhardigital.com.br/2023/06/01/internet-e-redes-sociais/twitter-api-cara-impede-uso-para-pesquisas-academicas/) ou [criação de mecanismos para dificultar a atividade de data scrapping](https://www.adweek.com/media/the-new-york-times-updates-terms-of-service-to-prevent-ai-scraping-its-content/). Neste cenário, a utilização de modelos gerativos passa a fazer sentido de modo a prover uma maior massa de dados para treinamento de modelos preditivos.

Além de prover aumento na quantidade das amostras, o desenvolvimento de datasets para a área pode facilitar a comparação de diferentes abordagens estudadas além de facilitar o desenvolvimento de novos trabalhos na área ao prover um dataset de referência balanceado e padronizado.

## Objetivo

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

### Bases de dados e Evolução
|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|Replication data for: predicting the brazilian stock market using sentiment analysis, technical indicators, and stock prices | [Repositório de dados Unicamp](https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/GFJHFK) | Base de títulos de notícias em língua portuguesa contendo aproximadamente 550 notícias rotuladas e 185 mil notícias não rotuladas para utilização em treinamento de rede neural profunda semisupervisionada utilizada na tese "[Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações](https://repositorio.unicamp.br/Acervo/Detalhe/1247846)".|4

O dataset contém diversos títulos de notícias no formato texto (txt) sem qualquer tipo de formatação. O conjunto contém:
  *  ~187 mil títulos não rotulados
  *  352 notícias classificadas como negativas
  *  296 notícias classificadas como positivas

### Pré-processamento

Para o melhor treinamento dos Modelos Pré-treinado, foram efetuados alguns procedimentos com o objetivo de sanear o conjunto de dados não rotulado:
1. Remoção de duplicatas
2. Remoção de títulos com 3 palavras ou menos
3. Remoção dos títulos meramente descritivos de páginas
  > "Bovespa - Opções - Parte 9".

  > "Fundos: Papéis de Índice Brasil Bovespa".

  > "Fundos: Ações Ibovespa Indexado".
4. Remoção da marcação de data e hora

### Workflow



## Experimentos, Resultados e Discussão dos Resultados


### Resultados preliminares
A seguir, amostra com 30 notícias geradas no treinamento de 17/10/2023.

> * Dólar opera instável nesta sexta, após Fed sinalizar abertura da bolsa
> * Receita abre consulta ao 2º lote de restituições do Imposto de Renda 2017 nesta segunda
> * Moradores de Itu têm que pagar para ver o Carnaval; confira como participar
> * No Rio, banco de sangue do Hospital-SP recebe doação de doações
> * Bovespa cede 0,40% e encerra a semana em queda
> * Homem é preso em casa abandonado por funcionários na Paraíba
> * Lucro da Gol dispara 3,2% no 2o trimestre e atinge R$ 10,7 bi
> * Ex-diretor da Petrobrás quer ter até fim dia 8 para concluir oferta da LLX
> * Brasil lidera a América Latina por 2,5% da arrecadação de ICMS indica que empresa de Eike lidera redução de desemprego em São Paulo
> * Bovespa opera em queda nesta quarta
> * Bovespa recua nesta quinta, mas sobe quase 3% na semana
> * Em um dia, mais de 11 milhões deixaram o Brasil neste domingo
> * BC anuncia novo corte de juros nos conta corrente e no abono salarial de 2017
> * Polícia prende suspeitos de sequestro milionário em banco de João Pessoa
> * BC diz que crise política afeta investimentos
> * O golpe do sapato, uma história com as escolas de samba no Brasil
> * Criminosos fazem buraco em parede e explodem loja na Zona Sul de Teresina
> * Grupo rende funcionários e foge com reféns e armas em Sorocaba
> * Agência é assaltada em Ribeirão Preto
> * OGX mantém lucro de R$ 3,7 bilhões no 2º trimestre
> * Bovespa recua e perde linha dos 64 mil pontos
> * Bovespa fecha em alta, com ajuda grega e investidor
> * Bandidos explodem banco e roubam agência do RN
> * Conheça 15 espécies de aves, incluindo o papagaio-de-papo azul de Madagascar
> * Oferta de papéis do Pão de Açúcar supera investimento em US$ 10 bi por 3ª semana
> * Governo quer renegociações a bancos e estatais
> * Bovespa sobe com piora no cenário externo
> * Brasil recebe o primeiro banco comercial dos EUA que atua no setor financeiro
> * Veja quais os melhores países do mercado de trabalho do mundo
> * Dólar tem pior semana desde a abertura e fecha em R$ 3,45

## Conclusão

## Referências Bibliográficas
Touseef Iqbal, Shaima Qureshi. The survey: Text generation models in deep learning. In: Journal of King Saud University - Computer and Information Sciences, Volume 34, Issue 6, Part A. 2022. Pages 2515-2528. ISSN 1319-1578. https://doi.org/10.1016/j.jksuci.2020.04.001. Disponível em: https://www.sciencedirect.com/science/article/pii/S1319157820303360

Katikapalli Subramanyam Kalyan and Ajit Rajasekharan and Sivanesan Sangeetha.AMMUS : A Survey of Transformer-based Pretrained Models in Natural Language Processing. 2021. Disponível em: https://arxiv.org/abs/2108.05542

CAROSIA, Arthur Emanuel de Oliveira. Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações. 2022. 1 recurso online (129 p.) Tese (doutorado) - Universidade Estadual de Campinas, Faculdade de Tecnologia, Limeira, SP.
