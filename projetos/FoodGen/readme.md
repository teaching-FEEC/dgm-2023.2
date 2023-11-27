# `Gerador de fotos de alimentos`
# `Food pictures generator`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> | Rafael Pedrosa Silva Clerici  | 273034  | Eng. de Computação|

> | Marco Antonio Cáceres Choqque  | 239271  | Eng. de Sistemas|

> | Kevin Inofuente  | 272316  | XXX|

## Resumo (Abstract)

Este trabalho se propôs a gerar imagens convincentes de alimentos por meio de redes neurais gerativas. Para isso, várias redes diferentes foram utilizadas, principalmente GANs, e treinadas na base de dados Food101. Os resultados foram pouco satisfatórios, uma vez que as imagens geradas não chegaram a retratar alimentos existentes de forma convincente, no máximo imitando formas ou texturas relevantes.

## Descrição do Problema/Motivação

Restaurantes menores possuem menos recursos à disposição para fotografar seus pratos disponíveis e gerar boas imagens para anúncios e cardápios. Uma rede neural suficientemente treinada pode gerar as imagens necessárias sem o custo associado, permitindo competitividade aos restaurantes.
Em todo caso, a motivação principal do projeto foi o aprendizado por parte dos seus integrantes.
## Objetivo


Gerar imagens convincentes de alimentos.
-  Revisar a bibliografia em busca de trabalhos similares.
-  Testar várias arquiteturas de redes diferentes para verificar suas propriedades.
-  Ser capaz de gerar imagens fotorrealistas de alimentos.
## Metodologia

O projeto usará a base de dados Food-101, que pode ser acessada em https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/, feita por Lukas Bossard, Matthieu Guillaumin, Luc Van Gool. Essa base contém 1000 imagens para cada uma das 101 categorias presentes na base, totalizando então 101000 imagens. Por estar bem organizada, documentada e anotada, deve conter um número adequado de imagens para treinar uma rede geradora. Adicionalmente, as bases de dados Food-11 (16643 imagens anotadas) e ChineseFoodNet (185628 imagens) também serão usadas para adicionar mais imagens caso necessário.

Caso o conjunto das três bases não seja suficiente, serão abordadas técnicas de *few-shot learning*, ou seja, aprendizado com poucas amostras de treinamento.

As redes CookGAN, StyleGAN3 e cGAN foram identificadas como boas inspirações para o projeto. Todas elas geram imagens fotorrealistas de alimentos e usam a estrutura de GAN.

A principal ferramenta a ser utilizada é o Google Colaboratory, que permite o desenvolvimento online de notebooks python. Com ele, serão usadas as bibliotecas pytorch e pandas para processar a base de dados, criar e treinar a rede. Posteriormente, bibliotecas como numpy, matplot e seaborn serão usadas para produzir gráficos e outras ferramentas de análise.

Espera-se que a rede seja capaz de produzir imagens convincentes de comidas existentes, ou seja, que um humano consiga reconhecer como um prato. Porém, não se descarta a possibilidade de gerar imagens semelhantes a comidas reais, mas com detalhes anômalos, como coloração diferente do usual. Também há a possibilidade de gerar arranjos e pratos diferentes dos apresentados no grupo de treino.

Serão usadas técnicas tradicionais como caminhada pelo espaço latente e *drop-out* para verificar se a rede "aprendeu" mesmo ou se os resultados são cópias de imagens apresentadas durante o treinamento. Também será realizada uma avaliação humana, com voluntários avaliando as imagens com os seguintes critérios:
1. Semelhança com fotos reais (tentar adivinhar se a imagem foi gerada ou não)
2. Aparência da comida (se parece algo gostoso ou detestável)
3. Presença ou ausência de artefatos ou anomalias (borrões, cores estranhas)

### Bases de Dados e Evolução

|Base de Dados | Endereço na Web | Resumo descritivo|
|Food101 | https://huggingface.co/datasets/food101 | Base mais comum usada para alimentos. Possui 101 classes com 100 imagens cada. |
|Food11 | https://www.kaggle.com/datasets/trolukovich/food11-image-dataset | Base contendo 11 classes diferentes de alimentos.|
|Chinese Food Net | https://sites.google.com/view/chinesefoodnet/ | Base com mais de 200 classes e milhares de imagens de alimentos da culinária chinesa.|

Apesar de três redes serem selecionadas, apenas a Food101 foi usada no projeto. A Food11 não apresentou quantidade suficiente de imagens para treinamento, e o link de acesso para a ChineseFoodNet não está funcionando (contato foi tentado com o mantenedor do site, sem sucesso).

