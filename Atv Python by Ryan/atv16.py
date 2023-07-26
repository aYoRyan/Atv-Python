# Atv 16

import math

def calcular_quantidade_e_preco_latas(area_a_ser_pintada):
    # Cálculo da quantidade de tinta necessária em litros com 10% de folga
    litros_de_tinta = area_a_ser_pintada / 6 * 1.1

    # Cálculo da quantidade de latas de tinta necessárias (considerando latas de 18 litros)
    latas_de_tinta = math.ceil(litros_de_tinta / 18)

    # Cálculo do preço total com latas de 18 litros
    preco_total = latas_de_tinta * 80

    return latas_de_tinta, preco_total

def calcular_quantidade_e_preco_galoes(area_a_ser_pintada):
    # Cálculo da quantidade de tinta necessária em litros com 10% de folga
    litros_de_tinta = area_a_ser_pintada / 6 * 1.1

    # Cálculo da quantidade de galões de tinta necessários (considerando galões de 3,6 litros)
    galoes_de_tinta = math.ceil(litros_de_tinta / 3.6)

    # Cálculo do preço total com galões de 3,6 litros
    preco_total = galoes_de_tinta * 25

    return galoes_de_tinta, preco_total

def calcular_quantidade_e_preco_mistura(area_a_ser_pintada):
    # Cálculo da quantidade de tinta necessária em litros com 10% de folga
    litros_de_tinta = area_a_ser_pintada / 6 * 1.1

    # Cálculo da quantidade de latas de tinta necessárias (considerando latas de 18 litros)
    latas_de_tinta = int(litros_de_tinta / 18)

    # Cálculo do restante de tinta em litros que será preenchido com galões de 3,6 litros
    restante_litros = litros_de_tinta % 18

    # Cálculo da quantidade de galões de tinta necessários
    galoes_de_tinta = math.ceil(restante_litros / 3.6)

    # Cálculo do preço total com a mistura de latas de 18 litros e galões de 3,6 litros
    preco_total = (latas_de_tinta * 80) + (galoes_de_tinta * 25)

    return latas_de_tinta, galoes_de_tinta, preco_total

def main():
    try:
        # Leitura do tamanho em metros quadrados da área a ser pintada
        area_a_ser_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

        # Opção 1: Comprar apenas latas de 18 litros
        latas_de_tinta, preco_latas = calcular_quantidade_e_preco_latas(area_a_ser_pintada)

        # Opção 2: Comprar apenas galões de 3,6 litros
        galoes_de_tinta, preco_galoes = calcular_quantidade_e_preco_galoes(area_a_ser_pintada)

        # Opção 3: Comprar uma combinação de latas de 18 litros e galões de 3,6 litros
        latas_mistura, galoes_mistura, preco_mistura = calcular_quantidade_e_preco_mistura(area_a_ser_pintada)

        # Exibição dos resultados
        print(f"\nOpção 1 - Comprar apenas latas de 18 litros:")
        print(f"Quantidade de latas de tinta: {latas_de_tinta}")
        print(f"Preço total: R$ {preco_latas:.2f}")

        print(f"\nOpção 2 - Comprar apenas galões de 3,6 litros:")
        print(f"Quantidade de galões de tinta: {galoes_de_tinta}")
        print(f"Preço total: R$ {preco_galoes:.2f}")

        print(f"\nOpção 3 - Comprar uma combinação de latas e galões:")
        print(f"Quantidade de latas de tinta: {latas_mistura}")
        print(f"Quantidade de galões de tinta: {galoes_mistura}")
        print(f"Preço total: R$ {preco_mistura:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para a área a ser pintada.")

if __name__ == "__main__":
    main()
