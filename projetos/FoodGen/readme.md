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

O projeto usará a base de dados Food-101, que pode ser acessada em https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/, feita por Lukas Bossard, Matthieu Guillaumin, Luc Van Gool. Essa base contém 1000 imagens para cada uma das 101 categorias presentes na base, totalizando então 101000 imagens. Por estar bem organizada, documentada e anotada, deve conter um número adequado de imagens para treinar uma rede geradora. Adicionalmente, as bases de dados Food-11 (16643 imagens anotadas) e ChineseFoodNet (185628 imagens) também serão usadas para adicionar mais imagens caso necessário.

Caso o conjunto das três bases não seja suficiente, serão abordadas técnicas de *few-shot learning*, ou seja, aprendizado com poucas amostras de treinamento.

As redes CookGAN, StyleGAN3 e cGAN foram identificadas como boas inspirações para o projeto. Todas elas geram imagens fotorrealistas de alimentos e usam a estrutura de GAN.

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

###Trabalhos relacionados:
CookGAN: Meal Image Synthesis from Ingredients, de Fangda Han, Ricardo Guerrero, Vladimir Pavlovic (https://openaccess.thecvf.com/content_WACV_2020/papers/Han_CookGAN_Meal_Image_Synthesis_from_Ingredients_WACV_2020_paper.pdf)
Conditional Synthetic Food Image Generation, de Wenjin Fu1, Yue Han, Jiangpeng He, Sriram Baireddy, Mridul Gupta, Fengqing Zhu (https://arxiv.org/pdf/2303.09005.pdf)
Food Image Generation using A Large Amount of Food Images with Conditional GAN: RamenGAN and RecipeGAN, de Yoshifumi Ito Wataru Shimoda Keiji Yanai (http://img.cs.uec.ac.jp/pub/conf18/180715shimok2_0.pdf)

###Datasets:
Food-101 – Mining Discriminative Components with Random Forests, de Lukas Bossard, Matthieu Guillaumin, Luc Van Gool (https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
Food-11 (https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/)
ChineseFoodNet, de Chen, Xin and Zhou, Hua and Zhu, Yu and Diao, Liang (https://sites.google.com/view/chinesefoodnet/)
