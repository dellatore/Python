def mostrar_lista(itens): 
    if len(itens) <= 0:
        print("a lista está vazia")      
    else:
        for indice,item in enumerate(itens):
            print(f"{indice + 1}. {item["nome"]} - {item["status"]}")
    
    print("\n")    
    menu(itens)

def adicionar_item(itens):
    novo_item = input("digite o nome do item que deseja adicionar: ")
    id = len(itens) 
    itens.append({"nome" : None, "status" : "pendente"})
    itens[id]["nome"] = novo_item
    print("\n")
    menu(itens)

def alterar_item(itens):
    id = int(input("digite o id do item que deseja alterar: "))
    id = id - 1
    alterar = input("digite o novo nome do item :")
    itens[id]["nome"] = alterar
    print("\n")
    menu(itens)
    
def remover_item(itens):
    id = int(input("digite o id do item que deseja remover: "))
    id = id - 1
    itens.pop(id)
    print("\n")
    menu(itens)

def marcar_como_concluida(itens):
    id = int(input("digite o id do item que deseja marcar como concluido: "))
    id = id - 1
    itens[id]["status"] = "concluido"
    print("\n")
    menu(itens)

def menu(itens):
    print("************************************************")
    print("esse é o menu de itens :")
    print("1. mostrar lista")
    print("2. adicionar item")
    print("3. alterar item")
    print("4. remover item")
    print("5. marcar como concluido")
    print("6. exportar para o Excel")
    print("0. encerrar programa")
    print("************************************************")
    parar = True
    op = 1
    while parar == True:
       
        op = int(input("digite o id que deseja: "))
        
        match op:
            case 1:
                print("\n")
                mostrar_lista(itens)
            case 2: 
                print("\n")
                adicionar_item(itens)
            case 3:
                print("\n")
                alterar_item(itens)
            case 4:
                print("\n")
                remover_item(itens)
            case 5:
                print("\n")
                marcar_como_concluida(itens)
            case 6:
                print("nao feito")
            case 0:
                exit()
             
    
            
itens = []
menu(itens)


