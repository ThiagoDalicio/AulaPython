"""
Dicionario possui chave valor
quando passo a chave ele devolve o valor 
não aceita valores duplicados
é mutavel, podemos modificar o valor dentro dele
"""

meses = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",

}

# imprimir todo dicionário
print(meses)

#imprimir valor a partir de uma chave
#passei uma chave e ele retornor o valor da respectiva chave
print(meses["Jan"])
print(meses["Jun"])
#print(meses["gato"]) KeyError: 'gato'


