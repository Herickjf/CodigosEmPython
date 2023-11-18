''' Uma imobiliária paga aos seus corretores um salário base
de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
cada imóvel vendido e 5% do valor de cada venda. Construa
um programa que solicite o nome do corretor, a quantidade
de imóveis vendidos e o valor total de suas vendas. Ao fim, o
programa deve calcular e escrever o salário final do corretor de
imóveis. '''
nome = input("Digite seu nome:  ")
n = int(input("Digite quantos imóveis você vendeu: "))
valor = float(input("Digite o valor total dos imóveis que você vendeu: "))
salario = float(1500 + n*200 + (5*valor/100))
print(f"O salário de {nome} é R${salario:.2f}.")