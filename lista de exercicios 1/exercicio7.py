"""Você está criando um sistema que irá calcular quanto um cinema recebe por sessão do filme que está em cartaz "As tranças do Rei Careca". Você deve solicitar que seja informado qual a capacidade de assentos de uma sala do cinema, o valor do Ingresso Inteiro, o valor do Meio-Ingresso, quantas vendas foram realizadas daquela sessão e das vendas realizadas quantas foram Inteiros e quantas foram Meio-Ingresso.

Você deve exibir:
**Qual a porcentagem de assentos vendidos.
**Qual a porcentagem de assentos vendidos como Ingresso Inteiro.
**Qual a porcentagem de assentos vendidos como Meio-Ingresso.
**Exibir qual o total de vendas por tipo de ingresso.
**Exibir o total da receita por sessão do filme."""


def TotalAssentos(capacidade,vendas_inteiras,vendas_meia):
    porc = (vendas_inteiras + vendas_meia) /capacidade 
    porc = porc * 100
    return porc

def AssentosMeio(vendas_meia,total):
    porc_meias = vendas_meia / total
    porc_meias = porc_meias * 100
    return porc_meias 

def AssentosInteiro(vendas_inteiras,total):
    porc_inteiras =  vendas_inteiras / total
    porc_inteiras = porc_inteiras *100
    return porc_inteiras

def TotalVendas(total, vendas_meia):
    inteiras = total - vendas_meia
    meias = total - inteiras
    print(f"total de vendas meia foram de {meias} ingressos")
    print(f"total de vendas inteiras foram de {inteiras} ingressos")
    
def ReceitaSessao(vendas_inteiras,vendas_meia,meio_ingresso,inteira):
    cont_int = vendas_inteiras * inteira
    cont_meia = vendas_meia * meio_ingresso
    cont_total = cont_int + cont_meia
    
    print(f"o valor arrecadado dos {vendas_inteiras} ingressos inteiros foi R${cont_int}")
    print(f"o valor arrecadado dos {vendas_meia} meio-ingressos foi R${cont_meia}")
    print(f"o total arrecadado foi de R$ {cont_total}")
    

print("\t\t\t\tBem-Vindo ao Netflix!!!")

capacidade = int(input("digite a quantidade de assentos da sessao: "))
inteira = float(input("digite o valor do ingresso inteiro: R$"))
meio_ingresso = float(input("digite o valor do meio-ingresso: R$"))
vendas_inteiras = int(input("Digite o total de vendas inteiras: "))
vendas_meia = int(input("digite a quantidade de vendas meio-ingresso: "))
total = vendas_inteiras + vendas_meia 
print("\n\n")
porc = TotalAssentos(capacidade,vendas_inteiras,vendas_meia)
print(f"A porcentagem de assentos vendidos foi : {porc} %")

print("\n\n")
porc_inteiras = AssentosInteiro(vendas_meia, total)
print(f"Dos {porc}%, {porc_inteiras} % foram assentos vendidos como meia")


porc_meias = AssentosInteiro(vendas_inteiras, total)
print(f"Dos {porc}%, {porc_meias} % foram assentos vendidos como inteira")

print("\n\n")
TotalVendas(total,vendas_meia)

print("\n\n")
print("\t\t\t\tRECEITA CINEMA")
ReceitaSessao(vendas_inteiras,vendas_meia,meio_ingresso,inteira)




