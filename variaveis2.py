
#lista
variavel = ["Gabriel Dellatore", 20, "masculino", "estudante"]
print(variavel)

variavel[0] = "Ezequiel"
print(variavel)

#tupla
variavel2 = (1,2,3,4,5)
i = 0
while ( i < 4):
    print(f"elemento {i} : {variavel2[i]}")
    i+=1
    
#dicionario

variavel3 = {
    "Nome" : "Gabriel", 
    "Idade": 20,
    "cidade" : "Araraquara",
    "Documentos" : {
        "cpf" : "123.456.789-00",
        "rg" : "12345567890"
    },
    "fotos" : [
        "iamgens/rosto.jpg",
        "imagens/corpo.png"
    ]
}


print(variavel3.get("Nome"))#acessando um unico elemento do dicionario
print(variavel3.get("Documentos").get("rg"))#acessando um dicionario dentro de outro dicionario
print(variavel3["fotos"][1])#acessando uma lista em um dicionario 

#set

variavel4 = {1,2,3,4,5}

print(list(variavel4)[0])#acessando um elemento do set transformando em lista

