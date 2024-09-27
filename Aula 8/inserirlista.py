# Solicitar o número de alunos
try:
    numero_alunos = int(input("Quantos alunos você deseja analisar? "))
except ValueError:
    print("Por favor, insira um número válido.")
    exit()

# Criar uma lista para armazenar os dados dos alunos
lista_alunos = []

# Loop para processar o número especificado de alunos
for _ in range(numero_alunos):
    # Solicitar nome do aluno e as duas notas
    nome_aluno = input("Digite o nome do aluno: ")
    
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    
        # Calcular a média
        media = (nota1 + nota2) / 2
    
        # Exibir a média e o resultado de aprovação ou reprovação
        print(f"\nAluno: {nome_aluno}")
        print(f"Média: {media:.2f}")
    
        if media > 6.5:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"
        
        print(f"Resultado: {resultado}\n")
    
        # Armazenar os dados do aluno em um dicionário e adicionar à lista
        aluno = {
            'nome': nome_aluno,
            'nota1': nota1,
            'nota2': nota2,
            'media': media,
            'resultado': resultado
        }
        lista_alunos.append(aluno)
    
    except ValueError:
        print("Por favor, insira valores válidos para as notas.\n")

# Exibir a lista de alunos com suas respectivas notas e resultados
print("Lista de Alunos:")
for aluno in lista_alunos:
    print(f"Aluno: {aluno['nome']}, Nota 1: {aluno['nota1']}, Nota 2: {aluno['nota2']}, Média: {aluno['media']:.2f}, Resultado: {aluno['resultado']}")

print("\nMédias Obtidas.")