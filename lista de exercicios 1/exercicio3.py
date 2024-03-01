""" Receba uma frase e conte quantas vogais ela possui."""

frase = input("escreva uma frase:")

#print(frase)
vogal = 0
for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vogal += 1
        
print(f"a frase '{frase}' possui {vogal} vogais.")