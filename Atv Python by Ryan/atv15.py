# Atv 15

import math

def calcular_latas_de_tinta(area_a_ser_pintada):
    # Cálculo da quantidade de tinta necessária em litros
    litros_de_tinta = area_a_ser_pintada / 3

    # Cálculo da quantidade de latas de tinta necessárias (considerando latas de 18 litros)
    latas_de_tinta = math.ceil(litros_de_tinta / 18)

    return latas_de_tinta

def calcular_preco_total(latas_de_tinta):
    # Preço de cada lata de tinta (R$ 80,00)
    preco_por_lata = 80

    # Cálculo do preço total
    preco_total = latas_de_tinta * preco_por_lata

    return preco_total

def main():
    try:
        # Leitura do tamanho em metros quadrados da área a ser pintada
        area_a_ser_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

        # Cálculo das latas de tinta necessárias
        latas_de_tinta = calcular_latas_de_tinta(area_a_ser_pintada)

        # Cálculo do preço total
        preco_total = calcular_preco_total(latas_de_tinta)

        # Exibição dos resultados
        print(f"\nQuantidade de latas de tinta a serem compradas: {latas_de_tinta}")
        print(f"Preço total: R$ {preco_total:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para a área a ser pintada.")

if __name__ == "__main__":
    main()
