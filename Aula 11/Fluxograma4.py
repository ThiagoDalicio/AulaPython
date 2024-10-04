def calcular_notas_e_centavos(valor):

    reais = int(valor)
    centavos = round((valor - reais) * 100)
    
    notas_50 = min(reais // 50, 50)
    resto_50 = reais - (notas_50 * 50)
    
    notas_10 = min(resto_50 // 10, 10)
    resto_10 = resto_50 - (notas_10 * 10)
    
    notas_1 = resto_10
    
    moedas_50 = centavos // 50
    resto_centavos = centavos % 50
    
    moedas_10 = resto_centavos // 10
    resto_centavos -= moedas_10 * 10
    
    moedas_1 = resto_centavos
    
    if notas_50 > 0:
        print(f"Notas de 50: {notas_50} (Valor total: {notas_50 * 50})")
    
    if notas_10 > 0:
        print(f"Notas de 10: {notas_10} (Valor total: {notas_10 * 10})")
    
    if notas_1 > 0:
        print(f"Notas de 1: {notas_1} (Valor total: {notas_1})")
    
    if moedas_50 > 0:
        print(f"Moedas de 50 centavos: {moedas_50} (Valor total: {moedas_50 * 50} centavos)")
    
    if moedas_10 > 0:
        print(f"Moedas de 10 centavos: {moedas_10} (Valor total: {moedas_10 * 10} centavos)")
    
    if moedas_1 > 0:
        print(f"Moedas de 1 centavo: {moedas_1} (Valor total: {moedas_1} centavos)")


def main():
    while True:
        valor = float(input("Digite o valor da conta (incluindo centavos): "))
        calcular_notas_e_centavos(valor)
        

        repetir = input("Deseja fazer outro saque? (sim/não): ").strip().lower()
        if repetir != "sim":
            print("Encerrando o programa.")
            break

# Executar o programa
main()