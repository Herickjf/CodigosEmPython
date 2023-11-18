objeto = input("De qual objeto você quer saber a velocidade? ")
deslocamento = float(input(f"\nDigite (em metros) a distância percorrida pelo(a) {objeto}: "))
tempo = float(input(f"Digite quanto tempo (em segundos) o(a) {objeto} levou para fazer esse"
                    f" deslocamento: "))
print(f"o(a) {objeto} se moveu a {deslocamento/tempo:.1f} m/s.")