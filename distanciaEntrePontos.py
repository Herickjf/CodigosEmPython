from math import sqrt, pow
x1 = int(input("Digite o valor da coordenada x1: "))
y1 = int(input("Digite o valor da coordenada y1: "))
x2 = int(input("Digite o valor da coordenada x2: "))
y2 = int(input("Digite o valor da coordenada y2: "))

distancia = float(sqrt(pow((x2-x1), 2)+pow((y2-y1), 2)))

print(f"A distância entre ({x1},{y1}) e ({x2},{y2}) é {distancia:.2f}.")