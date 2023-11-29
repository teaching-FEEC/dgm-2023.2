# `Super-Resolução de Imagem Única`
# `Single Image Super-Resolution (SISR)`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 | Alexsandro Barros | 233768  | Eng. Eletricista|
 | Jonyelison Morais Alves | 231473  | Eng. Eletricista|

## Descrição Resumida do Projeto

Este projeto tem como objetivo a implementação e avaliação de Redes Gerativas Adversariais, GANs, na
super-resolução de imagem única (Single Image Super-Resolution - SISR). A tarefa principal consiste
no mapeamento direto da imagem de baixa resolução para a imagem de saída de alta resolução.

> Motivação: 

A recuperação de imagens de alta resolução a partir de imagens de baixa resolução é uma questão
clássica em visão computacional. Aplicações se estedem em diversas áreas como sistemas de
segurança, imagens médicas, sistemas de fotografia, entre outras. A super-resolução é inerentemente um
problema mal-posto ("ill-posed"), visto que múltiplas soluções existem para cada pixel da imagem de baixa
resolução, ou seja, é um problema inverso indeterminado para o qual a solução não é única.  

Apesar dos avanços em velocidade e acurácia de SISR usando redes neurais convolucionais profundas (CNNs), um
problema central ainda permanece não resolvido: como recuperar os detalhes finos de textura quando resolvendo
para altos valores de escala? Os trabalhos com CNNs focam na diminuição do erro quadrático médio (MSE) da imagem resolvida. Os resultados apresentam altos valores de relação sinal-ruído de pico mas carecem 
de detalhes de alta frequência, de modo que são perceptualmente insatisfatórios. Abaixo é possível ver um comparativo entre diferentes abordagens para a resolução do problema: 

![sisr](references/sisr_img.png?raw=True "SISR")
Fonte: *Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (Christian Ledig, 2016)*

É nesse contexto que se insere o uso das GANs para SISR, visto que as mesmas são uma ferramenta
poderosa na geração de imagens plausíveis com alta qualidade perceptual.

## Metodologia Proposta

Ao pesquisar referências nos deparamos com algumas bases de dados bastante citadas dentro do contexto de
super-resolução como a VOC2012 e Unplash, usadas para treinamento de modelos, a BSD e a Set14 , usadas para
validação.

    - BSD: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
    - Set14: https://huggingface.co/datasets/eugenesiow/Set14
    - Unsplash: https://www.kaggle.com/datasets/quadeer15sh/image-super-resolution-from-unsplash
    - VOC2012: https://www.kaggle.com/datasets/gopalbhattrai/pascal-voc-2012-dataset

Visto que é o primeiro contato dos participantes do projeto com modelos gerativos, optou-se por explorar
o uso de GANs na tarefa de SISR a partir da reprodução, avaliação e comparação de resultados de arquiteturas
já difundidas na literatura da área. Os principais artigos que vão nortear o trabalho são: 

    - Image Super-Resolution Using Deep Convolutional Networks  (Chao Dong, 2014)
    - Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (Christian Ledig, 2016)
    - ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks (Xintao Wang, 2018)
    - Evaluation and development of deep neural networks for image super-resolution in optical microscopy (Chang Qiao, 2021)
    - Deep Neural Networks for Image Super-Resolution in Optical Microscopy by Using Modified Hybrid Task Cascade U-Net (Dawei Gong, 2021)

Objetiva-se iniciar os trabalhos a partir da implementação e avaliação da SRGAN com a base de dados VOC2012. Em seguida, deseja-se implementar a métrica LPIPS para melhorar a avaliação dos resultados, segue abaixo uma tabela com as métricas que serão utilizadas para avaliação dos resultados:

![metricas](references/metricas.png?raw=True "Métricas")

Neste início de projeto, elencamos as seguintes ferramentas a serem utilizadas:

