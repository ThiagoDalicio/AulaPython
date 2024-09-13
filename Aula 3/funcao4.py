def fazer_big_mac(nome):
    print(f'Sanduiche Big Mac {nome}')


def fazer_batata(tamanho):
    print(f'Batata {tamanho}')

def preparar_refrigerante(tipo,tamanho):
    print(f'{tipo} {tamanho}')


def combo_bigmac(nome, tamanho_batata,tipo_refrigerante,tamanho_refrigerante):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refrigerante,tamanho_refrigerante)

combo_bigmac("thiago", "Médio", "Coca-Cola","grande")
