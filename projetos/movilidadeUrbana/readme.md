![Mobilidade Urbana projet](https://github.com/anamabri/dgm-2023.2/assets/35360195/266daa3b-55e3-49e6-a182-d4f2a9f957f2)


<h2 id="membros-do-projeto">Apresentação</h2>

O presente projeto foi originado no âmbito das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

| Nome          | RA     | Curso           |
| ------------- | ------ | --------------- |
| Ana Briones (Github owner)| 272309 | Mestrando em Elétrica    |
| Miguel Gaybor  | 252040 | Mestrando em Elétrica    |
| Johsac Gomez   | 216401 | Doutorando em Elétrica   |

<h2 id="resumo">Resumo (Abstract)</h2>
Este projeto utiliza a geração de dados sintéticos para prever informações de velocidade ao longo do tempo. Embora o enfoque principal seja na velocidade, características como latitude, altitude, longitude e tempo foram incorporadas para enriquecer a obtenção de dados. Além das metodologias tradicionais de processamento de dados, integra-se uma Rede Generativa Adversarial Profunda (GAN) para aprimorar a qualidade dos dados sintéticos. A metodologia envolve a coleta abrangente de dados de ônibus da Universidade de Campinas, filtragem e rotulagem, com ênfase especial nos dados de 2022. A aplicação do GAN contribui para conjuntos de dados sintéticos mais precisos e realistas, abordando a escassez de conjuntos de dados abertos para pesquisa em mobilidade urbana e transporte. Esses conjuntos de dados enriquecidos são inestimáveis para o estudo e a melhoria dos sistemas de transporte urbano, promovendo o desenvolvimento sustentável na área.


<h2 id="descrição-do-projeto">Descrição do Projeto</h2>
Nosso projeto tem como foco a geração sintética de dados de velocidade do ônibus, utilizando modelos de redes generativas. O objetivo é lidar com a escassez de conjuntos de dados abertos para pesquisa e desenvolvimento em mobilidade urbana e transporte. Esses dados sintéticos fornecerão uma alternativa em termos de privacidade e segurança, reduzindo a necessidade de uma coleta intensiva de dados físicos e permitindo a criação de cenários diversos não disponíveis nos dados do mundo real. Os dados sintéticos gerados serão valiosos para testar algoritmos, simular ambientes e melhorar aplicativos baseados em dados relacionados a ônibus, contribuindo para o avanço da mobilidade urbana.



## Objetivos do Projeto

 * Implementar técnicas de estatísticas de filtragem para remover dados irrelevantes, como dados de fora do horário de operação dos ônibus e instâncias de alta variabilidade.
 * Gerar um conjunto de dados sintéticos abrangente de velocidade de ônibus que possa ser usado para o estudo e aprimoramento de sistemas de transporte urbano.
 * Comparar o conjunto de dados sintéticos com dados do mundo real.

## Metodologia

![fluxograma](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/eaa22310-8bac-41bd-9a4c-f86cfbcd5412)

Pré-processamento de Dados:

* Aplicação de métodos estatísticos para filtrar os dados coletados e identificar instâncias de alta variabilidade, que podem incluir flutuações extremas de velocidade ou valores atípicos [1].
* Remover pontos de dados com variabilidade excessiva para garantir a qualidade e consistência do conjunto de dados.
* Eliminação dos pontos de dados que estão fora do horário operacional dos ônibus.
* Categorização dos pontos de dados em dois estados: "Estacionário" e "Em Movimento" para diferenciar os períodos em que o ônibus está parado e em trânsito. Isso fornece insights sobre as rotas e ajuda a distinguir entre os estados dos ônibus durante a análise de dados.


### Classificação das Variáveis

| Variáveis       | Clasificação      |
| -------------   | ------------------|
| Velocidade       |     Inerciais     |
| Longitude       |     Orientação    |
| Altitude        |     Orientação    |
| Latitude        |     Orientação    |
| Tempo  (segundos)      |     Tempo        |
|Número de Viagens|     Horario       |

### Bases de Dados e Evolução


|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|Base de dados de Mobilidade Urbana | privada | Base de dados do Laboratorio Vivo de Mobilidade Urbana da UNICAMP. Dados coletados por dispositivos nos anos de 2021, 2022 e 2023.|

O ônibus da Universidade de Campinas (Unicamp) possui registros de dados coletados por dispositivos nos anos de 2021, 2022 e 2023. Decidiu-se tomar o ano de 2022 como ponto de referência, uma vez que nesse ano a pandemia já não estava presente e dados completos estavam disponíveis.

Em relação aos dados coletados em 2022, a maioria dos meses possui aproximadamente um milhão de registros, sendo os meses de abril, maio, julho e agosto os que apresentam maior frequência. Além disso, há um arquivo que registra o início e o fim de cada viagem. Como resultado, determinou-se que o conjunto de dados inicial para conduzir experimentos seria o correspondente ao meses de abril, maio ,julho e agosto de 2022.

![1](https://github.com/anamabri/dgm-2023.2/assets/35360195/ddf2a16d-d02a-453a-a2be-3cc92e45294f)


Filtro 1: Eliminação por Velocidade

Foram removidos os registros correspondentes a estacionamentos nos quais a velocidade registrada não é igual a zero. Isso ajuda a garantir que apenas paradas legítimas sejam consideradas, evitando dados incorretos ou artefatos.

Filtro 2: Restrição de Horário

Foram descartados os dados correspondentes a horas fora do horário de funcionamento do ônibus. O horário operacional considerado é das 07:00 às 18:00, de segunda a sexta-feira. Isso permite concentrar-se nos momentos de atividade real do serviço.

Filtro 3: Variabilidade de Distância com Centroides

Foi avaliada a variabilidade das distâncias dos registros em relação aos centroides mais próximos, obtidos por meio de um processo de agrupamento. Foram eliminadas as rotas que apresentam altas variabilidades de distância, uma vez que se espera que uma rota padronizada não tenha grandes desvios. Isso assegura que os dados considerados reflitam as rotas típicas e não variações anômalas ou incorretas. 

![2](https://github.com/anamabri/dgm-2023.2/assets/35360195/1543b115-78bf-43ca-90cd-29925a8e8e9e)


Filtro 4: Eliminação por Densidade de Agrupamento

Foram eliminados os agrupamentos que apresentavam uma baixa concentração de registros de dados. Isso permite descartar agrupamentos que não são representativos e que poderiam ser resultado de ruído ou dados atípicos.

Filtro 5: Rotulagem de Estado

Foram introduzidas duas etiquetas para classificar o estado do ônibus: "Estacionado" e "Em Movimento". Para isso, foi utilizada uma janela de análise que considera a proximidade às localizações de estacionamento e uma velocidade próxima a zero. Essa rotulagem fornece uma segmentação clara do conjunto de dados, permitindo identificar facilmente os momentos em que o ônibus está parado ou em movimento.
A tabela "tabela_viaje" apresenta dados coletados sobre o estado dos ônibus em diferentes terminais. A coluna "estacionado" indica a quantidade de tempo (ou eventos) que o ônibus passou no estado de estacionamento, enquanto "viajando" indica quanto tempo (ou eventos) o ônibus passou em movimento.

![3](https://github.com/anamabri/dgm-2023.2/assets/35360195/30019d78-06c4-425b-8b0f-40240c02e5f2)


Ônibus no estacionamento: Quando a coluna "estacionado" possui um valor alto e "viajando" é zero, como no terminal 1, isso significa que o ônibus permaneceu estacionado durante todo o período registrado.

Ônibus começa a se mover dentro do estacionamento: Se a coluna "estacionado" possui um valor e a coluna "viajando" também possui um valor, mas é menor, como no terminal 6, isso sugere que o ônibus começou a se mover, mas ainda dentro do estacionamento.

Ônibus continua no estacionamento: Em registros como o do terminal 9, onde "estacionado" tem um valor significativo e "viajando" é zero, indica que o ônibus permanece estacionado.

Ônibus sai do estacionamento e viaja: Se a coluna "estacionado" for zero e a coluna "viajando" tiver um valor alto, como nos terminais 10 e 18, isso mostra que o ônibus saiu do estacionamento e esteve em movimento durante todo o período registrado.

Esses dados oferecem uma visão clara de quanto tempo os ônibus passam nos estacionamentos em comparação com o tempo em que estão em movimento. Ao final, eles foram agrupados devido a essa classificação e a variável "Número de Viagens" foi criada, representando as viagens que o ônibus realiza diariamente. No total, eram 11 viagens, assim, o rótulo varia de 0 a 10.

![4](https://github.com/anamabri/dgm-2023.2/assets/35360195/849e4a4b-d5fa-4036-92c5-899cccd2c24d)

### Modelos
![modelos](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/2eb2ceaa-7c84-4e36-b395-ae39800176a8)

Neste projeto, exploramos arquiteturas como as Redes Generativas Adversariais (GANs) e os Autoencoders Variacionais (VAEs) para a geração de dados sintéticos. Após extensivos experimentos, observamos que os modelos GANs ofereceram os melhores resultados em termos de precisão e realismo na síntese de dados. Portanto, não apresentamos resultados específicos com VAEs. 

### Workflow
https://miro.com/app/board/uXjVMjWZwUU=/?share_link_id=277061908932

## Experimentos, Resultados e Discussão dos Resultados
* Para todos os modelos as Epochs: 500

### Experimentos e Resultados


#### Modelo 1: MLP (Perceptron Multicamada)
* Camadas:
Gerador e Discriminador com apenas
camadas MLP com regularização L2.
* Otimizadores:
Adam
* Funções de Perda:
Entropia Cruzada Binária

##### Grafico de Velocidade vs Tempo (Dados Sintéticos)

![modelo4](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/5e9a8c08-3755-4763-983a-fe4f34884e12)

Conjunto sequencial de gráficos de velocidade versus tempo gerados pelo Modelo 1

#### Modelo 2: LSTM + GRU
* Camadas:
Gerador e Discriminador com LSTM
+ GRU e regularização L2.
* Otimizadores:
Adam
* Funções de Perda:
Erro Quadrático Médio (MSE)
Entropia Cruzada Binária

##### Grafico de Velocidade vs Tempo (Dados Sintéticos)
![modelo5](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/4251ec10-ef8a-4360-98a8-dc5fcab18b5f)


Conjunto sequencial de gráficos de velocidade versus tempo gerados pelo Modelo 2


#### Modelo 3: Conv1D
* Camadas:
Gerador e Discriminador com Convolucionais e
regularização L2.
* Otimizadores:
Adam y RMSprop
* Funções de Perda:
Entropia Cruzada Binária

##### Grafico de Velocidade vs Tempo (Dados Sintéticos)
![modelo6](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/8dcca7a2-11a0-4438-afd3-b0b1df3d777a)

Conjunto sequencial de gráficos de velocidade versus tempo gerados pelo Modelo 3


#### Modelo 4: MLP + LSTM + GRU
* Camadas:
MLP + Bi(LSTM) + GRU e
regularização L2.
* Otimizadores:
Adam
* Funções de Perda:
Erro Quadrático Médio
(MSE)
Entropia Cruzada Binária

##### Grafico de Velocidade vs Tempo (Dados Sintéticos)

![modelo3 (1)](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/07e85a61-52b0-447d-8810-31b1dbc832de)

Conjunto sequencial de gráficos de velocidade versus tempo gerados pelo Modelo 4


##### Gráficos de Velocidade de Dados reales

![velocidad real](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/6c3038b2-dc43-411b-94b8-9cd7cd607bba)

Os gráficos oferecem uma representação visual do comportamento da velocidade em três viagens distintos do ônibus durante um dia. Cada período horário reflete a maneira como cada motorista aborda o trajeto, evidenciado pela variação nas cores dentro da imagem. A suavidade das curvas na velocidade indica que a aceleração e desaceleração do ônibus são graduais, sem mudanças bruscas. Esse enfoque resulta na ausência de picos extremos na velocidade, mantendo-se em uma faixa suave entre 0 km/h quando o veículo está parado até o valor máximo de 60 km/h quando está em movimento. Esses gráficos proporcionam uma compreensão visual da dinâmica da viagem em diferentes momentos o dia. 


#### Gráfico de Perda do Gerador vs Discriminador
* Últimas perdas ao longo de épocas
  ![Loss140](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/b88bb0e7-ecf2-49dc-9a17-b2a97463bf5f)

###### Perda D (azul): 
Esta perda mostra uma tendência de estabilização com pequenas flutuações à medida que o número de épocas aumenta. Inicia com alguns picos iniciais e, em seguida, parece convergir para um valor consistente.
###### Perda G (vermelha):
A perda generativa tem um comportamento muito mais volátil com picos significativos e quedas. Embora haja uma tendência geral de diminuição ao longo das épocas, as flutuações são notáveis e há períodos de aumento repentino na perda.

* Últimas perdas carregadas ao longo de épocas
![Loss200](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/6cd79426-cdf7-487e-bdfb-8efa085c1328)

###### Perda D (azul): 
Semelhante à primeira gráfica, a perda discriminatória parece ter menos variabilidade e tende a estabilizar à medida que as épocas avançam, com alguns picos no final.
###### Perda G (vermelha): 
Nesta gráfica, a perda generativa mostra um comportamento ainda mais errático e volátil do que na primeira imagem. Os picos são muito pronunciados, especialmente no final, indicando possíveis problemas de estabilidade ou convergência no processo de treinamento.

#### Discussão e limitações: 

* Ao comparar os gráficos de dados reais e sintéticos da série temporal de velocidade, observamos diferenças marcantes. Nos dados reais, a representação visual destaca a suavidade das curvas, indicando acelerações e desacelerações graduais do ônibus. No entanto, os dados sintéticos gerados pelo melhor modelo de GAN apresentam um comportamento distinto. A presença de picos na velocidade sugere uma maior variabilidade e eventos abruptos no trajeto sintético. Nota-se uma parada no final do percurso, mas a modelagem ainda não consegue distinguir claramente os padrões de viagem. Além disso, a ausência de curvas suaves contrasta com a fluidez observada nos dados reais.
* Uma limitação significativa observada foi a presença de dados de velocidades com sequências variáveis, o que apresentou desafios ao incorporar essas informações nas Redes Generativas Adversariais Profundas (GANs). Isso resultou em dificuldades para padronizar uma entrada única dos dados de velocidade na rede. Essa limitação destaca a complexidade inerente à variabilidade nas sequências de velocidade e aponta para a necessidade de estratégias mais robustas para lidar com essa diversidade.
*  A ausência de recursos computacionais adequados representou uma limitação crucial, limitando a capacidade de conduzir um grande número de treinamentos de modelos. Isso, por sua vez, pode ter impactado a exploração extensiva de arquiteturas e parâmetros. Este desafio computacional é uma consideração significativa ao avaliar os resultados, indicando a necessidade de recursos mais robustos para futuros projetos semelhantes.
(MLP + LSTM + GRU)

### Ferramentas a serem utilizadas.

- Google Drive / Armazenamento 
- R / Linguagem de programação
- Github / Control de Versões
- TensorFlow / Framework para DL
- Python / Linguagem de programação
- Laptop Toshiba i7-6th, 16 RAM, 1TB de SSD
- Laptop Dell-Inspiron i7-7th, 12 RAM, 512 SSD
- Laptop Dell G15 i7-13th, 16 RAM, 512 SSD
  
 ![ferramentas](https://github.com/teaching-FEEC/dgm-2023.2/assets/35360195/cf605275-688b-4996-bf34-35366088a6f9)

## Conclusões
* Este projeto abordou de forma experimental a geração de dados devido à escassez de bancos de dados abertos em mobilidade urbana e transporte, uma área chave para pesquisa. Nos concentramos em filtrar e classificar dados para assegurar sua qualidade e consistência, um passo crucial para qualquer estudo sério neste campo.
* Na nossa exploração de diferentes modelos, como MLP, LSTM, GRU e Conv1D, descobrimos aspectos únicos de cada um, mas os modelos de LSTM bidirecional realmente se destacaram. Sua capacidade de entender as relações temporais nos dados melhorou um pouco a geração de perfis de velocidade.
* Destaca-se a importância das arquiteturas para Síntese de Sinais no estudo de temas críticos como o transporte urbano. Os resultados não foram ótimos, no entanto, abrem caminho para futuras pesquisas e aplicações.
  
## Trabalho Futuro:

Para aprimorar objetivamente a avaliação dos modelos geradores de dados sintéticos, é necessário incorporar métricas de avaliação quantitativa e qualitativa. Isso permitirá uma análise mais rigorosa e precisa do desempenho dos modelos, indo além da interpretação subjetiva baseada nos gráficos presentes. Dado o atual estágio da pesquisa, é evidente a necessidade de explorar alternativas arquitetônicas. Uma estratégia promissora consiste na aplicação de Transformers, com ênfase especial nos mecanismos de atenção. Acreditamos que as camadas de atenção têm a capacidade de capturar de maneira mais eficaz padrões complexos e contextos temporais, permitindo assim lidar de maneira mais eficiente com a natureza dinâmica e multifacetada dos dados de mobilidade urbana. Essa abordagem não apenas resultaria em perfis de velocidade mais realistas, mas também os tornaria adaptáveis às nuances do comportamento do ônibus elétrico.


## Referências Bibliográficas
* [1] RPUBS - Cluster Analysis in R. (n.d.-b). https://rpubs.com/odenipinedo/cluster-analysis-in-R
* [2] Saxena, D. (2019, July 19). D-GAN: Deep Generative Adversarial Nets for Spatio-Temporal Prediction. arXiv.org. https://arxiv.org/abs/1907.08556
* [3] Hochreiter, S., & Schmidhuber, J"urgen. (1997). Long short-term memory. Neural Computation, 9(8), 1735–1780.
* [4] R. Fu, Z. Zhang and L. Li, "Using LSTM and GRU neural network methods for traffic flow prediction," 2016 31st Youth Academic Annual Conference of Chinese Association of Automation (YAC), Wuhan, China, 2016, pp. 324-328, doi: 10.1109/YAC.2016.7804912.
* [5] Zakir H. Farahmand, Konstantinos Gkiotsalitis, Karst T. Geurs, Predicting bus ridership based on the weather conditions using deep learning algorithms, Transportation Research Interdisciplinary Perspectives,
Volume 19, 2023, 100833, ISSN 2590-1982,https://doi.org/10.1016/j.trip.2023.100833.

