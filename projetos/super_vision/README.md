# `Geração de Imagens em Super Resolução`
# `Super Resolution Image Generation`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 | Alexsandro Barros | 233768  | Eng. Eletricista|
 | Jonyelison Morais Alves | 123456  | Eng. Eletricista|

## Descrição Resumida do Projeto
> Descrição do tema do projeto, incluindo contexto gerador, motivação.

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

> Descrição do objetivo principal do projeto.

Desenvolver um modelo generativo baseado em GANs que seja capaz de aumentar a resolução de imagens.
Avaliar a eficácia do modelo gerado usando métricas de qualidade de imagem.

> Esclarecer qual será a saída do modelo generativo.

A partir de uma imagem de baixa resolução como entrada, a saída principal do modelo será uma imagem de alta resolução mantendo todos os componentes presente na imagem original, ou seja, uma versão mais nítida.

> Incluir nessa seção link para vídeo de apresentação da proposta do projeto (máximo 5 minutos).

## Metodologia Proposta
> Para a primeira entrega, a metodologia proposta deve esclarecer:
> * Qual(is) base(s) de dado(s) o projeto pretende utilizar, justificando a(s) escolha(s) realizadas.

Ao pesquisar referências nos deparamos com alguns datasets bastante citados para validação de modelos generativos para super resolution, como o BSD e Set14, para treinamento encontramos datasets genéricos (Unsplash) e um específico para imagens de microscópio (BioSR) que pode ser utilizado como principal resultado gerado em vez de imagens genéricas.

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

> * Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

    - PyTorch: Biblioteca fundamental para implementação
    - GPU: Hardware para acelerar o treinamento do modelo, possibilitando um maior tempo de exploração de arquiteturas e hiperparâmetros

> * Resultados esperados

Espera-se ter um modelo generativo (baseado em GANs ou outras abordagens) treinado com sucesso para aprimorar a resolução de imagens de baixa qualidade. Pretende-se aplicar o modelo gerado a cenários do mundo real, demonstrando sua utilidade, como por exemplo, utilizando o banco de dados de imagens microscópicas ou para upscaling de fotos de câmera.

> * Proposta de avaliação dos resultados de síntese

Além das métricas tradicionais, como PSNR e SSIM, pretendemos explorar técnicas de avaliação visual, como o julgamento humano por meio de estudos de avaliação de qualidade de imagem e tentar trazer uma abordagem relacionando a densidade de pixels (ppi) no display e a imagem sendo visualizada.

## Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.

## Referências Bibliográficas
> Apontar nesta seção as referências bibliográficas adotadas no projeto.