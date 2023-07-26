# Atv 8 pt 1

def calcular_salario_mensal(valor_hora, horas_trabalhadas):
    salario_mensal = valor_hora * horas_trabalhadas
    return salario_mensal

def main_salario():
    try:
        valor_hora = float(input("Digite o valor que você ganha por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        if valor_hora < 0 or horas_trabalhadas < 0:
            print("Os valores não podem ser negativos.")
        else:
            salario_mensal = calcular_salario_mensal(valor_hora, horas_trabalhadas)
            print(f"Seu salário mensal é: R${salario_mensal:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores numéricos válidos.")

if __name__ == "__main__":
    main_salario()
