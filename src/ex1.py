primo_atual = 3
primos = [2]
eh_primo = 1  # flag que verifica se o numero é primo ou não
while( len(primos) != 10001): # loop ocorre enquanto não a lista de numeros primos é diferente a 10001
    eh_primo = 1
    primo_atual = primo_atual + 2 #C onsiderando que o unico numero primo par é o numero 2, podemos então pular todos os numero pares e considerar apenas os impares
    for n in primos: # utilizando todos os primos anteriores
        if primo_atual%n == 0: # verificamos se o numero a ser analizado no momento não é divisivel por nenhum deles o que implicara que ele so tem um unico divisor alem de 1
            eh_primo = 0	
    if eh_primo == 1: # passando nos testes o numero é adicionado a lista
        primos.append(primo_atual)
print(primos[10000])