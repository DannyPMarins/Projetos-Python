# lista1 = ["dado", "clipe", "dedo", "dolar", "mesa", "cadeira"]

# lista2 = [item for item in lista1 if item[0] == "d"]

# listaVezesDois = [numeros * 5 for numeros in lista1]

# print(sorted(lista2))

# lista_de_teste = ["America", "Brasil", "França", "Espanha", "Portugal", "Canada", "Mexico", "Alemanha", "Russia",]

# lista_em_orden = [item for item in lista_de_teste if item[0] == "A"]

# print(sorted(lista_em_orden))

listaDePerguntas = ["a. Sente dor no corpo?",
                    "b. Voce tem febre?",
                    "c. Voce tem tosse?",
                    "d. Esta com congestao nasal?",
                    "e. Tem manchas pelo corpo?"]

respostas = ''

for item in listaDePerguntas:
    resposta = input(f"{respostas} Por favor digite s ou n ")
    respostas += resposta

if (resposta == "ssnns" ):
    print("Voce tem dengue")

elif (resposta == "ssssn" or resposta == "nsssn" ):
    print("Voce tem gripe")

else:
    print("sem doenças")