def achaPrimos(limite): # Função que ira procurar todos os primos menores que um certo limite
    primos=[True for n in range(limite+1) ] # cria uma lista com n=limite elementos e os atribui o valor logico True
    crivo=2 # cria uma chave do primeiro número primo
    saida = [] # lista de saida
    while  crivo*crivo <= limite: # enquanto o quadrado da cahve for menor que o limite, o loop ocorre
        if(primos[crivo]==True): # verifica se a chave é um primo
            for i in range(crivo*2,limite+1,crivo): # procura todos os números multiplos da chave
                primos[i]=False # os transforma em falso, ou seja, não primos
        crivo += 1 # aumenta a chave 
    for i in range(2,limite): # Traduz o indice dos elemento primos para uma lista de elementos
        if primos[i]==True:
            saida.append(i)
    return saida
            
primos = achaPrimos(2000000)
soma = 0
for i in primos: # realiza a soma de todos os elementos
    soma += i
print(soma)