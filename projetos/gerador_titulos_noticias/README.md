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

Este projeto gerou uma base de dados pública em língua portuguesa que contém títulos de notícias sintéticos utilizando técnicas de PLN para uso em projetos relacionados ao tema econômico utilizando análise de sentimentos em texto. A base criada possui 250 mil amostras sintéticas de títulos de notícias. Para avaliar a contribuição da adição de dados sintéticos ao desempenho de modelos de análise de sentimentos, avaliamos quantitativamente as amostras geradas e qualitativamente utilizando o modelo [fasttext](https://fasttext.cc/) de classificação de textos utilizando em CAROSIA (2021), entretanto a adição de dados artificiais não se mostrou benéfica para a tarefa analisada e os índices de desempenho desta tarefa não foi melhorado.

**Vídeo descritivo:** [Vídeo](https://youtu.be/eHPE9ebIPyA)

## Motivação
A crescente digitalização e automatização da compra e venda de ativos financeiros diferentes abordagens têm sido desenvolvidas com o intuito de maximizar os ganhos financeiros advindos das estratégias de trocas de ações. Neste contexto, a análise de sentimentos extraídos de textos como postagens em redes sociais ou notícias da seção de economia vêm ganhando destaque ao correlacionar a variação no preços de ativos financeiros com o tom presente nos textos analisados.

O desenvolvimento de modelos computacionais baseado em redes neurais profundas e similares, tem como prerequisito a aquisição de grandes massas de dados para treinamento, atividade que vem sendo dificultada pelo [fechamento de API's antes abertas e gratuitas](https://olhardigital.com.br/2023/06/01/internet-e-redes-sociais/twitter-api-cara-impede-uso-para-pesquisas-academicas/) ou [criação de mecanismos para dificultar a atividade de data scrapping](https://www.adweek.com/media/the-new-york-times-updates-terms-of-service-to-prevent-ai-scraping-its-content/). Neste cenário, a utilização de modelos gerativos passa a fazer sentido de modo a prover uma maior massa de dados para treinamento de modelos preditivos.

Além de prover aumento na quantidade das amostras, o desenvolvimento de datasets para a área pode facilitar a comparação de diferentes abordagens estudadas além de facilitar o desenvolvimento de novos trabalhos na área ao prover um dataset de referência padronizado.

## Objetivo

## Metodologia Proposta

O desenvolvimento do projeto se terá como base os dados disponível em: https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/GFJHFK
A partir daí, treinamos modelos gerativos pré-treinados (T-PTLMs) avaliando desempenho para gerarem títulos de qualidade. Dentre os modelos treinados, destacou-se um [modelo baseado em GPT-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) e treinado com dados da base de artigos da Wikipedia-PT.

Após o fine tuning do modelo pré-treinado, geramos uma base de títulos de notícias contendo 250 mil amostras e submetemos o conjunto gerado a métricas quantitativas e qualitativas através de duas estratégias de treinamento do classificador fasttext, descritas no tópico "Experimentos", a seguir.

### Bases de dados e Evolução
|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|Replication data for: predicting the brazilian stock market using sentiment analysis, technical indicators, and stock prices | [Repositório de dados Unicamp](https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/GFJHFK) | Base de títulos de notícias em língua portuguesa contendo aproximadamente 550 notícias rotuladas e 185 mil notícias não rotuladas para utilização em treinamento de rede neural profunda semisupervisionada utilizada na tese "[Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações](https://repositorio.unicamp.br/Acervo/Detalhe/1247846)".|4

O dataset contém diversos títulos de notícias no formato texto (txt) sem qualquer tipo de formatação. O conjunto contém:
  *  ~187 mil títulos não rotulados
  *  352 notícias classificadas como negativas
  *  296 notícias classificadas como positivas

Foram também disponibilizadas os códigos utilizados para treinar a aquitetura do modelo, incluindo o módulo de análise de sentimentos, que foi modificado para realização dos testes descritos neste trabalho.

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

![Workflow do trabalho realizado](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/Workflow.png)

## Experimentos, Resultados e Discussão dos Resultados

A seguir, descrevemos os procedimentos utilizados para gerar o modelo, compor a base de dados sintética e avaliar a base gerada.

### Finetunning do modelo

Os primeiros passos para a construção do dataset foram dados com o teste de diversos modelos pré-treinados de dados para verificar se realmente era possível a utilização dos dados disponíveis para treinar um modelo de LLM (Large Language Model) que realmente gerasse amostras diversas e inteligíveis. Apesar de alguns modelos realmente convergirem no treinamento, foram poucos os que realmente geravam dados inteligíveis e diversos e não meras cópias ou pequenas variações de amostras do conjunto de treinamento (overfit).

Neste contexto, modelos mais simples (menor quantidade de parâmetros) tiveram, de maneira geral, desempenho maior do que modelos mais complexos, de modo que modelos como o [GPorTuguese-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) (124 milhões de parâmetros) e [BLOOM LM](https://huggingface.co/bigscience/bloom-560m) (560 milhões de parâmetros) desempenharam-se melhor do que modelos mais atuais e complexos de até 7 bilhões de parâmetros. Tal fato provavelmente advém do tamanho limitado do dataset utilizado para treinamento. Enquanto os datasets de treinamento de LLMs chegam às centenas de Gigabytes ou Terabytes, nosso conjunto era pouco menor que 10Mb (9,09 Mb).

![Losses de treinamento e validação](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/fine-tunning-losses.png)

#### Ambiente de execução

Os modelos utilizados neste trabalho foram treinados utilizando, principalmente, três infraestruturas, a saber:
* [Google Colab PRO](https://colab.research.google.com/signup) - GPU T4 - 16 Gb VRAM - Aprox. 120h de utilização
* [RunPod](https://www.runpod.io/console/gpu-secure-cloud) - GPU A40 - 48 Gb VRAM - 4vCPU - Aprox. 16h de utilização
* Recod - 3 x GPU Quadro RTX 8000 - 48 Gb VRAM - Aproximadamente 100h de utilização

A título de exemplo, o treinamento final do modelo cujo gráfico de loss foi apresentado acima levou 8h 29min 40seg.

#### Parâmetros de treinamento

O modelo final foi treinado seguindo os seguintes parâmetros de treinamento:
````
 num_train_epochs=120,
 per_device_train_batch_size=156
 per_device_eval_batch_size=256
 eval_steps = 500
 save_steps=500
 warmup_steps=200
 prediction_loss_only=False,
 evaluation_strategy="steps",
 weight_decay = 0
````

O conjunto de treinamento foi dividido na seguinte razão:
````
 test_size=0.15
````

### Geração do dataset

A geração do dataset sintético consiste em iterar sobre o método de inferência do modelo infinitamente.
Para esta tarefa, foram consideradas duas abordagens: sem prompt e utilizando um prompt.

#### Geração sem prompt
Consiste em gerar amostras sem utilizar um prompt específico.
Na primeira iteração, gera-se amostras utilizando uma string vazia `"  "` como prompt. A seguir, utiliza-se a última notícia gerada (geralmente incompleta) como prompt para geração do próximo lote de amostras.
Para cada execução, são geradas entre 5 e 7 amostras, na maioria das iterações. Esta etapa foi efetuada em computador local e utilizando-se da plataforma Google Colab PRO e, juntas, somaram mais de 72h de tempo de processamento. Observou-se que após a geração de cerca de 150 mil amostras, a taxa de geração de amostras repetidas superou a taxa de geração de amostras inéditas, o que pode sugerir um "esgotamento criativo" do modelo. Após 190 mil amostras geradas, menos e 1% das novas amostras eram inéditas, o que nos levou a tentar uma segunda abordagem de geração descrita a seguir.

Exemplos de amostras geradas:

Prompt (última amostra da iteração anterior): `Bovespa fecha em queda,`
````
Bovespa fecha em queda, puxada por Petrobras e Vale
Bovespa perde 0,40% na abertura; dólar marca R$ 1,75
Bolsa de São Paulo: Ibovespa abre em alta de 0,36%
Dólar fecha a R$ 3,239, menor cotação em um mês, com cenário externo e eleições
Ibovespa perde força com mercado à espera da declaração de Pizzolato
Dólar fecha a R$ 1,65; Bovespa sobe 0, (descartada e utilizada como prompt da próxima iteração)
````

#### Geração com prompt
Após a geração de aproximadamente 200 mil amostras utilizando a estratégia sem prompt e diante da estagnação da geração de amostras inéditas, expermimentou-se a geração de amostras utilizando como prompt uma palavra aleatória do dataset original. O objetivo era verificar se o fornecimento de uma palavra ajudava o modelo a gerar novas amostras. Para tanto, mapeamos todas as palavras presente no dataset original (eliminando as repetições) e fornecemos uma palavra aleatória como prompt para cada iteração da inferência.

O primeiro e o último títulos gerados foram descartados por serem (quase sempre) incompletos.

Exemplos de amostras geradas:

Prompt (palavra aleatória): `Céus`
````
Céus de água na maior estufa do Brasil (descartada)
Dilma anuncia R$ 8,1 bi ao Orçamento da Previdência para 2020
Bandidos assaltam agência do Banco do Brasil em Matão, Zona da Mata Central do MA
Bolsa de São Paulo: Ibovespa fecha em baixa de 1,27%
Em dia de recuperação da Petrobras, Bovespa tem leve queda
BTG Pactual quer fechar capital da BR Distribuidora
Petrobras garante liderança isolada entre anunciantes do setor no ano
Conf (descartada)
````

##### Loop infinito de geração uma amostra
Consiste em um fenômeno em que o gerador fica preso na geração de uma amostra infinitamente. Este fenômeno foi observado quando aumentamos a quantidade máxima de token de cada iteração. A seguir um exemplo de sua ocorrência:

Prompt: `Saiba como ajudar desabrigados`
````
Saiba como ajudar desabrigados em tragédia no Rio Grande do Sul
Banco Central corta taxa de juros de títulos públicos
Com queda na Selic, investidor adota cautela e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57
````
Prompt: `Com queda na Selic, investidor adota cautela e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57`
````
Com queda na Selic, investidor adota cautela e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando
````
Prompt: `Com queda na Selic, investidor adota cautela e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando`
````
Com queda na Selic, investidor adota cautela e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Ibovespa segue avançando na linha dos 57 mil pontos e Iboves
````

Note que o modelo entra em loop na geração de uma amostra e não consegue terminá-la, sempre repetindo o padrão " e Ibovespa segue avançando na linha dos 57 mil pontos".

### Avaliação Quantitativa

**adicionar breve explicação da métrica**

Perplexity (gpt-2):
Perplexity (gpt2-small-portuguese): 430,75
Perplexity (ours):115,31

![Perplexidade](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/Perplexidade.png)

### Avaliação Qualitativa

#### Abordagem Supervisionada

**explicar qual o modelo de classificação** e metodologia

![Balanceamento da Classificação Automática](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/Balanceamento%20da%20classifica%C3%A7%C3%A3o%20autom%C3%A1tica.png)

![Balanceamento por percentil](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/Balanceamento%20por%20percentil.png)

![Métricas de desempenho da Abordagem spervisionada](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/M%C3%A9tricas%20de%20desempenho%20do%20treinamento%20supervisionado%20(1).png)

#### Abordagem não supervisionada

**completar**

## Conclusão

A geração das amostras sintéticas não melhorou o desempenho da tarefa proposta.
Pode ser que seja interessante em outros modelos, arquiteturas ou problemas.

## Referências Bibliográficas
IQBAL, Touseef. QURESHI, Shaima. The survey: Text generation models in deep learning. In: Journal of King Saud University - Computer and Information Sciences, Volume 34, Issue 6, Part A. 2022. Pages 2515-2528. ISSN 1319-1578. https://doi.org/10.1016/j.jksuci.2020.04.001. Disponível em: https://www.sciencedirect.com/science/article/pii/S1319157820303360

KALYAN, Katikapalli Subramanyam. RAJASEKHARAN,  Ajit. SANGEETHA, Sivanesan. AMMUS : A Survey of Transformer-based Pretrained Models in Natural Language Processing. 2021. Disponível em: https://arxiv.org/abs/2108.05542

CAROSIA, Arthur Emanuel de Oliveira. Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações. 2022. 1 recurso online (129 p.) Tese (doutorado) - Universidade Estadual de Campinas, Faculdade de Tecnologia, Limeira, SP.

RADFORD, Alec. WU, Jeffrey. CHILD, Rewon. LUAN, David. AMODEI, Dario. SUTSKEVER, Ilya. Language Models are Usupervised Multitask Learners. 2018. 
