# 🏠 Análise Exploratória — Airbnb Rio de Janeiro

**Projeto Final — Técnicas de Programação I (DS-PY-004)**
Ada Tech | Turma 1735

---

## 📌 Sobre o projeto

Análise exploratória de dados (EDA) sobre o mercado de aluguéis de curta temporada
no Rio de Janeiro, utilizando a base pública do Inside Airbnb.

O projeto aplica técnicas de programação em Python para inspecionar, limpar e
extrair insights de um dataset real com mais de 28 mil registros.

---

## 🗂️ Dataset

| Atributo | Valor |
|---|---|
| Fonte | [Inside Airbnb — Rio de Janeiro](http://insideairbnb.com/get-the-data/) |
| Arquivo | `AirbnbRJRentals.csv` |
| Linhas | 28.301 |
| Colunas | 16 |

> 📥 A base utilizada está disponível em `dados/AirbnbRJRentals.csv`.
> Caso queira baixar diretamente da fonte original: http://insideairbnb.com/get-the-data/

**Colunas principais:**
`id`, `name`, `host_id`, `host_name`, `neighbourhood`, `latitude`, `longitude`,
`room_type`, `price`, `minimum_nights`, `number_of_reviews`, `last_review`,
`reviews_per_month`, `calculated_host_listings_count`, `availability_365`,
`number_of_reviews_ltm`

---

## 🔍 O que foi feito

- Verificação de versões das bibliotecas e ambiente
- Inspeção inicial: `shape`, `head().T`, `info()`
- Análise de distribuição por `room_type` com `value_counts()`
- Agregação de preços por tipo de quarto com `groupby()` + `agg()`
- Análise de outliers: quantis, preços zerados e preços extremos
- Ordenações e filtragens com `sort_values()`
- Criação de `df_limpo` excluindo registros com `price == 0` (6 linhas removidas)
- Identificação de outliers com método IQR (Intervalo Interquartil)
- Ranking dos 10 bairros mais caros e 10 mais baratos por média de preço

---

## 🛠️ Stack

| Biblioteca | Versão |
|---|---|
| Python | 3.12.3 |
| pandas | 3.0.6 |
| numpy | 2.5.3 |
| matplotlib | 3.11.2 |
| seaborn | 0.13.2 |

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.12+
- `uv` instalado ([astral.sh/uv](https://astral.sh/uv))

### Passo a passo

```bash
# 1. Clone o repositório
git clone git@github.com:erinardo-data/Projeto-Tecnica-Programacao-Final.git

# 2. Acesse a pasta
cd Projeto-Tecnica-Programacao-Final

# 3. Crie e ative o ambiente virtual
uv venv .venv3.12
source .venv3.12/bin/activate

# 4. Instale as dependências
uv pip install pandas numpy matplotlib seaborn jupyter

# 5. Abra o notebook principal
jupyter notebook Projeto_Final.ipynb
```

---

## 📁 Estrutura do repositório

```
Projeto-Tecnica-Programacao-Final/
├── dados/
│   └── AirbnbRJRentals.csv       # Base de dados — Inside Airbnb RJ
├── notebooks/
│   ├── 2.1_dimensoes_memoria.py
│   ├── 2.2_dados_faltantes.py
│   ├── 2.3_duplicados_inconsistentes.py
│   ├── 2.4_identificacao_outliers.py
│   ├── 3.1_analise_preco.py
│   └── Projeto_Analise_Airbnb.ipynb
├── Projeto_Final.ipynb           # Notebook principal
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 👥 Equipe

- Erinardo Moura Araujo
- Felipe Andrade Santos
