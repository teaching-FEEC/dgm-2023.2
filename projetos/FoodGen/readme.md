# `Gerador de fotos de alimentos`
# `Food pictures generator`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


|            Name               |    RA    |    Graduação       |
| ----------------------------  | -------  | -----------------  |
|Rafael Pedrosa Silva Clerici   |   273034 | Eng. de Computação |
|Marco Antonio Cáceres Choqque  |   239271 | Eng. de Sistemas   |
|Kevin Inofuente Colque         |   272316 | Eng. Eletrônica    |

  
## Resumo (Abstract)

Este trabalho se propôs a gerar imagens convincentes de alimentos por meio de redes neurais gerativas. Para isso, várias redes diferentes foram utilizadas, principalmente GANs e modelos basados em difussion process, e treinadas na base de dados Food101. Os resultados foram moderadamente satisfatórios, mas as imagens geradas não chegaram a retratar alimentos existentes de forma convincente, no máximo imitando formas ou texturas relevantes.

## Descrição do Problema/Motivação

Restaurantes menores possuem menos recursos à disposição para fotografar seus pratos disponíveis e gerar boas imagens para anúncios e cardápios. Uma rede neural suficientemente treinada pode gerar as imagens necessárias sem o custo associado, permitindo competitividade aos restaurantes.
Em todo caso, a motivação principal do projeto foi o aprendizado por parte dos seus integrantes.
## Objetivo


Gerar imagens convincentes de alimentos.
-  Revisar a bibliografia em busca de trabalhos similares.
-  Analise diferentes conjuntos de dados da literatura.
-  Testar várias arquiteturas de redes diferentes para verificar suas propriedades.
-  Ser capaz de gerar imagens fotorrealistas de alimentos.
## Metodologia

O projeto usa a base de dados Food-101, que pode ser acessada em https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/, feita por Lukas Bossard, Matthieu Guillaumin, Luc Van Gool. Essa base contém 1000 imagens para cada uma das 101 categorias presentes na base, totalizando então 101000 imagens. Por estar bem organizada, documentada e anotada, deve conter um número adequado de imagens para treinar uma rede geradora. Adicionalmente, as bases de dados Food-11 (16643 imagens anotadas) e ChineseFoodNet (185628 imagens) também foram estudadas.

Caso o conjunto das três bases não seja suficiente, serão abordadas técnicas de *few-shot learning*, ou seja, aprendizado com poucas amostras de treinamento.

As redes CookGAN, StyleGAN3 e cGAN foram identificadas como boas inspirações para o projeto. Todas elas geram imagens fotorrealistas de alimentos e usam a estrutura de GAN.

A principal ferramenta utilizada é o Google Colaboratory, que permite o desenvolvimento online de notebooks python. Com ele, serão usadas as bibliotecas pytorch e pandas para processar a base de dados, criar e treinar a rede.

Espera-se que a rede seja capaz de produzir imagens convincentes de comidas existentes, ou seja, que um humano consiga reconhecer como um prato. Porém, não se descarta a possibilidade de gerar imagens semelhantes a comidas reais, mas com detalhes anômalos, como coloração diferente do usual. Também há a possibilidade de gerar arranjos e pratos diferentes dos apresentados no grupo de treino.

Serão usadas técnicas tradicionais como caminhada pelo espaço latente e *drop-out* para verificar se a rede "aprendeu" mesmo ou se os resultados são cópias de imagens apresentadas durante o treinamento. Também será realizada uma avaliação humana, com voluntários avaliando as imagens com os seguintes critérios:
1. Semelhança com fotos reais (tentar adivinhar se a imagem foi gerada ou não)
2. Aparência da comida (se parece algo gostoso ou detestável)
3. Presença ou ausência de artefatos ou anomalias (borrões, cores estranhas)

### Bases de Dados e Evolução

|**Base de Dados** | **Endereço na Web**                                                  | **Resumo descritivo**|
| ---------------  | -------------------------------------------------------------------  | -------------------  |
|Food101           | https://huggingface.co/datasets/food101                              | Base mais comum usada para alimentos. Possui 101 classes com 100 imagens cada. |
|Food11            | https://www.kaggle.com/datasets/trolukovich/food11-image-dataset     | Base contendo 11 classes diferentes de alimentos.|
|Chinese Food Net  | https://sites.google.com/view/chinesefoodnet/                        | Base com mais de 200 classes e milhares de imagens de alimentos da culinária chinesa.|

