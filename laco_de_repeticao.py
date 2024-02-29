#numero_de_var = int(input())
"""
n= 0
lista = []
lista2 = [1,2,3,4]
while numero_de_var != 0 :
    var = int(input())
    lista.append(var)
    numero_de_var -= 1
print("------While-----") 
print(lista)
print("------For------")

for i in lista2:
    print(f"{n} : {i}")
    if i == 3:
        print("nmero achado")    
        break
    n += 1
"""

numero_tabuada = int(input("digite a tabuada que deseja formar:"))

for numero in range(11):
    print(f"{numero_tabuada} x {numero} = {numero_tabuada * numero}")

    