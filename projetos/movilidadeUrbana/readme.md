<h1 align="center">Mobilidade Urbana</h1>

![Mobilidade Urbana projet](https://github.com/anamabri/dgm-2023.2/assets/35360195/266daa3b-55e3-49e6-a182-d4f2a9f957f2)


<h2 id="membros-do-projeto">Apresentação</h2>

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

| Nome          | RA     | Curso           |
| ------------- | ------ | --------------- |
| Ana Briones (Github owner)| 272309 | Mestrado em Elétrica    |
| Miguel Gaybor  | 252040 | Mestrado em Elétrica    |
| Johsac Gomez   | 216401 | Doutorado em Elétrica   |

<h2 id="resumo">Resumo (Abstract)</h2>
Este projeto utiliza a geração de dados sintéticos e coordenadas GPS para prever dados de velocidade ao longo do tempo e do espaço. Além das metodologias tradicionais de processamento de dados, ele incorpora uma avançada Rede Generativa Adversarial Profunda (DGAN) para aprimorar a qualidade dos dados sintéticos. A metodologia envolve a coleta abrangente de dados de ônibus da Universidade de Campinas, filtragem e rotulagem, com ênfase especial nos dados de 2022. A aplicação do DGAN contribui para conjuntos de dados sintéticos mais precisos e realistas, abordando a escassez de conjuntos de dados abertos para pesquisa em mobilidade urbana e transporte. Esses conjuntos de dados enriquecidos são inestimáveis para o estudo e a melhoria dos sistemas de transporte urbano, promovendo o desenvolvimento sustentável na área.


<h2 id="descrição-do-projeto">Descrição do Projeto</h2>
Nos projeto tem como foco a geração sintética de dados de velocidade, altitude, longitude e latitude para ônibus, utilizando modelos de redes generativas. O objetivo é lidar com a escassez de conjuntos de dados abertos para pesquisa e desenvolvimento em mobilidade urbana e transporte. Esses dados sintéticos fornecerão uma alternativa em termos de privacidade e segurança, reduzindo a necessidade de uma coleta intensiva de dados físicos e permitindo a criação de cenários diversos não disponíveis nos dados do mundo real. Ao mesmo tempo, nossa abordagem reduzirá o impacto ambiental associado à coleta de dados, promovendo o desenvolvimento sustentável na área. Os dados sintéticos gerados serão valiosos para testar algoritmos, simular ambientes e melhorar aplicativos baseados em dados relacionados a ônibus, contribuindo para o avanço da mobilidade urbana."



## Objetivos do Projeto

* Implementar técnicas avançadas de estatísticas de filtragem para remover dados irrelevantes, como dados de fora do horário de operação dos ônibus e instâncias de alta variabilidade.
* Gerar um conjunto de dados sintéticos abrangente de velocidade de ônibus que possa ser usado para o estudo e aprimoramento de sistemas de transporte urbano.
* Avaliar a eficácia do conjunto de dados sintéticos comparando-o com dados do mundo real e avaliando seu potencial para diversas aplicações na pesquisa de mobilidade urbana e transporte.

## Metodologia

Pré-processamento de Dados:

* Aplicar métodos estatísticos para filtrar os dados coletados e identificar instâncias de alta variabilidade, que podem incluir flutuações extremas de velocidade ou valores atípicos [1].

* Remover pontos de dados com variabilidade excessiva para garantir a qualidade e consistência do conjunto de dados.
* Eliminar pontos de dados que estão fora do horário operacional dos ônibus.
* Categorizar os pontos de dados em dois estados: "Estacionário" e "Em Movimento" para diferenciar os períodos em que o ônibus está parado e em trânsito. Isso fornece insights sobre as rotas e ajuda a distinguir entre os estados dos ônibus durante a análise de dados.


### Classificação das Variáveis

| Variáveis  | Clasificação         |
| ------------- | ------------------|
| Velocidad     |     Inerciais     |
| Longitude     |     Orientação    |
| Altitude      |     Orientação    |
| Latitude      |     Orientação    |

Geração de Dados Sintéticos:

*Empregar uma Rede Generativa Adversarial Profunda (DGAN) para gerar dados sintéticos de velocidade de ônibus. [2]
*Treinar o modelo DGAN utilizando os dados do mundo real pré-processados do ônibus elétrico da UNICAMP em 2022. Esse processo de treinamento permite que o modelo capture os padrões e relações subjacentes presentes nos dados reais.
*Gerar um conjunto de dados sintéticos abrangente. 

Validação:

* Avaliações quantitativas, como MSE (Erro Quadrático Médio), MAE (Erro Absoluto Médio) e Diferença entre Distribuições.
* Avaliações qualitativas, como EDA (Análise Exploratória de Dados).
* Validar a utilidade e realismo do conjunto de dados sintéticos comparando-o com um conjunto de dados do mundo real.

### Bases de Dados e Evolução


|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|Base de dados de Mobilidade Urbana | privada | Base de dados do Laboratorio Vivo de Mobilidade Urbana da UNICAMP. Dados coletados por dispositivos nos anos de 2021, 2022 e 2023.|

O ônibus da Universidade de Campinas (Unicamp) possui registros de dados coletados por dispositivos nos anos de 2021, 2022 e 2023. Decidiu-se tomar o ano de 2022 como ponto de referência, uma vez que nesse ano a pandemia já não estava presente e dados completos estavam disponíveis.

Em relação aos dados coletados em 2022, a maioria dos meses possui aproximadamente um milhão de registros, sendo os meses de maio e agosto os que apresentam maior frequência. Além disso, há um arquivo que registra o início e o fim de cada viagem. Como resultado, determinou-se que o conjunto de dados inicial para conduzir experimentos seria o correspondente ao mês de maio de 2022, uma vez que é o mês que registra a maior quantidade de viagens e contém um grande número de registros.
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

Esses dados oferecem uma visão clara de quanto tempo os ônibus passam nos estacionamentos em comparação com o tempo em que estão em movimento.

![4](https://github.com/anamabri/dgm-2023.2/assets/35360195/849e4a4b-d5fa-4036-92c5-899cccd2c24d)



### Workflow
https://miro.com/app/board/uXjVMjWZwUU=/?share_link_id=824147713133

### Ferramentas a serem utilizadas.

- Google Colab / IDE Web
- Github / Control de Versões
- Pytorch / Framework
- Python / Linguagem de programação



## Referências Bibliográficas
[1] RPUBS - Cluster Analysis in R. (n.d.-b). https://rpubs.com/odenipinedo/cluster-analysis-in-R
[2]Saxena, D. (2019, July 19). D-GAN: Deep Generative Adversarial Nets for Spatio-Temporal Prediction. arXiv.org. https://arxiv.org/abs/1907.08556

