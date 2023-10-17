# `Síntese de Imagens de Lesões de Pele`
# `Synthesis of Skin Lesions Images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Especialização|
 |--|--|--|
 | Thiago Soares Laitz  | 224898  | Eng. Eletricista |
 | Vinícius Hirono Gonçalves  | 188182  | Eng. Eletricista |


## Resumo (Abstract)
 O projeto consiste em explorar formas de data augmentation para imagens de lesões de pele utilizando GANs, com o objetivo de melhorar a precisão dos modelos de classificação. Para isso, utilizaremos o dataset HAM10000, disponível no Kaggle, que contém 10015 imagens de lesões de pele, classificadas em 7 classes. Os modelos explorados serão a ACGAN e a ProGAN, que têm mostrado resultados promissores em tarefas de síntese de imagens.


## Descrição do Problema/Motivação


## Objetivo


## Metodologia Proposta


### Bases de Dados e Evolução


### Workflow


## Experimentos, Resultados e Discussão dos Resultados
Foram realizados experimentos envolvendo a GAN tradicional na geração de imagens sintéticas para o HAM10000, com o objetivo de verificar a viabilidade da abordagem. Os resultados qualitativos obtidos foram satisfatórios visualmente para as classes com uma boa quantidade de imagens disponíveis (+1000), porém houve uma grande dificuldade em gerar dados sintéticos para os dados com menos exemplos. Além disso, a fim de validar o código criado para a ACGAN, foi criado um notebook que implementa o modelo para a base de dados MNIST, uma vez que a variabilidade entre as classes pode ser facilmente identificada. 

![Mnist samples generated using ACGAN](reports/figures/mnist/images_mnist_acgan.jpg)

Por fim, podemos identificar que durante o treinamento da ACGAN para a base MNIST, o gerador sofreu com o fenômeno colapso de modo. A hipótese inicial é que devido ao grande número de camadas utilizadas na rede geradora, ocorreu overfitting nos dados, fazendo com que a rede discriminadora facilmente identificasse os dados sintéticos.

(...)

## Conclusão


## Referências Bibliográficas
- Odena, Augustus, Christopher Olah, and Jonathon Shlens. "Conditional image synthesis with auxiliary classifier gans." International conference on machine learning. PMLR, 2017.
- Karras, Tero, et al. "Progressive growing of gans for improved quality, stability, and variation." arXiv preprint arXiv:1710.10196 (2017).
