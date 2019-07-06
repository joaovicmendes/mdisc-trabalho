# Dado dois inteiros low, high, calcula o número de resultados diferentes 
# das possíveis combinações de a ** b (elevado), com a, b pertencentes a [low, high]
def num_combinacoes(low, high):
    lista_combinacoes = []
    for a in range(low, high + 1):
        for b in range(low, high + 1):
            aux = a**b
            if aux not in lista_combinacoes:
                lista_combinacoes.append(aux)
    
    return len(lista_combinacoes)

res = num_combinacoes(2, 100)
print(res)
