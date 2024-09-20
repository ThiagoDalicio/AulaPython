lista = [10,20]

while True:
    numero = int(input("Digite um número (0 - sai) : "))
    if numero == 0:
        break
    lista.append(numero)


# O while não pode ser convertido em for porque 
# O número de repetições é desconhecido no início
for i in lista:
    print(i)