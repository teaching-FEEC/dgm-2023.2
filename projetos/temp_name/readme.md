# `Geração de Dados de EEG`
# `EEG Data Augmentation`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação IA376L - Deep Learning aplicado à Síntese de Sinais, oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Especialização|
> |--|--|--|
> | Alexandre Herrero Matias  | 223665  | Eng. de Computação|
> | Maria Julia De Castro Villafranca Garcia | 183575  | Eng. Elétrica|


## Descrição Resumida do Projeto
<!--
> Descrição do tema do projeto, incluindo contexto gerador, motivação.
> Descrição do objetivo principal do projeto.
> Esclarecer qual será a saída do modelo generativo.
> Incluir nessa seção link para vídeo de apresentação da proposta do projeto (máximo 5 minutos).
-->

Eletroencefalograma (EEG) são sinais que registram, aproximadamente, a atividade do córtex cerebral. Os sinais são medidos em microvolts possuindo como frequência, principalmente, Delta, Theta, Alpha ou Beta, como exemplificado abaixo.

![Descrição Resumida do Projeto](./references/eeg_freqs.png)

Junto de técnicas de inteligência artificial, a aplicabilidade de tais dados é vasta. Dentro do âmbito tipo MI (*motor imagery*), tais dados de EEG permite com que pessoas com paralizia severa possam desenhar [7], para tratar epilepsia [8] e, também para jogos [9] e uso de veículos [10].

Entretanto, o uso de sinais MI dentro de aprendizado profundo necessita de quantidades grandes de dados para que o modelo seja treinado. Junto disso, a coleta desse tipo de dado em laboratório pode ser exaustivo para o paciente, a ponto de prejudicar a qualidade dos dados obtidos. 

Nesse sentido, a proposta do projeto visa obter um modelo generativo de sinais de eletroencefalograma (EEG), sob uma classe/categoria específica. 

Uma apresentação em vídeo da proposta pode ser acessada [aqui](https://www.youtube.com/)

## Metodologia Proposta
<!--
> Para a primeira entrega, a metodologia proposta deve esclarecer:
> * Qual(is) base(s) de dado(s) o projeto pretende utilizar, justificando a(s) escolha(s) realizadas.
> * Quais abordagens de modelagem generativa o grupo já enxerga como interessantes de serem estudadas.
> * Artigos de referência já identificados e que serão estudados ou usados como parte do planejamento do projeto
> * Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).
> * Resultados esperados
> * Proposta de avaliação dos resultados de síntese
-->

### Bases de Dados

Utilizando como referência alguns artigos ([1]-[3]), os conjuntos de dados utilizados variam, sendo similares, entretanto, em terem os sinais já separados por classes. Seja por emoção (SEED V, [1]), por objeto (EEG-image, [5]) ou do tipo *motor imagery* (MOABB, [6]). 

Para o treinamento, inicialmente, escolheremos um ou mais conjuntos de dados do MOABB [6], pois...

### Abordagens de Modelagem Generativa e Artigos de Referência


- [1] Usou DDPM (*denoising diffusion probabilistic model*) para a geração de dados EEG, à partir de EFDMs (*electrode-frequency distribution*) do *dataset* SEED V rotulados com base nas emoções *sad* (triste) e *happy* (feliz).

- [2] Trás um comparativo da geração de sinais de EEG através de 5 GANs com diferentes arquiteturas. O artigo trás a aplicação de métricas interessantes para a avaliação dos dados gerados frente aos dados originais.

- [3] Usou uma conditional TTS-WGAN-GP (transformer-encoder-based generator and discriminator for time series - TTS) com a informação adicional de *input* (rótulos) sendo a condição das amostras de EEG; *win* ou *lose*, mais informção no conjunto de dados vide [4].

### Ferramentas
À princípio, as ferramentas que serão utilizadas serão: 

- [Pytorch](https://pytorch.org/)
- [Pytorch Lightning](https://lightning.ai/)
- [TorchMetrics](https://torchmetrics.readthedocs.io/en/stable/)
- Notebook interfaces ([GoogleColab](https://colab.google/), [JupyterLab](https://jupyter.org/))


### Resultados Esperados e Propostas de Avaliação
Como resultado final, esperamos um modelo generativo capaz de gerar dados sintéticos de EEG (séries temporais), trazendo resultados práticos similares aos obtidos com os dados reais, porém se atendendo para uma pergunta pertinente na geração de dados sintéticos: "O modelos proposto está gerando novos dados ou simplemente replicando as amostras do dado original?" [1].

Para avaliar tais dados propõem-se, inicialmente, as seguintes métricas:

| Métrica | Referência |
| --- | --- |
| TSTR (*Train on Synthetic, Test on Real*) | [3] |
| TRTR (*Train on Real, Test on Real*) | [3] |
| Inception score (IS) | [2] |
| Frechet Inception Distance (FID) | [2] |
| Euclidean distance | [2] |
| Sliced Wasserstein distance | [2] |
| Acurácia de classificação | [1] |

## Cronograma
O cronograma proposto é uma estimativa temporal das principais etapas pelo projeto. Ademais, junto marcamos os *checkpoints* previstos para guiar e lembrar-nos das entregas e da geração das *release tags*.

![Cronograma](./references/cronograma.png)

## Referências Bibliográficas

[1] Tosato, G., Dalbagno, C. M., & Fumagalli, F. (2023). EEG Synthetic Data Generation Using Probabilistic Diffusion Models. arXiv preprint arXiv:2303.06068.

[2] Hartmann, K. G., Schirrmeister, R. T., & Ball, T. (2018). EEG-GAN: Generative adversarial networks for electroencephalographic (EEG) brain signals. arXiv preprint arXiv:1806.01875.

[3] Williams, C. C., Weinhardt, D., Wirzberger, M., & Musslick, S. (2023). Augmenting EEG with Generative Adversarial Networks Enhances Brain Decoding Across Classifiers and Sample Sizes. In Proceedings of the Annual Meeting of the Cognitive Science Society (Vol. 45, No. 45).

[4] Williams, C. C., Ferguson, T. D., Hassall, C. D., Abimbola, W., & Krigolson, O. E. (2021). The ERP, frequency, and time–frequency correlates of feedback processing: Insights from a large sample study. Psychophysiology, 58(2), e13722.

[5] Spampinato, C., Palazzo, S., Kavasidis, I., Giordano, D., Souly, N., & Shah, M. (2017). Deep learning human mind for automated visual classification. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 6809-6817).

[6] Jayaram, V., & Barachant, A. (2018). MOABB: trustworthy algorithm benchmarking for BCIs. Journal of neural engineering, 15(6), 066011.

[7] Münßinger, J. I., Halder, S., Kleih, S. C., Furdea, A., Raco, V., Hösle, A., & Kübler, A. (2010). Brain painting: first evaluation of a new brain–computer interface application with ALS-patients and healthy volunteers. Frontiers in neuroscience, 4, 182.

[8] Gadhoumi, K., Lina, J. M., Mormann, F., & Gotman, J. (2016). Seizure prediction for therapeutic devices: A review. Journal of neuroscience methods, 260, 270-282.

[9] Marshall, D., Coyle, D., Wilson, S., & Callaghan, M. (2013). Games, gameplay, and BCI: the state of the art. IEEE Transactions on Computational Intelligence and AI in Games, 5(2), 82-99.

[10] Zhuang, J., & Yin, G. (2017, July). Motion control of a four-wheel-independent-drive electric vehicle by motor imagery EEG based BCI system. In 2017 36th Chinese Control Conference (CCC) (pp. 5449-5454). IEEE.
