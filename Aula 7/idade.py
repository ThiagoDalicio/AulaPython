# Solicitar o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verificar a idade e exibir a mensagem apropriada
if idade > 50:
    mensagem = f"{nome} tem {idade} anos e é experiente."
else:
    mensagem = f"{nome} tem {idade} anos, está em treinamento."

print(mensagem)
