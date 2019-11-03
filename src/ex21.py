# Dado um número inteiro x, a função retorna a soma dos divisores inteiros de x
def soma_divisores(x):
    soma = 0;
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            soma = soma + i
    return soma

# Dado um número inteiro x, a função retorna a soma dos números amigáveis no intervalo [1, x)
def soma_amigaveis(x):
    soma = 0
    a = 1
    while a < x:
        b = soma_divisores(a)
        # se b > a, para que não se calcule um número amigável que já apareceu
        if b > a and soma_divisores(b) == a:
            soma = soma + a + b
        a = a + 1
    return soma

res = soma_amigaveis(10000)
print(res)
