#   A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos
#com desconto. O desconto é calculado sobre o valor do veículo de acordo com o tipo do
#combustível do veículo (álcool – 25%, gasolina – 21% ou diesel –14%). Escreva um
#programa que leia o valor de venda do veículo, calcule e mostre o valor do desconto e o
#valor final do veículo que será pago pelo cliente.

preco = float(input("Digite o valor do carro: "))
tipo = input("\nMenu:\n\n\t(a) Álcool\n\t(g) Gasolina\n\t(d) Diesel\n\nDigite o tipo de combustível do veículo: ")
teste = 0
match tipo:
    case('a'):
        precof = preco*0.75
        teste = 1
    case ('g'):
        precof = preco*0.79
        teste = 1
    case ('d'):
        precof = preco*0.86
        teste = 1
if teste==0:
    print("Opção inválida :(")
    exit(0)

print("Valor final do carro:  ", precof)
exit(0)
