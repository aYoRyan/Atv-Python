# Atv 13

def calcular_multa(peso_peixes):
    limite_peso = 50
    if peso_peixes <= limite_peso:
        excesso = 0
        multa = 0
    else:
        excesso = peso_peixes - limite_peso
        multa = excesso * 4.00

    return excesso, multa

def main():
    try:
        peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
        excesso, multa = calcular_multa(peso_peixes)

        if excesso > 0:
            print(f"Você excedeu o limite em {excesso:.2f} kg.")
            print(f"Valor da multa a ser pago: R$ {multa:.2f}")
        else:
            print("Peso dentro do limite permitido. Sem multa.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um valor numérico válido para o peso.")

if __name__ == "__main__":
    main()
