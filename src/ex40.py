from math import sqrt, ceil

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
    return lista_primo

# Encontra o primeiro número que não obedesce a conjectura
# de Goldbach
def goldbach_conjecture():
    lista_primos = sieve_eratosthenes(1000000)
    num = 1
    não_encontrou = True
    while não_encontrou:
        num += 2
        i = 0
        não_encontrou = False
        while num >= lista_primos[i]:
            a = num - lista_primos[i]
            # quando essa condição não é satisfeita, o número não é quadrado perfeito
            if sqrt(a/2) == int(sqrt(a/2)):
                não_encontrou = True
                break
            i += 1
    return num

res = goldbach_conjecture()
print(res)