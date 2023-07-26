# Atv 11

def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

def main():
    try:
        altura = float(input("Digite sua altura em metros: "))
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um valor numérico válido.")

if __name__ == "__main__":
    main()
