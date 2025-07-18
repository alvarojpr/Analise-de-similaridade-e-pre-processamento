# Análise de Similaridade de DNA e Pré-processamento de Dados de Vinhos

## Parte 1: Similaridade de Enzimas

Foi implementado um script em Python que:
- Lê arquivos `.fasta` contendo sequências DNA da enzima topoisomerase I de rato, hamster chinês e cavalo;
- Compara as sequências entre si, contando ocorrência de cada aminoácido;
- Calcula as distâncias: Manhattan, Euclidiana, Supremum e Similaridade do Cosseno;
- Gera vetores numéricos e imprime os resultados comparativos.

## Parte 2: Análise de Qualidade de Vinhos

Usando o dataset `winequality-red.csv`, foram aplicadas as seguintes transformações:
- Normalização, padronização, binarização;
- Visualizações com histogramas e gráficos de densidade para cada atributo.

Bibliotecas utilizadas: `pandas`, `numpy`, `matplotlib`, `sklearn.preprocessing`
