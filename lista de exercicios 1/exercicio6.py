"""Solicite ao usuário dois números e peça que solicite uma operação matemática (+, -, *, /). Depos de receber a operação matemática escolhida, exibir o resultado.

**Após exibir o resultado, perguntar ao usuário se deseja realizar um novo cálculo.
**Se a resposta for S reinicie a operação, se for N encerre o programa. Caso não seja nem S ou N, informar que a escolha foi inválida."""



#MATCH

def cont():
    num1 = float(input("Digite o 1 numero: "))
    num2 = float(input("Digite o 2 numero: "))
    op_mat = input("digite a operação matemática (+, -, *, /)  desejada:")

    match op_mat:
        case "+":
            cont = num1 + num2
            print(f"{num1} + {num2} = {cont}") 
        case "-":
            cont = num1 - num2
            print(f"{num1} - {num2} = {cont}") 
        case "*":
            cont = num1 * num2
            print(f"{num1} * {num2} = {cont}") 
        case "/":
            cont = num1 / num2
            print(f"{num1} + {num2} = {cont}") 
        case _ :
            print("erro")

continuar = "s"
cont()
while continuar == "s":
    continuar = None
    continuar =input("digite s se deseja continuar:")
    if  continuar == "s":
        cont()
    


