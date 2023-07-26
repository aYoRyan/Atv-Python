# Atv 12

def calcular_peso_ideal_altura(altura, sexo):
    if sexo == 'homem':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'mulher':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Escolha 'homem' ou 'mulher'.")

    return peso_ideal

def main():
    try:
        altura = float(input("Digite sua altura em metros: "))
        sexo = input("Digite seu sexo (homem/mulher): ").lower()

        if sexo == 'homem' or sexo == 'mulher':
            peso_ideal = calcular_peso_ideal_altura(altura, sexo)
            print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
        else:
            print("Sexo inválido. Escolha 'homem' ou 'mulher'.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um valor numérico válido para a altura.")

if __name__ == "__main__":
    main()
