start = 1 # começando pelo caso inicial
longest_number = 1 # Caso inicial da mais longa
longest_steps = 1 # Quantos passos ocorreram na mais longa
cur_steps = 0 # contador de passos
cur_number = 0 # numero inicial atual
while(start < 1000000): # verificando todos os casos ate 1000000
    cur_steps = 0
    start = start + 2 # verifica apenas os numeros impares pois esse tem as sequencias mais longas
    cur_number = start
    while (cur_number != 1): # loop ocorre enquanto não atingir o caso base
        if cur_number%2 == 0:
            cur_number = cur_number/2
            cur_steps = cur_steps+1
        else:
            cur_number = (3*cur_number)+1			
            cur_steps = cur_steps+1
    if cur_steps > longest_steps: # atualiza se a quantidade de passos da sequencia atual for maior que a sequencia maior anterior
        longest_number = start
        longest_steps = cur_steps
print(longest_number)