A Food101 apresenta uma boa quantidade de imagens, mas também uma grande variedade. Essa variedade advém de suas muitas classes de alimentos e das condições de iluminação, ângulo e preparo dos alimentos retratados: desde imagens com boas condições e o prato claramente retratado em seu centro até imagens com outros objetos, má iluminação e diferença no arranjo dos ingredientes no prato. Acredita-se que isso tenha afetado o treinamento das IAs, necessitando mais tempo para aprender a recriar a diversidade retratada.

## Experimentos, Resultados e Discussão dos Resultados

Como experimentos, vários treinos foram realizados com diferentes modelos de IAs gerativas. O código delas pode ser lido no diretório de Notebooks. No caso, foram duas redes neurais do tipo GAN e duas de Difusão. Para verificar a qualidade das imagens geradas, foi observada a função _loss_ em conjunto com uma análise visual de amostras do espaço latente.

Os resultados obtidos de nenhuma das redes chegou a produzir imagens convincentes de alimentos, sendo capazes de apenas replicar cores ou texturas de forma um tanto abstrata (avaliação visual por parte dos desenvolvedores do projeto). Acredita-se que isso tenha ocorrido devido à baixos tempos de treinamento e capacidade de processamento disponível. Assim, nem todas as métricas descritas na metodologia foram empregadas para avaliar as redes: dado que imagens fotorrealistas não foram produzidas, não se achou necessário verificar _overfitting_ nas redes testadas.

Curiosamente, a primeira GAN usada, uma simples arquitetura convolucional, produziu estranhos artefatos conforme o gerador teve mais tempo para treinar. É possível que isso seja uma espécie de mínimo local, onde a imagem ruidosa causa problemas para o discriminador. Foram feitos experimentos treinando o gerador mais vezes que o discriminador, mas isso intensificou a presença de artefatos.

A segunda GAN usada, a Progressive GAN, precisou de mais tempo para treinar e alcançar resultados semelhantes à outra GAN, mas produziu imagens em uma resolução maior e sem artefatos.

Os dois modelos de difusão exigiram muita memória e processamento do computador utilizado para treiná-los, e os resultados se resumem a ruído indistinto.

## Conclusão

Os resultados do experimento não alcançaram o nível esperado. Porém, foram uma boa oportunidade de aprendizado para os integrantes do projeto. Várias redes foram analizadas, utilizadas e avaliadas, oferecendo melhor compreensão das técnicas e desafios enfrentados na pesquisa de redes neurais.
O projeto se beneficiaria de uma extensão, especialmente se mais recursos computacionais pudessem ser utilizados, uma vez que as imagens geradas ficaram aquém do esperado por, muito provavelmente, falta de treino para as redes: os integrantes do projeto não possuíam acesso a máquinas poderosas o suficiente para realizar os cálculos necessários.

## Referências Bibliográficas
###Trabalhos relacionados:
CookGAN: Meal Image Synthesis from Ingredients, de Fangda Han, Ricardo Guerrero, Vladimir Pavlovic (https://openaccess.thecvf.com/content_WACV_2020/papers/Han_CookGAN_Meal_Image_Synthesis_from_Ingredients_WACV_2020_paper.pdf)
Conditional Synthetic Food Image Generation, de Wenjin Fu1, Yue Han, Jiangpeng He, Sriram Baireddy, Mridul Gupta, Fengqing Zhu (https://arxiv.org/pdf/2303.09005.pdf)
Food Image Generation using A Large Amount of Food Images with Conditional GAN: RamenGAN and RecipeGAN, de Yoshifumi Ito Wataru Shimoda Keiji Yanai (http://img.cs.uec.ac.jp/pub/conf18/180715shimok2_0.pdf)

###Datasets:
Food-101 – Mining Discriminative Components with Random Forests, de Lukas Bossard, Matthieu Guillaumin, Luc Van Gool (https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
Food-11 (https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/)
ChineseFoodNet, de Chen, Xin and Zhou, Hua and Zhu, Yu and Diao, Liang (https://sites.google.com/view/chinesefoodnet/)

###Redes usadas:
Progressive GAN - PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION, de Tero Karras, Timo Aila, Samuli Laine e Jaakko Lehtinen (https://research.nvidia.com/sites/default/files/pubs/2017-10_Progressive-Growing-of/karras2018iclr-paper.pdf)