Apesar de três bases serem estudadas, apenas a Food101 foi usada no projeto. A Food11 não apresentou quantidade suficiente de imagens para treinamento, e o link de acesso para a ChineseFoodNet não está funcionando (contato foi tentado com o mantenedor do site, sem sucesso).

A Food101 apresenta uma boa quantidade de imagens, mas também uma grande variedade. Essa variedade advém de suas muitas classes de alimentos e das condições de iluminação, ângulo e preparo dos alimentos retratados: desde imagens com boas condições e o prato claramente retratado em seu centro até imagens com outros objetos, má iluminação e diferença no arranjo dos ingredientes no prato. Acredita-se que isso tenha afetado o treinamento das IAs, necessitando mais tempo para aprender a recriar a diversidade retratada.

#### Exemplos de Food101
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/Examples%20of%20Food101%20dataset.png" style="float:left" width="540px">
</div>
  
#### Exemplos de Food11
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/Food11%20dataset.png" style="float:right" width="540px">
</div>

#### Exemplos de Chinese Food Net
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/ChineFood%20dataset.png" style="float:right" width="540px">
</div>

## Experimentos, Resultados e Discussão dos Resultados

Como experimentos, vários treinos foram realizados com diferentes modelos de IAs gerativas. O código delas pode ser lido no diretório de Notebooks. No caso, foram duas redes neurais do tipo GAN e duas de Difusão. Para verificar a qualidade das imagens geradas, foi observada a função _loss_ em conjunto com uma análise visual de amostras do espaço latente.

Os resultados obtidos de nenhuma das redes chegou a produzir imagens convincentes de alimentos, sendo capazes de apenas replicar cores ou texturas de forma um tanto abstrata (avaliação visual por parte dos desenvolvedores do projeto). Acredita-se que isso tenha ocorrido devido à baixos tempos de treinamento e capacidade de processamento disponível. Assim, nem todas as métricas descritas na metodologia foram empregadas para avaliar as redes: dado que imagens fotorrealistas não foram produzidas, não se achou necessário verificar _overfitting_ nas redes testadas.

Curiosamente, a primeira GAN usada, uma simples arquitetura convolucional, produziu estranhos artefatos conforme o gerador teve mais tempo para treinar. É possível que isso seja uma espécie de mínimo local, onde a imagem ruidosa causa problemas para o discriminador. Foram feitos experimentos treinando o gerador mais vezes que o discriminador, mas isso intensificou a presença de artefatos.

#### Arquitetura geral das camadas geradora e discriminadora
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/arquitectura__1.png" style="float:left" width="540px">
</div>

#### Arquitetura da camada do gerador
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/generador_1.png" style="float:left" width="540px">
</div>

#### Arquitetura da camada do discriminador
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/discriminador_1.png" style="float:left" width="540px">
</div>

#### Resultados da primeira arquitetura GAN

Realizamos muitas tentativas com a primeira GAN, mas decidimos mostrar os 6 resultados mais relevantes que ajudam a compreender e visualizar melhor o desempenho da nossa GAN. Para isso, é importante saber que temos 2 imagens para cada teste ou resultado; a primeira imagem exibe as curvas de perda do Gerador e do Discriminador em relação ao número de épocas, lembrando que a função de perda utilizada foi a BCE; a segunda imagem mostra alguns exemplos de imagens geradas pela primeira arquitetura GAN implementada, onde, na parte superior de cada imagem, estão os hiperparâmetros configurados para esse teste, enquanto na parte inferior de cada imagem é exibida a perda do Discriminador e do Gerador.

> Resultado 1

Para o primeiro resultado, utilizamos uma dimensão de vetor latente igual a 100 e uma taxa de aprendizado de 0,0005, com um total de 150 épocas. Isso resultou na primeira imagem parecendo um bom resultado, pois o custo do Discriminador estava próximo de zero, e o Gerador estava tentando subir. No entanto, ao observar a segunda imagem, percebe-se que as imagens geradas dos pratos são incomíveis, indicando que a geração não foi bem-sucedida.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result1_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result1_examples.png" style="float:left" width="540px">
</div>

> Resultado 2

No segundo resultado, o comportamento do gerador foi muito ruim. Isso ocorreu porque, embora tenhamos utilizado os mesmos hiperparâmetros do resultado 1, tentamos treinar o Gerador 5 vezes mais do que o Discriminador no resultado 2. Isso resultou em resultados incorretos tanto na primeira imagem de perdas quanto na segunda imagem de imagens geradas.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result2_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result2_examples.png" style="float:left" width="540px">
</div>

