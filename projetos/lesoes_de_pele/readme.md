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
 Apesar da crescente disponibilidade de conjuntos de dados públicos de alta qualidade, a escassez de amostras de dados médicos de treinamento ainda é um dos principais desafios do deep learning para análise de lesões na pele. Redes Generativas Adversariais (GANs) surgem como uma hipótese para data augmentation, com a esperança de criar amostras que são praticamente indistinguíveis de dados reais porém sem a preocupação com a quebra de sigilo médico.

## Objetivo
Descobrir se usar data augmentation a partir de uma ACGAN ou ProGAN é capaz de melhorar o estado da arte na classificação de imagens de lesões de pele do dataset HAM10000.

## Metodologia Proposta
Treinar ACGANs e ProGANs em um dataset isolado de cada tipo de lesão de pele. Gerar novas imagens usando os modelos treinados. Treinar um classificador usando o dataset aumentado e comparar sua precisão ao classificador treinado com o dataset original.

### Bases de Dados e Evolução
HAM10000, processado em .jpg 64x64 64int, guardado no Git. 
checkpoint da ACGAN e PROGAN treinadas, guardadas no Drive local Google Colab + backup no Git (pasta reports/figures).

### Workflow
Find related work - créditos a professora Sandra Ávila pelo auxílio nessa tarefa.

Experiments - treinar a ACGAN e a PROGAN no dataset HAM10000, retreinar o classificador com o dataset aumentado.

Discussion - comentar e modificar parâmetros de treinamento das GANs, comentar e modificar o número de imagens aumentadas ao dataset, procurar entender a precisão do classificador encontrada. 

Conclusion - editar o registro da metodologia e resultados de forma didática.

## Experimentos, Resultados e Discussão dos Resultados
Foram realizados experimentos envolvendo a GAN tradicional na geração de imagens sintéticas para o HAM10000, com o objetivo de verificar a viabilidade da abordagem. Os resultados qualitativos obtidos foram satisfatórios visualmente para as classes com uma boa quantidade de imagens disponíveis (+1000), porém houve uma grande dificuldade em gerar dados sintéticos para os dados com menos exemplos. Além disso, a fim de validar o código criado para a ACGAN, foi criado um notebook que implementa o modelo para a base de dados MNIST, uma vez que a variabilidade entre as classes pode ser facilmente identificada. 

![Mnist samples generated using ACGAN](reports/figures/mnist/images_mnist_acgan.jpg)

Por fim, podemos identificar que durante o treinamento da ACGAN para a base MNIST, o gerador sofreu com o fenômeno colapso de modo. A hipótese inicial é que devido ao grande número de camadas utilizadas na rede geradora, ocorreu overfitting nos dados, fazendo com que a rede discriminadora facilmente identificasse os dados sintéticos.

 A seguir, exploramos a aplicação da PROGAN usando o conjunto de dados HAM10000. Mais uma vez, os resultados foram satisfatórios em termos visuais para as classes que dispunham de uma quantidade significativa de imagens (mais de 1000 exemplos) para o treinamento da rede. No entanto, enfrentamos desafios semelhantes ao utilizar a PROGAN para as classes com menos exemplos, destacando a complexidade de gerar dados sintéticos precisos nessas circunstâncias.

(---)

## Conclusão
(---)

## Referências Bibliográficas
- Odena, Augustus, Christopher Olah, and Jonathon Shlens. "Conditional image synthesis with auxiliary classifier gans." International conference on machine learning. PMLR, 2017.
- Karras, Tero, et al. "Progressive growing of gans for improved quality, stability, and variation." arXiv preprint arXiv:1710.10196 (2017).
- GAN-based data augmentation and anonymization for skin-lesion analysis: A critical review | Sandra Avila. https://www.ic.unicamp.br/~sandra/publication/2021-bissoto-isic-cvprw/. Acessado 23 de outubro de 2023.
