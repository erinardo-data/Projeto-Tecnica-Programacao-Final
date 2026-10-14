import pandas as pd

def validar_regras_negocio(caminho_arquivo):
    print("\n--- 3. DUPLICADOS E INCONSISTÊNCIAS ---")
    
    # 1. Carrega o CSV direto neste script
    df = pd.read_csv(caminho_arquivo)
    
    # 2. Checagem de linhas duplicadas
    duplicados = df.duplicated().sum()
    print(f"Linhas perfeitamente duplicadas: {duplicados}")
    
    # 3. Categorias inconsistentes (verificando se há tipos de quartos estranhos)
    print("\nDistribuição de Tipos de Quarto (room_type):")
    print(df['room_type'].value_counts())
    
    # 4. Valores inválidos baseados na lógica do mundo real
    precos_invalidos = (df['price'] <= 0).sum()
    noites_invalidas = (df['minimum_nights'] <= 0).sum()
    
    print(f"\nAnúncios com preço R$ 0 ou negativo: {precos_invalidos}")
    print(f"Anúncios com noites mínimas zeradas ou negativas: {noites_invalidas}")

# Execução independente
if __name__ == "__main__":
    validar_regras_negocio("AirbnbRJRentals.csv")