> Resultado 3 - O Primeiro Resultado Bom

Para o terceiro resultado, aumentamos a dimensão do vetor latente para 200, reduzimos as épocas para 50 e ajustamos a taxa de aprendizado para 0,0003. A escolha de 0,0003 para a taxa de aprendizado foi baseada na experimentação, pois Andrej Karpathy (Diretor de IA da Tesla) mencionou que um bom valor para a taxa de aprendizado ao usar o otimizador Adam é 0,0003. Assim, decidimos experimentar com esse valor, já que estávamos usando o otimizador Adam. Os resultados desta tentativa foram melhores do que os dois primeiros, não apenas na imagem de perdas, mas também na imagem de exemplo, pois pela primeira vez tínhamos exemplos gerados mais claros de pratos.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result3_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result3_examples.png" style="float:left" width="540px">
</div>

> Resultado 4 - Ruim, porque aumentamos a quantidade de épocas em 250 do teste 3.

Para o resultado 4, apenas aumentamos a quantidade de épocas, pois, como no resultado 3 havia dado um bom resultado, pensamos que aumentar a quantidade de épocas poderia melhorar. No entanto, não foi o caso. Na verdade, isso resultou em alguns resultados semelhantes aos da tentativa anterior, outros muito ruins, definitivamente representando pratos não apetitosos. Portanto, aumentar as épocas não funcionou para essa configuração de hiperparâmetros.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result4_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result4_examples.png" style="float:left" width="540px">
</div>

> Resultado 5 - Ruim, porque aumentamos a quantidade de épocas em 500 do teste 3.

En el caso del resultado número 5, mantivemos a mesma configuração utilizada nos testes 3 e 4, ou seja, Dimensão do Vetor Latente de 200 e Taxa de Aprendizado de 0,0003, alterando apenas a quantidade de épocas, aumentando para 500. Como esperado, o resultado não foi bom. Ao analisar a segunda imagem, percebe-se que as imagens geradas não fazem sentido e não representam pratos de comida. Na imagem 1, é possível observar que o resultado das perdas começou a falhar por volta das 380 épocas aproximadamente.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result5_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result5_examples.png" style="float:left" width="540px">
</div>

> Resultado 6 - O Segundo Resultado Bom

Para o teste número 6, os resultados foram bons, sendo assim nossos segundos resultados positivos. No entanto, se tivéssemos que comparar com os primeiros resultados positivos, então esses resultados do teste 6 seriam os melhores. Para alcançar esses bons resultados, utilizamos uma dimensão latente de 100, reduzimos a taxa de aprendizado para 0,0002 e também diminuímos a quantidade de épocas para 100. Com esses hiperparâmetros, as perdas do Gerador e do Discriminador são melhores do que nos outros casos, e as imagens geradas também parecem representar pratos comestíveis, ou pelo menos se assemelham a pratos reais.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result6_chart.png" style="float:left" width="540px">
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result6_examples.png" style="float:left" width="540px">
</div>

#### Segunda GAN utilizada

A segunda GAN usada, a Progressive GAN, precisou de mais tempo para treinar e alcançar resultados, mas produziu imagens em uma resolução maior e sem artefatos. Foi capaz de imitar cores e texturas, mas não gerou imagens convincentes de pratos com alimentos.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/arquitectura_2.png" style="float:left" width="540px">
</div>

A PGAN começa como uma GAN tradicional bem pequena, operando em imagens reduzidas e com poucas camadas. Depois, é progressivamente aumentada até a resolução e o número de camadas desejado. Isso permite grande economia de computação, uma vez que a maior parte das camadas será treinada com uma resolução menor. Isso pôde ser constatado durante o treinamento: as primeiras iterações foram realizadas muito mais rapidamente do que as últimas.

>Resultado 7 - Primeiro teste
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result7_examples.png" style="float:left" width="540px">
</div>

O sétimo resultado foi feito com os parâmetros recomendados da rede, e produziu imagens com padrões de texturas e cores semelhantes a alimentos reais, porém nada muito definido, se assemelhando a manchas derretidas. Foi usada uma _learning rate_ de 0,001, o que é maior que os outros casos de teste, e um período de 300.000 iterações.

