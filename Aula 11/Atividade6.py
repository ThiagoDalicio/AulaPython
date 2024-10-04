def calcular_peso_ideal(altura, sexo):
    if sexo.upper() == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.upper() == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido. Use 'M' para masculino ou 'F' para feminino."
    
    return round(peso_ideal, 2)

altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

peso_ideal = calcular_peso_ideal(altura, sexo)
print(f"O peso ideal é: {peso_ideal} kg")