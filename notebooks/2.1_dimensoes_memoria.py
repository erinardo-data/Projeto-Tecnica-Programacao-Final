import pandas as pd

def analisar_estrutura(caminho_arquivo):
    print("--- 1. DIAGNÓSTICO DE ESTRUTURA E MEMÓRIA ---")
    df = pd.read_csv(caminho_arquivo)
    
    # Dimensões
    linhas, colunas = df.shape
    print(f"Dimensões: {linhas} linhas e {colunas} colunas")
    
    # Uso de memória (em Megabytes)
    memoria_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
    print(f"Uso de Memória: {memoria_mb:.2f} MB\n")
    
    # Tipos de dados
    print("Tipos de dados por coluna:")
    print(df.dtypes)
    
    return df

# Execução
if __name__ == "__main__":
    df_base = analisar_estrutura("AirbnbRJRentals.csv")
