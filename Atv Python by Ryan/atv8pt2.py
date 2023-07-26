# Atv 8 pt 2

def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = 5 * ((temp_fahrenheit - 32) / 9)
    return temp_celsius

def main_temperatura():
    try:
        temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
        print(f"A temperatura em graus Celsius é: {temp_celsius:.2f} °C")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um valor numérico válido.")

if __name__ == "__main__":
    main_temperatura()
