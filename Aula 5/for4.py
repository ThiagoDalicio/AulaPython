# Solicito ao usuário para digitar um número
numero = int(input("Digite um número para a tabuada de 10: "))

# Inicializo a tabuada de 1 até 10
for index in range(0, 10):
    aux = index * numero
    print(index, "x", numero, "=", aux)