|Ferramenta | Descrição|
|--|--|
| [Google Colab](https://colab.research.google.com/) | Ferramenta para elaboração dos notebooks e códigos em linguagem Python 3.8 |
| [Pytorch](https://pytorch.org/) | Ferramenta principal de manipulação de tensores e construção da GAN |
| [Seaborn](https://seaborn.pydata.org/) | Ferramenta para visualização de dados |

> * Resultados Esperados:

Conforme elucidado na sessão de descrição do projeto, o resultado principal esperado é uma imagem de 
saída de alta resolução a partir da imagem de entrada de baixa resolução. Assim, ao final do projeto, 
espera-se que o modelo seja capaz de realizar a tarefa de SISR com um grau de qualidade aceitável, sendo
aplicado a cenários do mundo real, como por exemplo em imagens médicas de microscopia. 

> * Proposta de avaliação dos resultados de síntese:

Além das métricas tradicionais na área, como PSNR e o índice de similaridade estrutural (Structural Similarity Index Measure - SSIM), pretendemos incorporar uma avaliação visual através de pesquisa
com os próprios colegas de turma, e tentar trazer uma abordagem que leve em consideração a
densidade de pixels (ppi) do display no qual a imagem será visualizada. 

## Base de Dados e Evolução

|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|BioSR | https://figshare.com/articles/dataset/BioSR/13264793 | Dataset de imagens de microscópio para super resolução, com mais de 2200 pares de baixa e alta resolução.|

Esse dataset mostrou ser mais complexo do que inicialmente planejavamos para o projeto, apesar de ser uma base de dados bem relevante devido a sua aplicação em microscopia, o tamanho dos arquivos e a complexidade de processamento das imagens torna o dataset inviável para o escopo do projeto. O dataset está dividido em tipos de estruturas biológicas, como por exemplo Retículo Endoplasmático e Microtúbulos. Além disso, no artigo de referência é utilizado outra arquitetura chamada DFGAN (Deep Fourier GAN) que não é o foco do projeto, por isso optamos por utilizar outra base de dados para o projeto.

|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|Unsplash | https://www.kaggle.com/datasets/quadeer15sh/image-super-resolution-from-unsplash | Dataset pré processado com imagens em alta resolução e depixeladas em três níveis |

Imagens em jpg, que facilitam o processamento e a manipulação. Todas as imagens ja possuem versões depixeladas em 3 níveis: 2x, 4x e 6x. Possui 1254 imagens únicas e 3762 imagens depixeladas, totalizando 1.1 GB. Abaixo segue o exemplo de uma das imagens e suas variações de resolução:

*Imagem Original*
![1000](references/1000.jpg?raw=True "1000")

*2x*
![1000_2](references/1000_2.jpg?raw=True "1000_2")

*4x*
![1000_4](references/1000_4.jpg?raw=True "1000_4")

*6x*
![1000_6](references/1000_6.jpg?raw=True "1000_6")

## Workflow
Nesta seção, apresentamos o workflow do projeto, conforme ilustrado na figura abaixo, utilizamos a arquitetura original da SRGAN como base para o projeto, onde utilizamos os datasets VOC 2012 e Unsplash para treinamento do modelo. A partir dos resultados obtidos com a SRGAN utilizamos as métricas SSIM, PSNR e adicionamos LPIPS como contribuição para o trabalho.

![workflow](references/workflow.png?raw=True "Workflow")

Arquitetura da SRGAN

![arch](references/arch_srgan.png?raw=True "Arquitetura da SRGAN")

## Experimentos, Resultados e Discussão dos Resultados

> Experimentos:

Utilizamos como referência dois repositórios encontrados no Github para a implementação da SRGAN, onde os mesmos disponibilizam os datasets utilizados para treinamento e os modelos pré treinados para avaliação dos resultados. Os repositórios são:
    
    1. SRGAN: https://github.com/leftthomas/SRGAN
    2. SRGAN-PyTorch: https://github.com/Lornatang/SRGAN-PyTorch

Enfretamos alguns problemas com a obtenção dos datasets utilizados pelo primeiro repositório (SRGAN leftthhomas), por ser implementado por um time chinês, os links de download foram disponibilizados em uma ferramenta chinesa que se mostrou bastante inacessível, após algumas pesquisas e dificuldade com velocidade baixa de donwload foi possível obter o dataset VOC 2012.

Essa implementação funcionou bem para o dataset VOC 2012, porém ao utilizar o dataset Unsplash, o modelo não convergiu e apresentou resultados ruins. Para o treinamento, utilizamos os valores de hiperparametros definidos no artigo, Learning Rate 1e-5, para os dois casos de treinamento, VOC2012 e Unsplash. Tivemos que ajustar o Batch Size por conta do tamanho do dataset Unsplash ser bem menor que o VOC2012, onde utilizamos 16 para o Unsplash e 64 para o VOC2012. O treinamento foi realizado em uma máquina local com GPU Nvidia RTX 3060 Ti e em uma máquina virtual com Nvidia T4, onde o tempo de treinamento foi de aproximadamente 6 horas para o dataset Unsplash e 16 horas para o dataset VOC2012 na máquina local e 1 hora para o dataset Unsplash e 6 horas para o dataset VOC2012 na máquina virtual. Nos dois casos fizemos o downscale em 4 vezes o tamanho da imagem original e o treinamento ocorreu em 100 épocas.

Enquanto os problemas de download aconteciam com o primeiro repositório, encontramos o segundo repositório (SRGAN-PyTorch Lornatang), onde o download dos datasets foi bem mais simples pois são disponibilizados scripts shell no próprio repositório. Com isso foi possível executar um teste inicial com os datasets  e Set5 onde obtivemos PSNR 30.6708 e SSIM 0.8626, utilizando os modelos pré treinados que também são disponibilizados no repositório. Tentamos iniciar o treinamento localmente e verificar os resultados obtidos ao utilizar os datasets que encontramos, porém o treinamento não iniciou por algum problema no código e seguimos com o primeiro.

> Resultados:

Após o treinamento, obtivemos os seguintes resultados para o dataset VOC2012:

![voc2012](references/voc2012_training.png?raw=True "VOC2012")

Para o dataset Unsplash:

![unsplash](references/unsplash_training.png?raw=True "Unsplash")

> Discussão dos Resultados:

Para o benchmark dos resultados obtidos com os dois modelos treinados com os datatests VOC2012 e Unsplash, foi utilizado um conjunto de imagens dos datasets BSD100, Set5, Set14 e Urban100, facilitando a comparação entre os dois. Percebe-se que pelo tamanho do dataset VOC2012 ser 10 vezes maior que o Unsplash, a média geral de resultados ficou muito melhor e podemos analisar a LPIPS que indica a similaridade entre a imagem original e a imagem super resolvida, perceptivelmente se assemelha ao que analisamos ao observar as imagens, onde quanto menor o LPIPS melhor a qualidade.
Abaixo temos um exemplo de imagem que foi super resolvida utilizando os dois modelos e com valores próximos da média geral:

![table_imag1](references/table_img1.png?raw=True "Tabela Imagem 1")
![img1](references/img1.png?raw=True "Imagem 1")

Nessa segunda imagem podemos perceber que por se tratar de uma imagem com texturas mais complexas, ambos os modelos tiveram dificuldades para lidar com a componente de alta frequência.

![table_imag1](references/table_img2.png?raw=True "Tabela Imagem 2")
![img1](references/img2.png?raw=True "Imagem 2")

> Conclusões:

Por fim, o trabalho realizou o que se propôs a fazer, conseguimos implementar e avaliar a SRGAN utilizando o modelo disponibilizado pelo leftthomas, além disso adicionamos a métrica LPIPS que representa melhor a percepção visual do sistema humano em comparação com a SSIM. Percebemos que imagens com maior conteúdo de alta frequência (textura) são mais difíceis de serem super resolvidas independente do dataset utilizado para treinamento, tanto com o VOC2012 com mais de 16 mil imagens em 480p como o Unsplash com menos de 2 mil imagens em 1080p.
Para trabalhos futuros, segurimos testar a implementação da utilização da LPIPS na função de perda e atualizar a arquitetura da GAN para ESRGAN ou Real-ESRGAN. Além de fazer um estudo de hiperparâmetros utilizando ferramentas de tracking como MLFlow.

## Cronograma
> Proposta inicial de cronograma:
>
|Atividade  | Descrição | Tempo estimado|
|--|--|--|
| Entrega E1 | Discussão, formalização e elaboração da proposta de projeto (E1) | 11/09 |
| Finalização de Leitura | Finalização da leitura dos artigos selecionados | 11/09 a 17/09 (1 semana) |
| Ambiente de Experimentos | Setup do ambiente de experimentos | 18/09 a 24/09 (1 semana) |
| SRGAN pt.1 | Execução e tentativa de reprodução dos resultados da SRGAN. | 25/09 a 01/10 (1 semana) |
| SRGAN pt.2 | Avaliação dos dos resultados da SRGAN. | 02/10 a 08/10 (1 semana) |
| DFGAN pt.1 | Início da reprodução/execução do modelo DFGAN | 09/10 a 15/10 (1 semana) |
| Entrega E2 | Discussão, formalização e elaboração da E2 no Github do projeto | 16/10 a 18/10 (3 dias) |
| DFGAN pt.2 | Continuação dos trabalhos com a DFGAN e levantamento de resultados | 19/10 a 29/10 (1 semama e meia) |
| MHTCUN pt.1 | Início da reprodução/execução do modelo MHTCUN | 30/10 a 05/11 (1 semama) |
| MHTCUN pt.2 | Levantamento de resultados do modelo MHTCUN | 06/11 a 12/11 (1 semama) |
| Análises dos Dados Sintetizados | Avaliação dos dados sintetizados e análises dos resultados | 13/11 a 19/11 (1 semana) |
| Finalização | Ajustes finais para a entrega do projeto e análise crítica dos resultados | 20/11 a 24/11 (4 dias) |
| Entrega E3 – Código Final  | Discussão, formalização e elaboração do *commit* da E3 no Github do projeto | 25/11 a 26/11 (2 dias) |

## Referências Bibliográficas

[1] [Dong, C., Loy, C. C., He, K., & Tang, X. (2015). Image Super-Resolution Using Deep Convolutional Networks. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1501.00092.pdf)

[2] [Ledig, C., Theis, L., Huszar, F., Caballero, J., Aitken, A. P., Tejani, A., Totz, J., Wang, Z., & Shi, W. (2016). Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1609.04802.pdf)

[3] [Wang, X., Yu, K., Wu, S., Gu, J., Liu, Y., Dong, C., Loy, C. C., Qiao, Y., & Tang, X. (2018). ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1809.00219.pdf)

[3] [Qiao, C., Li, D., Guo, Y., Liu, C., Jiang, T., Dai, Q., & Li, D. (2021). Evaluation and development of deep neural networks for image super-resolution in optical microscopy. Nature Methods 18 (pp. 194-202)](https://www.nature.com/articles/s41592-020-01048-5)

[4] [Gong, D., Ma, T., Evans, J., He, S. (2021). Deep Neural Networks for Image Super-Resolution in Optical Microscopy by Using Modified Hybrid Task Cascade U-Net. Progress In Electromagnetics Research, Vol. 171, 185–199.](https://www.jpier.org/issues/volume.html?paper=21110904)
