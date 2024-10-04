def calcular_notas(valor):
    # Calcular a quantidade de notas de 50
    notas_50 = valor // 50
    resto_50 = valor % 50
    
    # Calcular a quantidade de notas de 10
    notas_10 = resto_50 // 10
    resto_10 = resto_50 % 10
    
    # Calcular a quantidade de notas de 1
    notas_1 = resto_10
    
    # Exibir o resultado
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 1: {notas_1}")

# Exemplo de uso
valor = int(input("Digite o valor da conta: "))
calcular_notas(valor)