<h1 align="center">Mobilidade Urbana</h1>

![Mobilidade Urbana projet](https://github.com/anamabri/dgm-2023.2/assets/35360195/266daa3b-55e3-49e6-a182-d4f2a9f957f2)



<h3>Tópicos</h3>

* [Membros do projeto](#membros-do-projeto)
* [Descrição do projeto](#descrição-do-projeto)
* [Classificação das Variáveis](#classificação-das-variáveis)
* [Metodologia](#metodologia)
* [Cronologia](#crono)
* [Video](#video)
* [Referencias Bibliográficas](#biblio)

<h2 id="membros-do-projeto">Membros do Projeto</h2>

| Nome          | RA     | Curso           |
| ------------- | ------ | --------------- |
| Ana Briones (Github owner)| 272309 | Mestrado em Elétrica    |
| Miguel Gaybor  | 252040 | Mestrado em Elétrica    |
| Johsac Gomez   | 216401 | Doutorado em Elétrica   |

<h2 id="descrição-do-projeto">Descrição do Projeto</h2>
Este projeto tem como foco a geração sintética de dados de velocidade, altitud, giroscópio, acelerometro, magnetometro, temperatura e humidade, para ônibus utilizando modelos de redes generativas baseados em coordenadas GPS. O objetivo é abordar a escassez de conjuntos de dados abertos para pesquisa e desenvolvimento em mobilidade urbana e transporte. Esses dados sintéticos fornecerão uma alternativa de privacidade e segurança, reduzindo a necessidade de coleta de dados físicos intensiva em recursos e permitindo a criação de cenários diversos não disponíveis nos dados do mundo real. Ao mesmo tempo, nossa abordagem reduzirá o impacto ambiental associado à coleta de dados, promovendo um desenvolvimento sustentável na área. Os dados sintéticos gerados serão valiosos para testar algoritmos, simular ambientes e aprimorar aplicativos orientados por dados relacionados a ônibus, contribuindo para o avanço da mobilidade urbana.

<h2 id="classificação-das-variáveis">Classificação das Variáveis</h2>

| Variáveis  | Clasificação         |
| ------------- | ------------------|
| Velocidad     |     Inerciais     |
| Acelerômetro  |     Inerciais     |
| Giroscópio    |     Orientação    |
| Magnetômetro  |     Orientação    |
| Altitude      |     Ambientais    |
| Temperatura   |     Ambientais    |
| Umidade       |     Ambientais    |


<h2 id="metodologia">Metodologia</h2>

### Qual(is) base(s) de dado(s) o projeto pretende utilizar, justificando a(s) escolha(s) realizadas. 
 Os dados propostos a serem sintetizados fazem parte do banco de dados de monitoramento do Ônibus Elétrico na Unicamp (2021-2022), dado que 2 membros fazem parte do projeto, o que permitirá a inclusão de mais perfis com outros tipos de ônibus, sejam eles convencionais ou elétricos.

### Quais abordagens de modelagem generativa o grupo já enxerga como interessantes de serem estudadas.
Realizar uma análise estatística em cada etapa da geração de dados sintéticos, a fim de fornecer ao modelo de Deep Learning dados mais processados que permitam uma melhor captura da relação entre as variáveis. Serão utilizadas técnicas estatísticas descritivas, análises inferenciais e séries temporais, para posteriormente empregar GANs ou VAEs.

### Artigos de referência já identificados e que serão estudados ou usados como parte do planejamento do projeto.
trajGANs: Using generative adversarial networks for geo-privacy protection of trajectory data

### Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

- Google Colab / IDE Web
- Github / Control de Versões
- Pytorch / Framework
- Python / Linguagem de programação

### Resultados esperados
Criar um conjunto de dados ou subconjunto dos dados originais que permitam, com base em variáveis como GPS (latitude e longitude), estimar outras variáveis como giroscópio ou acelerômetro. Isso possibilitará a simulação ou teste de diferentes tipos de veículos.

### Proposta de avaliação dos resultados de síntese
 -Avaliações quantitativas, como MSE (Erro Quadrático Médio), MAE (Erro Absoluto Médio) e Diferença entre Distribuições.
 -Avaliações qualitativas, como EDA (Análise Exploratória de Dados)."

<h2 id="crono">Cronologia</h2>
![cronograma](https://github.com/anamabri/dgm-2023.2/assets/35360195/358967d8-7535-4848-bc4f-5e6875b63c25)

<h2 id="video">Link do Video Explicativo</h2>
https://drive.google.com/drive/folders/1VLP9w0TCstcMAjTkvByVzGRkTCJU73R5?usp=sharing

<h2 id="biblio">Referencias Bibliográficas</h2>
Liu, X., Chen, H., & Andris, C. (2018). trajGANs : Using generative adversarial networks for geo-privacy protection of trajectory data ( Vision paper ).
