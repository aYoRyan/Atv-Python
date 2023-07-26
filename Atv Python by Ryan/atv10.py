# Atv 10

def calcular_resultados(num_int1, num_int2, num_real):
    produto = (2 * num_int1) * (num_int2 / 2)
    soma = (3 * num_int1) + num_real
    cubo = num_real ** 3
    return produto, soma, cubo

def main():
    try:
        num_int1 = int(input("Digite o primeiro número inteiro: "))
        num_int2 = int(input("Digite o segundo número inteiro: "))
        num_real = float(input("Digite o número real: "))

        resultado_produto, resultado_soma, resultado_cubo = calcular_resultados(num_int1, num_int2, num_real)

        print(f"O produto do dobro do primeiro com metade do segundo é: {resultado_produto:.2f}")
        print(f"A soma do triplo do primeiro com o terceiro é: {resultado_soma:.2f}")
        print(f"O terceiro elevado ao cubo é: {resultado_cubo:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores numéricos válidos.")

if __name__ == "__main__":
    main()
