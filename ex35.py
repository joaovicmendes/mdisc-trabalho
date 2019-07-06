from math import ceil

# Dado um inteiro x, retorna True se for primo e False caso contrário
def primo(x):
    if x == 2:
        return True
    elif x % 2 == 0 or x < 2:
        return False
    else:
        divisivel = False
        i = 2
        while i <= x/2 and not divisivel:
            if x % i == 0:
                divisivel = True
            i = i + 1
    return not divisivel

# Dado um limitante superior x, retorna a lista de tamanho x com
# True se o número com aquele índice é primo e False caso contrário
def lista_primos(x):
    lista = []
    for i in range(0, x):
        lista.append(primo(i))
    return lista

# Algotimo mais eficiente para gerar uma lista de primos
# Dado um inteiro x, retorn uma lista com True se aquele 
# índice é de um primo, False caso contrário
def sieve_eratosthenes(x):
    arredonda = lambda x, primo: int(ceil(float(x) / primo))

    primos = [True] * x
    primos[0] = False
    primos[1] = False
    lista_primo = []

    for primo_atual in range(2, x):
        if not primos[primo_atual]:
            continue
        lista_primo.append(primo_atual)
        for m in range(2, arredonda(x, primo_atual)):
            primos[m * primo_atual] = False
    return primos

# Dado um valor primo x, verifica se as rotações dos dígitos 
# de x estão contidas numa lista booleana de primos
def primo_circular(x, lista_de_primos):
    x = str(x) # convertendo para string para facilitar rotação
    for i in range(0, len(x)):
        rotacionado = x[i:len(x)] + x[0:i]
        if not lista_de_primos[int(rotacionado)]:
            return False
    return True

# Dado um limitante superior inteiro x, retorna quantos primos
# circulares existem em [1, x)
def quantos_primos_circulares(x):
    quantidade = 0
    primos = sieve_eratosthenes(x)
    for i in range(0, x):
        if primo_circular(i, primos):
            quantidade = quantidade + 1
    return quantidade

res = quantos_primos_circulares(1000000)
print(res)
