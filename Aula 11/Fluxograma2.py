def calcular_notas(valor):
    # Limitar a quantidade de notas de 50 a no máximo 50
    notas_50 = min(valor // 50, 50)
    resto_50 = valor - (notas_50 * 50)
    
    # Limitar a quantidade de notas de 10 a no máximo 10
    notas_10 = min(resto_50 // 10, 10)
    resto_10 = resto_50 - (notas_10 * 10)
    
    # Calcular a quantidade de notas de 1, sem limitação
    notas_1 = resto_10
    
    # Exibir o resultado de forma condicional
    if notas_50 > 0:
        print(f"Notas de 50: {notas_50} (Valor total: {notas_50 * 50})")
    
    if notas_10 > 0:
        print(f"Notas de 10: {notas_10} (Valor total: {notas_10 * 10})")
    
    if notas_1 > 0:
        print(f"Notas de 1: {notas_1} (Valor total: {notas_1})")

# Exemplo de uso
valor = int(input("Digite o valor da conta: "))
calcular_notas(valor)