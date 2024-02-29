temperatura = int(input())

#CONDICIONAL SIMPLES
if temperatura > 30 or temperatura< 10:         # OR = ou
    print("a temperatura esta extrema")
elif temperatura>10 and temperatura<30:         # AND = e
    print("A TEMPERATURA SE ENCONTRA NESSA FAIXA")    
else:
    print("a temperatura esta moderada!")
    
#OPERADOR TERNARIO
idade = int(input())
idade = "Maior de idade" if idade >= 18 else "Menor de idade" #variavel = reorno_verdade if condição else retorno_falso
print(idade)
     