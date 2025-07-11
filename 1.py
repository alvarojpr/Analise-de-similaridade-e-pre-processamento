def read_fasta(arq):
  seq = ''
  with open(arq) as f:
    f.readline()
    for line in f:
      seq += line.strip()
  return seq

def comparar_sequencias(seq1, seq2):
  # Contagem de aminoácidos
  aminoacidos = set(seq1 + seq2) # União dos aminoácidos das duas sequências (sem repetições)
  # Em seguida, dois dicionários (ocorrencias1 e ocorrencias2) são criados, um para cada sequência. 
  # Cada dicionário mapeia cada aminoácido para o número de vezes que ele aparece na sequência.
  ocorrencias1 = {aa: 0 for aa in aminoacidos}
  ocorrencias2 = {aa: 0 for aa in aminoacidos}
  # As sequências são percorridas caractere por caractere, e a contagem de cada aminoácido no dicionário 
  # correspondente é incrementada.
  for aa in seq1:
    ocorrencias1[aa] += 1 
  for aa in seq2:
    ocorrencias2[aa] += 1

  # Distâncias
  distancia_manhattan = sum(abs(ocorrencias1[aa] - ocorrencias2[aa]) for aa in aminoacidos)
  distancia_euclidiana = ((sum((ocorrencias1[aa] - ocorrencias2[aa])**2 for aa in aminoacidos))**0.5)
  distancia_supremum = max(abs(ocorrencias1[aa] - ocorrencias2[aa]) for aa in aminoacidos)

  # Similaridade de cosseno
  numerador = sum(ocorrencias1[aa] * ocorrencias2[aa] for aa in aminoacidos)
  denominador = ((sum(ocorrencias1[aa]**2 for aa in aminoacidos))**0.5) * ((sum(ocorrencias2[aa]**2 for aa in aminoacidos))**0.5)
  similaridade_cosseno = numerador / denominador

  return {
    "distancia_manhattan": distancia_manhattan,
    "distancia_euclidiana": distancia_euclidiana,
    "distancia_supremum": distancia_supremum,
    "similaridade_cosseno": similaridade_cosseno
  }
def salvar_resultados(arquivo, resultados):
  """
    arquivo: Nome do arquivo CSV a ser criado.
    resultados: Dicionário com os resultados das comparações.
  """
  with open(arquivo, "w") as f:
    f.write("Sequência 1,Sequência 2,Distância Manhattan,Distância Euclidiana,Distância Supremum,Similaridade Cosseno\n")
    for seq1, seq2, medidas in resultados:
      f.write(f"{seq1},{seq2},{medidas['distancia_manhattan']},{medidas['distancia_euclidiana']},{medidas['distancia_supremum']},{medidas['similaridade_cosseno']}\n")

# Testes
hamster = read_fasta("hamster.fasta")
horse = read_fasta("horse.fasta")
rat = read_fasta("rat.fasta")

comparacao1 = comparar_sequencias(hamster, horse)
comparacao2 = comparar_sequencias(hamster, rat)
comparacao3 = comparar_sequencias(horse, rat)

resultados = [
  ("hamster", "horse", comparacao1),
  ("hamster", "rat", comparacao2),
  ("horse", "rat", comparacao3),
]

salvar_resultados("resultados_comparacoes.csv", resultados)

print("Resultados salvos no arquivo resultados_comparacoes.csv")

print("Comparação entre as sequências hamster e cavalo: ")
print(f"Distância Manhattan: {comparacao1['distancia_manhattan']}") # f = formatação 
print(f"Distância Euclidiana: {comparacao1['distancia_euclidiana']}")
print(f"Distância Supremum: {comparacao1['distancia_supremum']}")
print(f"Similaridade de Cosseno: {comparacao1['similaridade_cosseno']}\n")

print("Comparação entre as sequências hamster e rato: ")
print(f"Distância Manhattan: {comparacao2['distancia_manhattan']}")
print(f"Distância Euclidiana: {comparacao2['distancia_euclidiana']}")
print(f"Distância Supremum: {comparacao2['distancia_supremum']}")
print(f"Similaridade de Cosseno: {comparacao2['similaridade_cosseno']}\n")

print("Comparação entre as sequências cavalo e rato: ")
print(f"Distância Manhattan: {comparacao3['distancia_manhattan']}")
print(f"Distância Euclidiana: {comparacao3['distancia_euclidiana']}")
print(f"Distância Supremum: {comparacao3['distancia_supremum']}")
print(f"Similaridade de Cosseno: {comparacao3['similaridade_cosseno']}\n")


# Salvando os resultados em um arquivo de texto
  # with open('resultados.txt', 'w') as f:
  #   f.write('Comparação de proximidade entre rato e hamster: {}\n'.format(rat == hamster))
  #   f.write('Comparação de proximidade entre rato e cavalo: {}\n'.format(rat == horse))
  #   f.write('Comparação de proximidade entre hamster e cavalo: {}\n'.format(hamster == horse))
  #   f.write('Distância Manhattan: {}\n'.format(distancia_manhattan))
  #   f.write('Distância Euclidiana: {}\n'.format(distancia_euclidiana))
  #   f.write('Distância Supremum: {}\n'.format(distancia_supremum))
  #   f.write('Similaridade de cosseno: {}\n'.format(similaridade_cosseno))