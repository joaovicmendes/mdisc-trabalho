x = 2**1000 # numero a ser usado
div = 10 # potencia de 10 inicial
aux = 0
aux2 = 1
soma = 0 # soma final dos digitos
while(x>0): # realiza o loop até que o numero inicial seja 0
    aux = x%div # armazena o digito a ser recebido nessa iteração
    soma = soma+ (aux/aux2) # soma o digito a soma total, é usado um auxiliar para garantir que o numero seja unitário 
    x = x - aux # remove o resto do número
    aux2 =div # atualiza as potencias para poder continuar a operação
    div = div*10
print(soma)