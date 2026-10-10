import pandas as pd

def analisar_faltantes(caminho_arquivo):
    print("\n--- 2. DIAGNÓSTICO DE DADOS FALTANTES ---")
    
    # 1. Carrega o CSV direto neste script
    df = pd.read_csv(caminho_arquivo)
    
    # 2. Cálculo de nulos e percentuais
    qtd_faltantes = df.isnull().sum()
    perc_faltantes = (df.isnull().sum() / len(df)) * 100
    
    # 3. Criação de uma tabela resumo
    tabela_faltantes = pd.DataFrame({
        'Faltantes (Qtd)': qtd_faltantes,
        'Percentual (%)': perc_faltantes
    })
    
    # 4. Filtra apenas colunas que têm dados faltando e ordena
    tabela_filtrada = tabela_faltantes[tabela_faltantes['Faltantes (Qtd)'] > 0]
    tabela_filtrada = tabela_filtrada.sort_values(by='Percentual (%)', ascending=False)
    
    print(tabela_filtrada)

# Execução independente
if __name__ == "__main__":
    analisar_faltantes("AirbnbRJRentals.csv")
