# Fluxograma

def calcular_notas(valor):

    notas_50 = min(valor // 50, 50)
    resto_50 = valor - (notas_50 * 50 )
    
    notas_10 = min(resto_50 // 10, 10)
    resto_10 = resto_50 - (notas_10 * 10)
    
    notas_1 = resto_10
    
    print(f"Notas de 50: {notas_50} (Valor total: {notas_50 * 50})")
    print(f"Notas de 10: {notas_10} (Valor total: {notas_10 * 10})")
    print(f"Notas de 1: {notas_1} (Valor total: {notas_1})")

valor = int(input("Digite o valor da conta: "))
calcular_notas(valor)


# como eu incluo condição sendo as informações separadas sobre a conta?