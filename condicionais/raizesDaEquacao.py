from math import sqrt
a = int(input("Para a equação de 2° grau, digite o valor de a: "))
b = int(input("Para a equação de 2° grau, digite o valor de b: "))
c = int(input("Para a equação de 2° grau, digite o valor de c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Essa equação não possui raízes")
elif delta == 0: 
    delta = sqrt(delta)
    x1 = (-b+delta)/2*a
    print(f"Delta = {delta}\nX1 = {x1} (único valor de x)")
else: 
    delta = sqrt(delta)
    x1 = (-b+delta)/2*a
    x2 = (-b-delta)/2*a
    print(f"Delta = {delta}\nX1 = {x1}\nX2 = {x2}")