>Resultado 8 - Alterando parâmetros
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result8_examples.png" style="float:left" width="540px">
</div>

No oitavo teste, alguns parâmetros foram alterados de acordo com o que foi aprendido com a GAN anterior. A _learning rate_ foi reduzida para 0,0003. Porém, devido ao longo tempo de treino, a quantidade de iterações também foi reduzida. Acredita-se que isso tenha alterado significativamente a qualidade dos resultados, uma vez que reduções na _learning rate_ tendem a exigir mais tempo de treino para alcançar resultados semelhantes.

#### Difusão

Os dois modelos utilizados são inspirados na UNet, um tipo bastante comum para análise de imagens. Ele tem esse nome por possuir uma estrutura onde camadas são gradualmente reduzidas e depois aumentadas, deixando um gargalo no meio, mas camadas posteriores ainda tem acesso às respostas das camadas anteriores à redução. Dessa forma, busca-se ter contato com detalhes em alto e baixo nível.

<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/arquitectura_2.png" style="float:left" width="540px">
</div>

Infelizmente, os dois modelos de difusão exigiram muita memória e processamento do computador utilizado para treiná-los, e os resultados se resumem a ruído indistinto. Cerca de 12 horas foram necessárias para treinar apenas 10 epochs da segunda rede de difusão, cujos resultados são apresentados abaixo, com um tamanho de batch bem pequeno, o que limitou a capacidade de realizar experimentos com elas.

>Resultado 9 - Ruído difuso
<div align="center">
<img src="https://raw.githubusercontent.com/Racdi/dgm-2023.2/main/projetos/FoodGen/readme_images/result9_examples.png" style="float:left" width="540px">
</div>

### Acessando as redes

As redes podem ser acessadas no diretório "notebooks". Os arquivos NetExtention e NetRecreation são variantes da primeira GAN, sendo que a segunda possui uma alteração para treinar o gerador mais vezes que o discriminador. O subdiretório Progressive-GAN-pytorch-master contém os arquivos da PGAN. Diffusion contém o código da primeira rede de difusão, baseada na rede de exemplo disponibilizada na disciplina. Por fim, Diffusion2 contém um modelo alternativo, ainda sim baseado na UNet, que foi mais treinado, mas igualmente sem sucesso.

## Conclusão

Os resultados do experimento não alcançaram o nível esperado. Porém, foram uma boa oportunidade de aprendizado para os integrantes do projeto. Várias redes foram analizadas, utilizadas e avaliadas, oferecendo melhor compreensão das técnicas e desafios enfrentados na pesquisa de redes neurais.
O projeto se beneficiaria de uma extensão, especialmente se mais recursos computacionais pudessem ser utilizados, uma vez que as imagens geradas ficaram aquém do esperado por, muito provavelmente, falta de treino para as redes: os integrantes do projeto não possuíam acesso a máquinas poderosas o suficiente para realizar os cálculos necessários.

## Referências Bibliográficas
### Trabalhos relacionados:
CookGAN: Meal Image Synthesis from Ingredients, de Fangda Han, Ricardo Guerrero, Vladimir Pavlovic (https://openaccess.thecvf.com/content_WACV_2020/papers/Han_CookGAN_Meal_Image_Synthesis_from_Ingredients_WACV_2020_paper.pdf)

Conditional Synthetic Food Image Generation, de Wenjin Fu1, Yue Han, Jiangpeng He, Sriram Baireddy, Mridul Gupta, Fengqing Zhu (https://arxiv.org/pdf/2303.09005.pdf)

Food Image Generation using A Large Amount of Food Images with Conditional GAN: RamenGAN and RecipeGAN, de Yoshifumi Ito Wataru Shimoda Keiji Yanai (http://img.cs.uec.ac.jp/pub/conf18/180715shimok2_0.pdf)

### Datasets:
Food-101 – Mining Discriminative Components with Random Forests, de Lukas Bossard, Matthieu Guillaumin, Luc Van Gool (https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)

Food-11 (https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/)

ChineseFoodNet, de Chen, Xin and Zhou, Hua and Zhu, Yu and Diao, Liang (https://sites.google.com/view/chinesefoodnet/)

### Redes usadas:
Progressive GAN - PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION, de Tero Karras, Timo Aila, Samuli Laine e Jaakko Lehtinen (https://research.nvidia.com/sites/default/files/pubs/2017-10_Progressive-Growing-of/karras2018iclr-paper.pdf)
