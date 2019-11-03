from math import ceil

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
    return lista_primo, primos

# Dado um inteiro x, retorna a maior sequência de soma de primos, tal que a soma é inferior a x
def maior_soma_primos(x):
    maior = 0
    lista_primo, é_primo = sieve_eratosthenes(x)
    consecutivo = 0
    for i in range(len(lista_primo)):
        soma = lista_primo[i]
        consec = 1
        for j in range(i + 1, len(lista_primo)):
            soma += lista_primo[j]
            consec += 1
            if soma >= len(é_primo):
                break
            if é_primo[soma] and consec > consecutivo:
                maior = soma
                consecutivo = consec
    return maior

res = maior_soma_primos(1000000)
print(res)
