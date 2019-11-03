from math import sqrt, floor, log10

# Dado um inteiro x, calcula o número de digitos
def num_digitos(x):
    return floor(1 + log10(x))

# Dado inteiro x, returna o x-ésimo valor da sequência de Fibonacci
# Solução não ideal para o problemas, pois calcula fib(x) em tempo exponencial
def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2) 

# Dado inteiro x, returna o x-ésimo valor da sequência de Fibonacci
# Solução melhor, pois calcula fib(x) em tempo constante (linear se 
# considerarmos o número de multiplicações que vão ocorrer para elevar
# a e b a x). Foi obtida usando o conceito de fórmula fechada para 
# recorrências
def fib_fechado(x):
    raiz5 = sqrt(5)
    a = (1 + raiz5) / 2
    b = (1 - raiz5) / 2
    return (a ** x - b ** x) / raiz5

# Dado inteiro x, returna o x-ésimo valor da sequência de Fibonacci
# Solução definitiva, pois calcula fib(x) em tempo linear, e possui 
# um uso de memória constante
def fib_definitivo(x):
    a = 1
    b = 0
    while x > 1:
        aux = a
        a = a + b
        b = aux
        x = x - 1
    return a

# Dado um inteiro x, retorna o índice do número de Fibonacci 
# que possui x digitos
def x_digit_Fibonacci(x):
    i = 1
    while num_digitos(fib_definitivo(i)) < x:
        i = i + 1
    return i

res = x_digit_Fibonacci(1000)
print(res)