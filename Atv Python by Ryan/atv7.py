# Atv 7

def calcular_area_quadrado(lado):
    area = lado ** 2
    return area

def main():
    try:
        lado = float(input("Digite o valor do lado do quadrado: "))
        if lado < 0:
            print("O lado não pode ser negativo.")
        else:
            area = calcular_area_quadrado(lado)
            area_dobro = area * 2
            print(f"A área do quadrado é: {area:.2f}")
            print(f"O dobro da área do quadrado é: {area_dobro:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para o lado.")

if __name__ == "__main__":
    main()
