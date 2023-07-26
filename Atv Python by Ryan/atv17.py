# Atv 17

def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    velocidade_bytes_por_segundo = velocidade_internet_mbps / 8
    tempo_segundos = tamanho_arquivo_mb / velocidade_bytes_por_segundo
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

def main():
    try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_internet_mbps = float(input("Digite a velocidade da conexão de Internet (em Mbps): "))

        tempo_aproximado_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

        print(f"\nO tempo aproximado de download do arquivo é de {tempo_aproximado_minutos:.2f} minutos.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos para o tamanho do arquivo e a velocidade da Internet.")

if __name__ == "__main__":
    main()
