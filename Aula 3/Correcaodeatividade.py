# Atividades da aula 2

# Atividades 1 •	Escreva um programa que leia um valor em metros e exiba convertido em milímetros.
metros = float(input("Digite o valor em metros: "))
print(f"{metros} metros é igual a {metros * 1000} milímetros.")

# Atividades 2 •	Escreva um programa que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem de aumento do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite o valor do salário atual: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento: "))
print(f"Valor do aumento: R$ {salario * (percentual_aumento / 100):.2f}")
print(f"Novo salário: R$ {salario * (1 + percentual_aumento / 100):.2f}")

# Atividades 3 •	Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco_mercadoria = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
print(f"Valor do desconto: R$ {preco_mercadoria * (percentual_desconto / 100):.2f}")
print(f"Preço a pagar: R$ {preco_mercadoria * (1 - percentual_desconto / 100):.2f}")

# Atividades 4 •	Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância e percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))
print(f"O tempo estimado de viagem é de {distancia / velocidade_media:.2f} horas.")

# Atividades 5 	Escreva um programa que converta uma temperatura em º C em º F. A fórmula para essa conversão é: "F"=(9 x C)/5+"32" 
celsius = float(input("Digite a temperatura em ºC: "))
print(f"{celsius}ºC é igual a {(9 * celsius) / 5 + 32}ºF.")