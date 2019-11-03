soma = 1000 # esse é o resultado da soma dos 3 numeros
solucao = 0
for a in range(1, soma + 1): # Sera testada cada iteração a partir do caso base de A ser 1 ate A ser 1000 
    for b in range(a + 1, soma + 1): # então sera testado o B>A que então consiga satisfazer a solução
        c = soma - a - b
        if a * a + b * b == c * c:
            solucao = a * b * c
print(solucao)