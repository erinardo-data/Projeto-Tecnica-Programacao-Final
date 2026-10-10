import pandas as pd

def analisar_preco_localizacao_texto(caminho_arquivo):
    # 1. Carregar os dados
    df = pd.read_csv(caminho_arquivo)
    
    # 2. Limpeza de Outliers (Filtro estatístico pelo método IQR)
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    limite_superior = Q3 + 1.5 * IQR
    
    # Filtra preços zerados e valores absurdos
    df_limpo = df[(df['price'] > 0) & (df['price'] <= limite_superior)]
    
    # 3. Métricas Gerais
    print("=========================================")
    print("       RESUMO DE PREÇOS (RJ)             ")
    print("=========================================")
    print(f"Preço Médio na cidade:   R$ {df_limpo['price'].mean():.2f}")
    print(f"Preço Mediano na cidade: R$ {df_limpo['price'].median():.2f}")
    
    # 4. Agrupamento por Bairro (Filtrando bairros com pelo menos 10 anúncios)
    bairros_stats = df_limpo.groupby('neighbourhood')['price'].agg(['mean', 'median', 'count'])
    bairros_validos = bairros_stats[bairros_stats['count'] >= 10]
    
    # Ordenação
    top_10_caros = bairros_validos.sort_values(by='mean', ascending=False).head(10)
    top_10_baratos = bairros_validos.sort_values(by='mean', ascending=True).head(10)
    
    # 5. Exibição Tabular
    print("\n=========================================")
    print("   TOP 10 BAIRROS MAIS CAROS (Média)     ")
    print("=========================================")
    # Renomeando as colunas para ficar mais amigável no terminal
    top_10_caros_formatado = top_10_caros.rename(columns={'mean': 'Preço Médio (R$)', 'median': 'Mediana (R$)', 'count': 'Qtd Anúncios'})
    print(top_10_caros_formatado.round(2))
    
    print("\n=========================================")
    print("  TOP 10 BAIRROS MAIS BARATOS (Média)    ")
    print("=========================================")
    top_10_baratos_formatado = top_10_baratos.rename(columns={'mean': 'Preço Médio (R$)', 'median': 'Mediana (R$)', 'count': 'Qtd Anúncios'})
    print(top_10_baratos_formatado.round(2))

# Execução do script
if __name__ == "__main__":
    analisar_preco_localizacao_texto("AirbnbRJRentals.csv")
