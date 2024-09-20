"""
Escreva um programa que leia dois números e 
que pergunte qual operação você deseja realizar.
Você deve poder calcula
soma (+), subtração (-) multiplicação (*) e divisão (/).
exiba o resultado da operação solicitada
 """
# entrada
num1 = int("Digite o primeiro número para cálculo. ")
num2 = int("Digite p segundo número. ")
operação = input("Deseja realizar soma (+), subtração (-) multiplicação (*) e divisão (/)")

# Processamento
if operação == "+":
    resultado = num1 + num2
elif operação == "-":
    resultado = num1 - num2
elif operação == "*":
    resultado = num1 * num2
elif operação == "/":
    resultado = num1 / num2
else:
    print("Operação Inválida")
    resultado = 0
print("Resultado : ", resultado)
