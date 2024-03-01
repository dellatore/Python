""" Receba o total de vendas realizadas por um vendedor de uma loja e cálcule o valor de sua comissão."""


num_comissoes = int(input("Digite o numero de vendas realizadas: "))
vendas = 0
comissao = 0
i = 1

while num_comissoes > 0 :
    
    vendas += float(input(f"valor da venda{i}: "))
    num_comissoes -= 1
    i += 1
    
if vendas <= 1000 :
    comissao = vendas * 0.05
    vendas = vendas + comissao
    print(f"o salario é igual a: {vendas}")
elif vendas > 1000 and vendas <= 5000 :
    comissao = vendas * 0.075
    vendas = vendas + comissao
    print(f"o salario é igual a: {vendas}")
else:
    comissao = vendas * 0.09
    vendas = vendas + comissao
    print(f"o salario é igual a: {vendas}")
