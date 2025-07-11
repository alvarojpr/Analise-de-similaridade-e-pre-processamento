
import sys # Importa o módulo sys para forçar o programa a sair
import pandas as pd # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa a biblioteca Matplotlib para visualização de dados
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, Binarizer # Importa as classes de pré-processamento do scikit-learn

# Carregando os dados do arquivo CSV
data = pd.read_csv('./winequality-red.csv', sep=';')
# Definindo os nomes das colunas do DataFrame
data.columns = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']

# Visualizando as primeiras linhas do DataFrame
print(data.head())

# Padronização dos dados
print('Padronização dos dados')
# Cria um objeto StandardScaler para realizar a padronização
scaler = StandardScaler()
# Aplica a padronização aos dados, excluindo a última coluna (`quality`)
data_standard = scaler.fit_transform(data.iloc[:, :-1])
# Converte o array de volta para um DataFrame com as colunas originais
data_standard = pd.DataFrame(data_standard, columns=data.columns[:-1])
# Exibe as primeiras linhas do DataFrame padronizado
print(data_standard.head())

# Normalização MinMax dos dados
# Exibe a mensagem "Normalização MinMax"
print('Normalização MinMax')
# Cria um objeto MinMaxScaler para realizar a normalização MinMax
scaler = MinMaxScaler()
# Aplica a normalização MinMax aos dados, excluindo a última coluna (`quality`)
data_minmax = scaler.fit_transform(data.iloc[:, :-1])
# Converte o array de volta para um DataFrame com as colunas originais
data_minmax = pd.DataFrame(data_minmax, columns=data.columns[:-1])
# Exibe as primeiras linhas do DataFrame normalizado com MinMax
print(data_minmax.head())

# Normalização L2 dos dados
print('Normalização L2')
# Cria um objeto Normalizer para realizar a normalização L2
scaler = Normalizer()
# Aplica a normalização L2 aos dados, excluindo a última coluna (`quality`)
data_normalize = scaler.fit_transform(data.iloc[:, :-1])
# Converte o array de volta para um DataFrame com as colunas originais
data_normalize = pd.DataFrame(data_normalize, columns=data.columns[:-1])
# Exibe as primeiras linhas do DataFrame normalizado com L2
print(data_normalize.head())

# Binarização dos dados
print('Binarização')
# Cria um objeto Binarizer com um limite de 0.0
scaler = Binarizer(threshold=0.0)
# Binariza os dados, excluindo a última coluna (`quality`)
data_binarize = scaler.fit_transform(data.iloc[:, :-1])
# Converte o array de volta para um DataFrame com as colunas originais
data_binarize = pd.DataFrame(data_binarize, columns=data.columns[:-1])
# Exibe as primeiras linhas do DataFrame binarizado
print(data_binarize.head())

# Visualização
def histograma(): #pega as variaveis data_standard e data_minmax plota um histograma
    data_standard.hist()
    plt.show()
    data_minmax.hist()
    plt.show() # plota o histograma
    sys.exit()

def grafico_densidade():
    data_standard.plot(kind='kde') # kde = kernel density estimate
    plt.show()
    data_minmax.plot(kind='kde')
    plt.show()
    data_normalize.plot(kind='kde')
    plt.show()
    data_binarize.plot(kind='kde')
    plt.show()
    sys.exit()

def grafico_dispersao(): #pega as variaveis data_standard e data_normalize e plota um gráfico de caixa
    pd.plotting.scatter_matrix(data_standard, alpha=0.2)
    plt.show()
    pd.plotting.scatter_matrix(data_minmax, alpha=0.2)
    plt.show()
    pd.plotting.scatter_matrix(data_normalize, alpha=0.2)
    plt.show()
    pd.plotting.scatter_matrix(data_binarize, alpha=0.2)
    plt.show()
    sys.exit()

def grafico_caixa(): #pega as variaveis data_standard e data_normalize e plota um gráfico de caixa
    data_standard.plot(kind='box')
    plt.show()
    data_minmax.plot(kind='box')
    plt.show()
    data_normalize.plot(kind='box')
    plt.show()
    data_binarize.plot(kind='box')
    plt.show()
    sys.exit()

def grafico_linha(): #pega a variavel data_standard e plota um gráfico de linha
    data_standard.plot(kind='line') #kind = tipo de gráfico
    plt.show()
    data_minmax.plot(kind='line')
    plt.show()
    data_normalize.plot(kind='line')
    plt.show()
    data_binarize.plot(kind='line')
    plt.show()
    sys.exit()

def grafico_barra(): #pega a variavel data_standard e plota um gráfico de barra
    data_standard.plot(kind='bar') #kind = tipo de gráfico
    plt.show()
    data_minmax.plot(kind='bar')
    plt.show()
    data_normalize.plot(kind='bar')
    plt.show()
    data_binarize.plot(kind='bar')
    plt.show()
    sys.exit()

# Função default para opção inválida
def default():
    print("Opção inválida")

visualizador = {
    1: histograma,
    2: grafico_densidade,
    3: grafico_dispersao,
    4: grafico_caixa,
    5: grafico_linha,
    6: grafico_barra
}

# Solicita entrada do usuário
n = int(input("Escolha: \n1-Histograma   2-Grafico de densidade\n3-Grafico de dispersao   4-Grafico de caixa \n5-Grafico de linha   6-Grafico de barra: "))

# Executa a função correspondente à opção
visualizador.get(n, default)() # vai pra funçao escolhida
sys.exit() # Força a saída do programa, mas nao funciona kkkkkk
