# Loop para processar mais de um aluno
while True:
    # Solicitar nome do aluno e as duas notas
    nome_aluno = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    
    if nome_aluno.lower() == 'sair':
        break
    
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    
        # Calcular a média
        media = (nota1 + nota2) / 2
    
        # Exibir a média e o resultado de aprovação ou reprovação
        print(f"\nAluno: {nome_aluno}")
        print(f"Média: {media:.2f}")
    
        if media > 6.5:
            print("Resultado: Aprovado\n")
        else:
            print("Resultado: Reprovado\n")
    
    except ValueError:
        print("Por favor, insira valores válidos para as notas.\n")
        