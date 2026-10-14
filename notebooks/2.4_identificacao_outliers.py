import pandas as pd

def identificar_outliers_iqr(caminho_arquivo, coluna):
    print(f"\n--- 4. IDENTIFICAÇÃO DE OUTLIERS: Coluna '{coluna}' ---")
    
    # 1. Carrega o CSV direto neste script
    df = pd.read_csv(caminho_arquivo)
    
    # 2. Cálculo dos Quartis (25% e 75%)
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    
    # 3. Cálculo do Intervalo Interquartil (IQR)
    IQR = Q3 - Q1
    
    # 4. Definição dos limites estatísticos
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # 5. Filtragem dos registros que estão fora dos limites
    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    perc_outliers = (len(outliers) / len(df)) * 100
    
    print("Método Justificado: IQR (Intervalo Interquartil)")
    print(f"Q1 (25%): R$ {Q1:.2f} | Q3 (75%): R$ {Q3:.2f}")
    print(f"Limite Superior de Corte: R$ {limite_superior:.2f}")
    print(f"Total de Outliers encontrados: {len(outliers)} anúncios ({perc_outliers:.2f}% da base)")
    
    # 6. Retorna a base limpa sem os outliers para análises futuras
    df_sem_outliers = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
    return df_sem_outliers

# Execução independente focada na coluna de preço
if __name__ == "__main__":
    df_limpo = identificar_outliers_iqr("AirbnbRJRentals.csv", "price")
