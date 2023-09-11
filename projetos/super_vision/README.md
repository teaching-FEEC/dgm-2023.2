# `Super-Resolução de Imagem Única`
# `Single Image Super-Resolution (SISR)`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 | Alexsandro Barros | 233768  | Eng. Eletricista|
 | Jonyelison Morais Alves | 123456  | Eng. Eletricista|

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
para altos valores de escala? Os trabalhos com CNNs focam na diminuição do erro quadrático médio (MSE) da imagem
resolvida. Os resultados apresentam altos valores de relação sinal-ruído de pico mas carecem 
de detalhes de alta frequência, de modo que são perceptualmente insatisfatórios.

É nesse contexto que se insere o uso das GANs para SISR, visto que as mesmas são uma ferramenta
poderosa na geração de imagens plausíveis com alta qualidade perceptual.

## Metodologia Proposta
> Para a primeira entrega, a metodologia proposta deve esclarecer:
> * Qual(is) base(s) de dado(s) o projeto pretende utilizar, justificando a(s) escolha(s) realizadas.

Ao pesquisar referências nos deparamos com algumas base de dados bastante citadas dentro do contexto de
super-resolução como a CelebA e Unplash, usadas para treinamento de modelos, a BSD e a Set14 , usadas para
validação, por fim, a base de dados biológica para super-resolução microscópica BioSR. 

    - CelebA: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
    - BSD: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
    - Set14: https://huggingface.co/datasets/eugenesiow/Set14
    - Unsplash: https://www.kaggle.com/datasets/quadeer15sh/image-super-resolution-from-unsplash
    - BioSR: https://figshare.com/articles/dataset/BioSR/13264793

> * Quais abordagens de modelagem generativa o grupo já enxerga como interessantes de serem estudadas.

Inicialmente as GANs são as mais utilizadas no contexto de Super Resolution, a ideia seria explorar novas arquiteturas e métodos de treinamento, além de expandir os métodos de validação da qualidade das imagens.

> * Artigos de referência já identificados e que serão estudados ou usados como parte do planejamento do projeto

    - Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (Christian Ledig, 2017)
    - Image Super-Resolution Using Deep Convolutional Networks  (Chao Dong, 2014)
    - ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks (Xintao Wang, 2018)
    - Evaluation and development of deep neural networks for image super-resolution in optical microscopy (Chang Qiao, 2021)
    - Deep Neural Networks for Image Super-Resolution in Optical Microscopy by Using Modified Hybrid Task Cascade U-Net (Dawei Gong, 2021)

> * Ferramentas a serem utilizadas:

Neste início de projeto, elencamos as seguintes ferramentas:
> |Ferramenta | Descrição|
> |--|--|
> | [Google Colab](https://colab.research.google.com/) | Ferramenta para elaboração dos notebooks e códigos em linguagem Python 3.8 |
> | [Pytorch](https://pytorch.org/) | Ferramenta principal de manipulação de tensores e construção da GAN |
> | [Seaborn](https://seaborn.pydata.org/) | Ferramenta para visualização de dados |

> * Resultados Esperados:

Conforme elucidado na sessão de descrição do projeto, o resultado principal esperado é uma imagem de 
saída de alta resolução a partir da imagem de entrada de baixa resolução. Assim, ao final do projeto, 
espera-se que o modelo seja capaz de realizar a tarefa de SISR com um grau de qualidade aceitável, sendo
aplicado a cenários do mundo real, como por exemplo em imagens médicas de microscopia. 

> * Proposta de avaliação dos resultados de síntese

Além das métricas tradicionais, como PSNR e o índice de similaridade estrutural (Structural Similarity Index Measure - SSIM), pretendemos explorar técnicas de avaliação visual, como o julgamento humano por meio de estudos de avaliação de qualidade de imagem e tentar trazer uma abordagem que leve em consideração a
densidade de pixels (ppi) do display no qual a imagem será visualizada. 

## Cronograma
> Proposta de cronograma:
>
> |Atividade  | Descrição | Tempo estimado|
> |--|--|--|
> | Entendimento do Problema | Análise do problema e busca de artigos para encontrarmos uma boa metodologia a para a síntese de timbre instrumental  | 16/03 a 06/04 (3 semanas)|
> | Entendimento dos Dados  | Busca e avaliação dos dados necessários para o projeto   | 06/04 a 20/04 (2 semanas)|
> | Entrega E1  | Discussão, formalização e elaboração do *commit* da E1 no Github do projeto | 20/04 a 27/04 (1 semana) |
> | Finalização de Leitura  | Finalização da leitura dos artigos selecionados | 11/09 a 17/09 (1 semana) |
> | SRGAN | Execução e tentativa de reprodução dos resultados da SRGAN. | 18/09 a 24/09 (1 semana) |
> | SRGAN | Execução e tentativa de reprodução dos resultados da SRGAN. | 03/10 a 10/10 (1 semana) |
> | Entrega E2 - Checkpoint  | Discussão, formalização e elaboração do *commit* da E2 no Github do projeto | 03/10 a 10/10 (1 semana) |
> | Análises dos Dados Sintetizados | Elaboração do código para a síntese, avaliação dos dados sintetizados e análises dos resultados | 11/05 a 08/06 (4 semanas) |
> | Finalização | Ajustes finais para a entrega do projeto e análise crítica dos resultados e suas contribuições | 08/06 a 15/06 (1 semana) |
> | Entrega E3 – Código Final  | Discussão, formalização e elaboração do *commit* da E3 no Github do projeto | 15/06 a 22/06 (1 semana) |
> | Entrega E4 – Apresentação do Projeto  | Discussão, formalização e elaboração do *commit* da E4 no Github do projeto | 22/06 a 06/07 (2 semanas) |

## Referências Bibliográficas

[1] [Dong, C., Loy, C. C., He, K., & Tang, X. (2015). Image Super-Resolution Using Deep Convolutional Networks. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1501.00092.pdf)

[2] [Ledig, C., Theis, L., Huszar, F., Caballero, J., Aitken, A. P., Tejani, A., Totz, J., Wang, Z., & Shi, W. (2016). Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1609.04802.pdf)

[3] [Wang, X., Yu, K., Wu, S., Gu, J., Liu, Y., Dong, C., Loy, C. C., Qiao, Y., & Tang, X. (2018). ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks. Computing Research Repository (CoRR).](https://arxiv.org/pdf/1809.00219.pdf)

[3] [Qiao, C., Li, D., Guo, Y., Liu, C., Jiang, T., Dai, Q., & Li, D. (2021). Evaluation and development of deep neural networks for image super-resolution in optical microscopy. Nature Methods 18 (pp. 194-202)](https://www.nature.com/articles/s41592-020-01048-5)

[4] [Gong, D., Ma, T., Evans, J., He, S. (2021). Deep Neural Networks for Image Super-Resolution in Optical Microscopy by Using Modified Hybrid Task Cascade U-Net. Progress In Electromagnetics Research, Vol. 171, 185–199.](https://www.jpier.org/issues/volume.html?paper=21110904)