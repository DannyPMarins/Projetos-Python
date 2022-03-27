lista  = []

numero_recebido = input('Digite um numero: ')

while (numero_recebido != 'fim') :
    lista.append(int(numero_recebido))
    numero_recebido = input('Digite outro numero : ')

print(lista)
