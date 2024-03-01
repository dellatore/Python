"""Solicite um número e imprima a tabuada do número informado."""

num = int(input("digite o numero da tabuada desejado: "))
    
for i in range(1,11):
    print(f"{num} x {i} = {i * num}")
    
"""cont = 1
while cont <= 10:
    mult = cont * num
    print(f"{num} x {cont} = {mult}")
    cont += 1"""