""" Solicite ao usuário para inserir números até que a soma deles seja maior que 100."""


soma = 100.0
num = 0
total = 0
while soma != -1:
    num = float(input("digite um numero: "))
    total += num
    soma -= num
    print(f"total : {total}")
    
print("FIM")
    