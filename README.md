# Projeto de Manutenção Preditiva com Machine Learning

# Descrição

Este projeto tem como objetivo desenvolver um modelo de Machine Learning para prever falhas em máquinas industriais a partir de dados de sensores. Foram aplicadas técnicas de preparação dos dados, balanceamento das classes, padronização das variáveis e treinamento de dois algoritmos de classificação: K-Nearest Neighbors (KNN) e Random Forest.

O desenvolvimento foi realizado em Python utilizando bibliotecas voltadas para análise de dados e aprendizado de máquina.

# Objetivo

Construir um modelo capaz de identificar a ocorrência de falhas em máquinas industriais, comparando o desempenho dos algoritmos KNN e Random Forest.

# Base de Dados

O conjunto de dados contém informações de sensores industriais, incluindo:

1-Tipo da máquina
2-Temperatura do ar
3-Temperatura do processo
4-Velocidade de rotação
5-Torque
6-Desgaste da ferramenta
7-Potência
8-Variável alvo: falha_maquina

# Etapas do Projeto

O projeto foi desenvolvido seguindo as seguintes fases:

-Importação das bibliotecas
-Carregamento da base de dados
-Limpeza e preparação dos dados
-Separação das variáveis preditoras e variável alvo
-Divisão entre treinamento e teste
-Balanceamento das classes com SMOTE
-Padronização dos dados (apenas para o KNN)
-Treinamento do modelo KNN
-Treinamento do modelo Random Forest
-Comparação dos modelos

# Tecnologias Utilizadas
-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
-Scikit-learn
-Imbalanced-learn (SMOTE)
-Jupyter Notebook

# Resultados Obtidos
Modelo	Melhor Parâmetro	Acurácia
KNN	K = 3	90,55%
Random Forest	max_depth = None	94,30%

# Conclusão

Os dois modelos apresentaram bom desempenho na previsão de falhas em máquinas industriais.

O modelo Random Forest obteve a melhor performance, alcançando 94,30% de acurácia, enquanto o modelo KNN atingiu 90,55%.

A utilização do balanceamento com SMOTE contribuiu para reduzir o desequilíbrio entre as classes durante o treinamento, tornando o aprendizado mais eficiente.

Com base nos resultados obtidos, a Random Forest foi o algoritmo que apresentou maior capacidade de classificação para este conjunto de dados.


# Estrutura do Projeto

Avaliacao_modulo1/
│
├── .venv/
├── data/
│   └── manutencao_preditiva.csv
│
├── graficos/
│
├── imagens/
│   ├── hist_temperatura.png
│   ├── boxplot_torque.png
│   └── distribuicao_falha.png
│
├── main.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

# Como Executar

Clone este repositório:
git clone https://github.com/Dora-bit767/avaliacao-modulo1-manutencao-preditiva.git
Acesse a pasta do projeto:
cd avaliacao-modulo1-manutencao-preditiva
Instale as dependências:
pip install -r requirements.txt
Execute o notebook no Jupyter Notebook ou Visual Studio Code.

 # Autora

Auxiliadora Silvino Arce

Curso: Fundamentos de Dados, Programação e Análise Preditiva com Python

Projeto desenvolvido como atividade avaliativa do curso.
