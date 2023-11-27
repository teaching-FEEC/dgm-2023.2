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

Este projeto gerou uma base de dados pública em língua portuguesa que contém títulos de notícias sintéticos utilizando técnicas de PLN para uso em projetos relacionados ao tema econômico utilizando análise de sentimentos em texto. A base criada possui 230 mil amostras sintéticas de títulos de notícias. Para avaliar a contribuição da adição de dados sintéticos ao desempenho de modelos de análise de sentimentos, avaliamos quantitativamente as amostras geradas e qualitativamente utilizando o modelo [fasttext](https://fasttext.cc/) de classificação de textos utilizando em CAROSIA (2021), entretanto a adição de dados artificiais  nesta tarefa não melhou índices de desempenho.

**Vídeo descritivo:** [Vídeo](https://youtu.be/eHPE9ebIPyA)

## Motivação
A crescente digitalização e automatização da compra e venda de ativos financeiros diferentes abordagens têm sido desenvolvidas com o intuito de maximizar os ganhos financeiros advindos das estratégias de trocas de ações. Neste contexto, a análise de sentimentos extraídos de textos como postagens em redes sociais ou notícias da seção de economia vêm ganhando destaque ao correlacionar a variação no preços de ativos financeiros com o tom presente nos textos analisados.

O desenvolvimento de modelos computacionais baseado em redes neurais profundas e similares, tem como prerequisito a aquisição de grandes massas de dados para treinamento, atividade que vem sendo dificultada pelo [fechamento de API's antes abertas e gratuitas](https://olhardigital.com.br/2023/06/01/internet-e-redes-sociais/twitter-api-cara-impede-uso-para-pesquisas-academicas/) ou [criação de mecanismos para dificultar a atividade de data scrapping](https://www.adweek.com/media/the-new-york-times-updates-terms-of-service-to-prevent-ai-scraping-its-content/). Neste cenário, a utilização de modelos gerativos passa a fazer sentido de modo a prover uma maior massa de dados para treinamento de modelos preditivos.

Além de prover aumento na quantidade das amostras, o desenvolvimento de datasets para a área pode facilitar a comparação de diferentes abordagens estudadas além de facilitar o desenvolvimento de novos trabalhos na área ao prover um dataset de referência padronizado.

## Objetivo

O objetivo principal deste projeto é desenvolver um sistema capaz de gerar títulos de notícias financeiras em língua portuguesa (BR). Para alcançar esse propósito, foram explorados métodos que ampliam o volume de dados por meio da criação de conjuntos sintéticos através do treinamento de redes neurais profundas baseadas em modelos gerativos pré-treinados (T-PTLMs).

Além disso, a análise da performance de modelos utilizando dados reais versus dados sintéticos também foi um importante foco deste estudo. Avaliamos o impacto e a eficácia desses dados sintéticos na precisão dos modelos de análise de sentimento aplicados ao mercado financeiro.

Investigamos, também, como a aplicação de dados gerados artificialmente influenciou o desempenho de uma tarefa específica de Análise de sentimentos para o mercado financeiro e a contribuição da incorporação destes dados na mitigação das limitações das bases de dados existentes, proporcionando novas perspectivas e melhorando a o desempenho dos modelos treinados para tarefas relacionadas ao mercado financeiro que utilizam Processamento de Linguagem Natural (PLN).

Um dos resultados práticos deste projeto foi a geração e disponibilização de um dataset sintético em língua portuguesa (BR) para a comunidade na esperança de que esse conjunto de dados contribua para a pesquisa e o avanço de modelos de PLN aplicados ao domínio financeiro, beneficiando a comunidade interessada nessa área de estudo.

## Metodologia Proposta

O desenvolvimento do projeto se terá como base os dados disponível em: https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/GFJHFK
A partir daí, efetuamos *fine tuning* em  modelos gerativos pré-treinados (T-PTLMs) avaliando desempenho para gerarem títulos de qualidade. Dentre os modelos treinados, destacou-se um [modelo baseado em GPT-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) e treinado com dados da base de artigos da Wikipedia-PT.

Após o fine tuning do modelo pré-treinado, geramos uma base de títulos de notícias contendo quase 230 mil amostras e submetemos o conjunto gerado a métricas quantitativas e qualitativas através de duas estratégias de treinamento do classificador fasttext, descritas no tópico "Experimentos", a seguir.

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

### O GPT-2 Small

O modelo GPT-2 small é o modelo utilizado como base para os experimentos conduzidos neste projeto. Contendo 124 milhões de parâmetros, o modelo GPT-2 Small é uma versão reduzida da arquitetura GPT-2 (1,5 bilhão de parâmetros), desenvolvida pela OpenAI. Ele faz parte da família de modelos GPT (Generative Pre-trained Transformer), que são modelos de linguagem pré-treinados usando a técnica de aprendizado de máquina conhecida como transferência de aprendizado. O GPT-2 Small é uma versão mais compacta em comparação com suas contrapartes maiores, como o GPT-2 Medium e o GPT-2 Large, sendo projetado para tarefas que demandam menos recursos computacionais.

Composta por uma rede neural de transformer, a arquitetura do GPT-2 Small inclui camadas de atenção multi-head, módulos de normalização e redes neurais totalmente conectadas. Uma característica notável do GPT-2 Small é sua capacidade de gerar texto coerente e contextualmente relevante, mesmo em tarefas de geração de linguagem complexas, como continuação de textos ou resposta a perguntas.

O fato do modelo GPT-2 Small ter menos parâmetros em comparação com versões maiores da série GPT-2, ou outros modelos estado da arte que chegam a ter 7 bilhões ou mais de parâmetros pode ter sido fundamental para a geração do nosso dataset uma vez que a quantidade de dados que disponíveis para treinamento eram limitadas (180 mil amostras) e seu tamanho reduzido facilitou o treinamento em infraestrutura mais leve (treinou com relativa rapidez mesmo em GPU's de 16GB de VRAM como RTX A4000 e T4 (Google Colab).

### Finetunning do modelo

Os primeiros passos para a construção do dataset foram dados com o teste de diversos modelos pré-treinados de dados para verificar se realmente era possível a utilização dos dados disponíveis para treinar um modelo de LLM (Large Language Model) que realmente gerasse amostras diversas e inteligíveis. Apesar de alguns modelos realmente convergirem no treinamento, foram poucos os que realmente geravam dados inteligíveis e diversos e não meras cópias ou pequenas variações de amostras do conjunto de treinamento (overfit).

Neste contexto, modelos mais simples (menor quantidade de parâmetros) tiveram, de maneira geral, desempenho maior do que modelos mais complexos, de modo que modelos como o [GPorTuguese-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) (24 milhões de parâmetros) e [BLOOM LM](https://huggingface.co/bigscience/bloom-560m) (560 milhões de parâmetros) desempenharam-se melhor do que modelos mais atuais e complexos de até 7 bilhões de parâmetros. Tal fato provavelmente advém do tamanho limitado do dataset utilizado para treinamento. Enquanto os datasets de treinamento de LLMs chegam às centenas de Gigabytes ou Terabytes, nosso conjunto era pouco menor que 10Mb (9,09 Mb).

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
 learning_rate=2e-5
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

Note que o modelo entra em loop na geração de uma amostra e não consegue terminá-la, sempre repetindo o padrão " e Ibovespa segue avançando na linha dos 57 mil pontos" indefinidamente.

### O dataset artificial de títulos de notícias

Nosso dataset artificial de títulos de notícias está [disponível livremente para download](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/dataset_final.txt) e contém 229.639 amostras únicas de títulos de notícias relacionados majoritariamente a assuntos do mercado financeiro.


#### Alucinações
``Com maior margem para pagamento, clientes reclamam do IPTU em Campina Grande; veja Com menor margem para pagamento, clientes reclama do IPTU em Campina Grande; veja Veja as tarifas cobradas pelos bancos em até dois dias, mas bancos só pagaram com desconto após a declaração do IR 2017``

#### Miniloop
``Bovespa sobe, com bancos e siderúrgicas ofuscando queda de Bovespa sobe, com Petrobras e siderúrgicas ofuscando queda de Bovespa fecha em movimento de baixa pela primeira vez desde julho``

``BC deve reforçar taxa de juros para evitar intervenção do BC deve reforçar taxa de juros para evitar intervenção do BB deve reforçar taxa de juros para evitar intervenção do BB anuncia redução de juros nos próximos dias``

``BB eleva limite de crédito imobiliário para bancos em R$ 12 bi no BB aumenta limite de crédito imobiliário para bancos em R$ 12 bi no Minha Casa, Minha Vida 2``

``BTG Pactual vai investir US$ 1 bi e se unirá ao BTG Pactual vai investir US$ 1 bi e se unirá ao BTG Pactual vai investir US$1 bi e se unirá ao BB quer retomar obras em áreas como saúde. Acionistas querem aprovar a privatização do banco a partir de 2018``

``Bancos Centrais devem anunciar data para novos estímulos à Bancos Centrais devem anunciar data para novos estímulos à Bancos Centrais devem anunciar data para novos estímulos à Bovespa cai 0,29%; Banco Central baixa para 0,57% a desvalorização de 0,2% do dólar``

#### Predileção por assalto a agências bancárias
Provavelmente proveniente da quantidade de notícias sobre o assunto no conjunto de treinamento.

``Quadrilha explode caixas de banco e depois atira contra destacamento da PM``

``Ladrões furtam caixas eletrônicos do Itaú em Itaju do Colônia, RS``

``Quadrilha explode caixas eletrônicos de duas agências em Boquira``

``Grupo explode caixas eletrônicos em São Domingos dos de Benfica, SP``

``Grupo armado invade banco e explode caixas eletrônicos em São José do Vale do Rio Preto, no RJ``

``Em 3 minutos, quadrilha armada rouba caixas eletrônicos de duas agências``

#### Notícias abandonadas no meio da geração
``Ações de construção e empresas da Vale puxam ganhos da Depois de abrir a semana em alta, Bovespa fecha no vermelho nesta quinta``

``Bolsas operam em alta nesta terça-feira, mas balanços ainda atrapalham a Bovespa tem pior desempenho mensal desde novembro de 2009``

#### Notícias de outros assuntos
``O melhor da hora - Mauro Nogueira Jr.``

``Confira programação da ExpoSP no Paraná e AL``

``Brasil vence o Japão e garante vaga olímpica``

``Eclipse causa destruição em várias cidades do Brasil``

``Em Manaus, moradores de rua têm vagas para quem têm conta paga até dia 30; veja as oportunidades``

``Polícia Federal encerra investigação que investiga negócios de Cabral em obras nos EUA``

#### Títulos aparentemente incompletos
``Grupo de hackers``

``O novo presidente do Banco Central``

### Avaliação Quantitativa

Para a avaliação quantitativa, utilizamos duas métricas de avaliação: *cross entropy* e *perpelexity*, que são as métricas apresentadas nos resultados dos modelos utilizados como base.

#### Cross Entropy

A métrica comumente utilizada como função de perda (*loss function*) para treinamento de modelos profundos de aprendizados, mede a "proximidade" do modelo previsto em comparação com o originalmente proposto. Os resultados obtidos no treinamento do nosso modelo foram numericamente compatíveis com o resultado do treinamento do modelo base.

![Losses](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/loss2.png)


#### Perplexity

A perplexidade mede a capacidade do modelo de gerar uma sequência de tokens dado o contexto das palavras anteriores. Pode também ser entendida como o nível de "surpresa" que o modelo acarreta ao gerar tokens diversos do que era originalmente esperado. Deste modo, quanto menor o valor da perpexidade, melhor o desempenho do modelo avalidado.
![Perplexidade](https://thegradient.pub/content/images/2019/10/Screenshot-from-2019-10-08-15-56-38-2.png)

Seu cálculo é feito através do produtório de probalilidades (atribuído pelo modelo) da próxima palavra ser aquela da amostra de avaliação.
![probabilidade](https://thegradient.pub/content/images/2019/10/lm-1.png)
Fonte: [The Gradient](https://thegradient.pub/understanding-evaluation-metrics-for-language-models/)

Conseguimos gerar um modelo que se adaptou para o dataset de treinamento, fato ilustrado pela diminuição da perplexidade do nosso modelo pela base de notícias. Mas ainda assim, os resultados ficaram longe dos considerados "estado da arte" na época de seus lançamentos. Cabe lembrar que a métrica de perplexidade consideravelmente maior dos modelos ``gpt-2`` e ``gpt2-small-portuguese`` para o conjunto de notícias, se deve ao fato dos modelos não serem treinados utilizando estas bases de notícias, como o nosso modelo foi.

| Modelo/Dataset | NOTICIAS | ORIGINAL |
|----- | ----- | -----|
| gpt-2 | 574,65 | 29,41 |
| gpt2-small-portuguese | 430,75 | 23,76 |
| OUrs | 115,31 | - |

![Perplexidade](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/Perplexidade2.png)

### Avaliação Qualitativa

A avaliação qualitativa consistiu no  teste da hipótese de que a adição de dados sinéticos poderiam melhorar o desempenho de um classificador na tarefa de analisar o sentimento nos títulos de notícias relacionadads à economia. Para operacionlizá-la, recorremos a duas abordagens de treinamento: supervisionada e semi-supervisionada. Na primeira, classificamos as amostras sintéticas automaticamente com o auxílio de um modelo pronto e, em seguida, incorporados ao conjunto de treinamento do classificador. Na abordagem semi-supervisionada ingênua implementada, as amostras são classificadas iterativamente a medida em que as amostras cuja classificação superam um limiar escolhido são incorporadas ao conjunto de treinamento.

#### Fasttext

O [Fasttext](https://fasttext.cc/) é um modelo disponibilizado pelo Facebook originalmente criado para criar representações vetoriais de textos, mas que pode ser também utilizado como classificador de textos. Foi utilizado por CAROSIA (2022) como módulo de análise de sentimentos de uma arquitetura de predição de preços de ações e é a tarefa que tentamos melhorar durante este trabalho pelas estratégias supervisionada e semi supervisionada.

#### Abordagem Supervisionada

Primeiramente, foi testada uma abordagem supervisionada para análise de sentimentos das amostras sintéticas. Esta abordagem requer o uso de dados anotados para treinamento. Numa tentativa de anotar os dados sintéticos utilizamos o modelo [distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student), baseado em distilbert, otimizado para classificar sentimentos em várias línguas em positivo ou negativo.

A partir daí, as amostras com pontuação maior que 0.5 positivas ou negativas foram organizadas em um conjunto de dados intermediário separados em percentis em incrementos de 10 pontos percentuais. A seguir, a quantidade de amostras de cada percentil e exemplos de amostras do dataset artificial classificadas e suas pontuações.

| Amostra | Sentimento | Score |
| -- |-- |--|
| Bovespa registra 3ª queda por preocupações com Europa | Negativo | 0,58 |
| BB deve emprestar US$ 3 bilhões para tentar combater preços no câmbio | Positivo | 0,52 |
| BC diz que inflação vai subir em 2014 e não crescer em 2015 | Negativo | 0,62 |
| Brasil conquista os 90 mil pontos com virada no fim | Positivo | 0.69 |
| Bovespa ganha com exterior positivo, e fecha em alta de 0,2% | Positivo | 0,88 |
| Criminosos quebram parede para roubar dois caixas eletrônicos | Negativo | 0,74 |
| Mercado reduz pessimismo e Bolsa mantém alta; dólar cai a R$ 3,17 | Negativo | 0,90 |
| Bolsas da Ásia fecham em alta com dados positivos dos EUA | Positivo | 0,91 |
| Com cenário externo positivo, Ibovespa fecha em alta de 3,49% | Positivo | 0,93 |
| Bovespa opera em queda com pessimismo global | Negativo | 0,91 |

Nota-se que notícias parecidas podem ganhar pontuações discrepantes e que existe um pequeno desbalanceamento para notícias positivas o que pode significar um viés positivo no modelo de geração ou um viés na classificação.

![Balanceamento por percentil](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/classificacao_automatica.png)

Amostras por sentimentos/percentil
|Sentimentos/Percentil| [0,5-0,6[ | [0,6-0,7[ | [0,7-0,8[ | [0,8-0,9[ | [0,9-1,0] | Total |
|-|-|-|-|-|-| -|
|Positivo | 22.580 | 10.396 | 4.389 | 2.818 | 674 | 40857 |
|Negativo | 10.198 | 6.247 | 9.643 | 3.951 | 421 | 30460 |

Após a classificação automática, os dados sintéticos foram adicionados ao conjunto de treinamento respeitando o percentil de cada experimento da seguinte maneira:
* Os dados originais foram separados em treinamento e teste de acordo com o paper base ``(80% para treinamento, 20% para teste)`` e ``random_seed = 42``
* Os dados sintéticos foram adicionados ao conjunto de treinamento.

![Métricas de desempenho da Abordagem spervisionada](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/resultado_superv.png)

Ao final dos exeperimentos, observamos que não houve melhoria dos índices alcançados por CAROSIA (2022). A cada percentil adicionado ao conjunto de testes, foram observadas pioras em todas as métricas observadas, sendo indicativo que a adição de amostras sintéticas não ajudou o modelo na classificação das amostras de teste.

#### Abordagem não supervisionada

A segunda abordagem experimentada foi a eliminação do classificador completamente e adoção de uma abordagem semi-supervisionada ingênua. A abordagem implementada consistia em utilizar o próprio classificador treinado pelo conjunto de amostras anotadas original para classificar as amostras sintéticas geradas e retreinar o classificador iterativamente incorporanddo as amostras classificadas acima de um limiar escolhido ao conjunto de treinamento. A cada iteração as amostras vão sendo incorporadas ao conjunto de treinamento e o novo modelo é testado.

Os parâmetros de treinamento podem ser consultados a seguir:
``
threshold = [0.85, 0.95, 0.99, 0.9995, 1]
max_iter = 10 #numero maximo de iterações
``
critérios de parada:
* max_iter
* 90%+ do conjunto não anotado incorporado ao teste
* incremento do conjunto de testes >1% do conjunto de amostras não incorporadas

Observa-se acima que para limiares abaixo de 95%, atinge-se o critério de parada de incorporação de 90% do conjunto de treinamento de maneira muito rápida, em menos de 4 iterações. Por este motivo, os experimentos se concentraram em valores de ``treshold  > 0.999``.


![Métricas de resultado do treinamento semi supervisionado](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/train_size.png)

 A seguir, é apresentado um histograma de classificação das amostras sintéticas na primeira iteração, ou seja, no classificador treinado apenas com os dados originais assim como exemplos de títulos e seus escores na primeira iteração do modelo.

**histograma de classificação para demonstrar que o modelo tende a classificar muito nas pontas**
| Amostra | Sentimento | Score |
| -- |-- |--|
| Bovespa vira e passa a operar em leve queda nesta quinta | Negativo | 0,95878 |
| Bolsas europeias fecham em alta após PIB e indicadores dos EUA | Positivo | 0,99775 |
| Dólar tem maior baixa mensal desde janeiro; Petrobras cai mais de 4% | Negativo | 0,99335 |
| Itaú prevê crescimento de até 3% menos no 2º trimestre do que estimativa original | Positivo | 0.68669 |
| Brasil e Argentina decidem o Banco Mundial de Alimentos | Negativo | 0,66921 |
| BC e banco dos EUA anunciam corte no juro | Negativo | 0,88466 |
| Ibovespa fecha em queda, abaixo de 59 mil pontos | Negativo | 0,99998 |
| Bolsa cai e juros futuros fecham em queda após decisão do Fed | Negativo | 1 |
| Bovespa descola de Wall Street e sobe, puxada por bancos pequenos | Negativo | 0,60183 |
| Polícia Civil de SC apreende tijolos de maconha em banco de Goiânia | POsitivo | 0,52862 |
| Bovespa fecha em baixa de 1,48% | Negativo | 0,52366 |

![Histograma das amostras classificadas como Negativa](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/fasttext_histo.png)

Os experimentos conduzidos para os limiares escolhidos mostraram, como ilustrados pelos gráficos abaixo, que as métricas de desempenho foram diminuindo a cada iteração, conforme dos dados eram incorporados ao conjunto de treinamento. A única exceção é a métrica de precisão, que aumentou em alguns períodos prossivelmente devido ao claro viés do modelo treinado pela classificação de amostras como negativas.
![Gráfico do tamanho do conj. treinamento por threshold e iteration](https://github.com/mmakita/IA376_gerador_titulos/blob/main/projetos/gerador_titulos_noticias/reports/figures/metricas_semisuper.png)

## Sobre a pegada de carbono no desenvolvimento do projeto
Ao realizar os testes para o desenvolvimento deste projeto, geramos uma pegada de carbono estimada em mais de 50 kg de CO2 emitido. Essa quantidade de emissão, equivalente à energia consumida por um carro em cerca de 240 km, levanta questões éticas cruciais. A necessidade de avanços tecnológicos e experimentação em inteligência artificial deve ser ponderada em relação ao impacto ambiental que tais testes acarretam. Até que ponto vale a pena investir recursos significativos e realizar experimentos extensivos, considerando o impacto ambiental substancial associado? É fundamental repensar e buscar abordagens mais sustentáveis na pesquisa e desenvolvimento de tecnologias, visando minimizar o impacto ambiental, especialmente em setores que demandam intensa computação como o da inteligência artificial.

## Conclusão

O principal objetivo de criar uma base de dados sinteticos foi alcançado e a base de dados de notícias sintéticas foi gerada com o desenvolvemos um gerador de títulos de notícias financeiras em português com o modelo GPT-2 Small. Testamos o uso de dados sintéticos para melhorar a análise de sentimentos em títulos econômicos e utilizamos abordagens supervisionadas e semi-supervisionadas para treinar o modelo. Apesar da adaptação do modelo aos dados, os resultados ainda não atingiram o "estado da arte". A métrica de perplexidade dos modelos GPT-2 e GPT-2 Small para o conjunto de notícias foi maior, pois não foram treinados com esses dados. Aprendemos sobre a importância das estratégias de treinamento, a influência dos dados sintéticos e a utilidade do Fasttext na análise de sentimentos. Este projeto expandiu nosso conhecimento em modelos de linguagem e uso de dados sintéticos para análise de sentimentos em textos financeiros. Apesar da geração das amostras sintéticas não ter melhorado o desempenho da tarefa testada, o modelo pode ser que útil em outras tarefas ou treinamento de arquiteturas no campo de NLP.

## Referências Bibliográficas
IQBAL, Touseef. QURESHI, Shaima. The survey: Text generation models in deep learning. In: Journal of King Saud University - Computer and Information Sciences, Volume 34, Issue 6, Part A. 2022. Pages 2515-2528. ISSN 1319-1578. https://doi.org/10.1016/j.jksuci.2020.04.001. Disponível em: https://www.sciencedirect.com/science/article/pii/S1319157820303360

KALYAN, Katikapalli Subramanyam. RAJASEKHARAN,  Ajit. SANGEETHA, Sivanesan. AMMUS : A Survey of Transformer-based Pretrained Models in Natural Language Processing. 2021. Disponível em: https://arxiv.org/abs/2108.05542

CAROSIA, Arthur Emanuel de Oliveira. Previsão do mercado de ações brasileiro com o uso de análise de sentimentos, indicadores técnicos e valores de ações. 2022. 1 recurso online (129 p.) Tese (doutorado) - Universidade Estadual de Campinas, Faculdade de Tecnologia, Limeira, SP.

RADFORD, Alec. WU, Jeffrey. CHILD, Rewon. LUAN, David. AMODEI, Dario. SUTSKEVER, Ilya. Language Models are Usupervised Multitask Learners. 2018. 
