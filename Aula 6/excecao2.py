try:
    n1 = int(input("Digite o primeiro número"))
    print(n1)
    n2 = int(input("Digite o segundo número"))
    print(n2)

    calculo = n1/n2
    print(calculo)

except ValueError:
    print("Digite um valor numérico")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except:
    print("Erro Inesperado")
finally:
    print("---------")
    print("Sempre executará... entranto ou não dentro de uma excessão.")
    
