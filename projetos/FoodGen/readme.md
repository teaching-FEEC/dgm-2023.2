# `Gerador de fotos de alimentos`
# `Food pictures generator`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os grupos devem ter no máximo três integrantes.
> |Nome  | RA | Especialização|
> |--|--|--|
> | Rafael Pedrosa Silva Clerici  | 273034  | Eng. de Computação|
> | Nome2  | 123456  | XXX|
> | Nome3  | 123456  | XXX|


## Descrição Resumida do Projeto
> Descrição do tema do projeto, incluindo contexto gerador, motivação.
> Descrição do objetivo principal do projeto.
> Esclarecer qual será a saída do modelo generativo.
> 
> Incluir nessa seção link para vídeo de apresentação da proposta do projeto (máximo 5 minutos).

A proposta deste projeto é criar uma rede generativa capaz de gerar imagens convincentes de alimentos.

## Metodologia Proposta
> Para a primeira entrega, a metodologia proposta deve esclarecer:
> * Qual(is) base(s) de dado(s) o projeto pretende utilizar, justificando a(s) escolha(s) realizadas.
> * Quais abordagens de modelagem generativa o grupo já enxerga como interessantes de serem estudadas.
> * Artigos de referência já identificados e que serão estudados ou usados como parte do planejamento do projeto
> * Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).
> * Resultados esperados
> * Proposta de avaliação dos resultados de síntese

O projeto usará a base de dados Food-101, que pode ser acessada em https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/, feita por Lukas Bossard, Matthieu Guillaumin, Luc Van Gool. Essa base contém 1000 imagens para cada uma das 101 categorias presentes na base, totalizando então 101000 imagens. Por estar bem organizada, documentada e anotada, deve conter um número adequado de imagens para treinar uma rede geradora.

Caso não seja suficiente, serão abordadas técnicas de *few-shot learning*, ou seja, aprendizado com poucas amostras de treinamento.


<Artigos>

A principal ferramenta a ser utilizada é o Google Colaboratory, que permite o desenvolvimento online de notebooks python. Com ele, serão usadas as bibliotecas pytorch e pandas para processar a base de dados, criar e treinar a rede. Posteriormente, bibliotecas como numpy, matplot e seaborn serão usadas para produzir gráficos e outras ferramentas de análise.

Espera-se que a rede seja capaz de produzir imagens convincentes de comidas existentes, ou seja, que um humano consiga reconhecer como um prato. Porém, não se descarta a possibilidade de gerar imagens semelhantes a comidas reais, mas com detalhes anômalos, como coloração diferente do usual. Também há a possibilidade de gerar arranjos e pratos diferentes dos apresentados no grupo de treino.

Serão usadas técnicas tradicionais como caminhada pelo espaço latente e *drop-out* para verificar se a rede "aprendeu" mesmo ou se os resultados são cópias de imagens apresentadas durante o treinamento. Também será realizada uma avaliação humana, com voluntários avaliando as imagens com os seguintes critérios:
1. Semelhança com fotos reais (tentar adivinhar se a imagem foi gerada ou não)
2. Aparência da comida (se parece algo gostoso ou detestável)
3. Presença ou ausência de artefatos ou anomalias (borrões, cores estranhas)

## Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.

O projeto pode ser dividido em 6 etapas:

1. Setup do projeto e da hierarquia
   - 04/09 até 17/09
2. Leitura da base de dados e pré-processamento
   - 18/09 até 24/09
3. Estudo de artigos e escolha do método para geração
   - 25/09 até 08/10
4. Planejamento da arquitetura
   - 09/10 até 22/10
5. Treinamento
   - 23/10 até 05/11
6. Análise dos resultados
   - 06/11 até 19/11

## Referências Bibliográficas
> Apontar nesta seção as referências bibliográficas adotadas no projeto.

<Food-101>