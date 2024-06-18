print('Olá, informe seus dados para calcular se o emprestimo é possivél!')
valor_imovel = float(input("qual o valor do imovél:"))
salário = float(input("Qual o seu sálario mensal:"))
tempo = int(input("Quanto tempo em anos você quer pagar o impresitmo:"))
if valor_imovel/tempo > (salário * 12)*0.3 :
    print('Infelizmente seu emprestimo foi negado')
else:
    print("seu imprestimo foi aprovado")
    print(f'A prestação será de R${float((valor_imovel/tempo)/12): .2f} mensais')