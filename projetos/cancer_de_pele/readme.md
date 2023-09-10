# `Síntese de Imagens de Lesões de Pele`
# `Synthesis of Skin Lesions Images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Especialização|
> |--|--|--|
> | Thiago Soares Laitz  | 224898  | Eng. Eletricista |
> | Vinícius Hirono Gonçalves  | 188182  | Eng. Eletricista |


## Descrição Resumida do Projeto
> O projeto consiste em explorar formas de data augmentation para imagens de lesões de pele, com o objetivo de melhorar a precisão dos modelos de classificação. O principal objetivo é gerar imagens sintéticas a partir de modelos generativos, como GANs, e avaliar o impacto dessas imagens na acurácia do classificador.
> O modelo de classificação será treinado com imagens do dataset [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T), que contém 10015 imagens de lesões de pele, classificadas em 7 categorias.

> [Vídeo explicativo](https://drive.google.com/file/d/1ot6AAC68K9oxxHQCFKWLAgzKk4Kks_0m/view?usp=sharing)

## Metodologia Proposta
Para a primeira entrega do projeto, é fundamental que definamos com clareza a metodologia a ser seguida. Abaixo estão os pontos-chave que devem ser abordados:

>Base de Dados: O projeto pretende utilizar o conjunto de dados disponível no site Kaggle, especificamente o conjunto de dados HAM10000. Essa escolha se justifica pela relevância do dataset na área de detecção de lesões pigmentadas de pele.

Abordagens de Modelagem Generativa: Nesta fase inicial, o grupo já identificou as seguintes abordagens de modelagem generativa como interessantes de serem estudadas:

> Redes Generativas Adversariais (GANs): Inicialmente, pretendemos explorar as GANs, como a ACGAN (Auxiliary Classifier GAN) e a ProGAN (Progressive GAN), para a geração de imagens de câncer de pele. Essas arquiteturas têm mostrado resultados promissores em tarefas de síntese de imagens.

>Ferramentas: Para a implementação, o grupo planeja utilizar a linguagem Python, a biblioteca de aprendizado profundo PyTorch e as GPUs disponibilizadas pelo Google Colab.

>Resultados Esperados: Nesta fase inicial, esperamos concluir com sucesso a implementação das GANs para a síntese de imagens de lesões pigmentadas de pele. Os resultados esperados incluem a geração de imagens realistas que se assemelham a lesões de pele reais e a validação dessas imagens por meio de métricas de acurácia do classificar implementado. Para isso, treinaremos uma rede convolucional em duas situações: (1) dataset original e (2) dataset original + dados sintéticos.

## Cronograma
> Considerando 5 etapas de desenvolvimento, o cronograma proposto é o seguinte:
- Estudo bibliográfico e processamento dos dados: 1 semana
- Implementação das GANs: 6 semanas
- Treinamento e avaliação do classificador: 2 semanas
- Escrita do relatório: 1 semana

## Referências Bibliográficas
- Odena, Augustus, Christopher Olah, and Jonathon Shlens. "Conditional image synthesis with auxiliary classifier gans." International conference on machine learning. PMLR, 2017.
- Karras, Tero, et al. "Progressive growing of gans for improved quality, stability, and variation." arXiv preprint arXiv:1710.10196 (2017).
