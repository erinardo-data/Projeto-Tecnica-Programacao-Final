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

| Atributo     | Valor                                      |
|--------------|--------------------------------------------|
| Fonte        | [Inside Airbnb — Rio de Janeiro](http://insideairbnb.com/rio-de-janeiro/) |
| Arquivo      | `AirbnbRJRentals.csv`                      |
| Linhas       | 28.301                                     |
| Colunas      | 16                                         |

> ⚠️ O arquivo CSV **não está versionado** neste repositório por ser pesado.
> Baixe-o diretamente em: http://insideairbnb.com/get-the-data/
> Salve como `AirbnbRJRentals.csv` na raiz do projeto antes de rodar o notebook.

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

---

## 🛠️ Stack

| Biblioteca   | Versão  |
|--------------|---------|
| Python       | 3.12.3  |
| pandas       | 3.0.6   |
| numpy        | 2.5.3   |
| matplotlib   | 3.11.2  |
| seaborn      | 0.13.2  |

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.12+
- `uv` instalado ([astral.sh/uv](https://astral.sh/uv))

### Passo a passo

```bash
# 1. Clone o repositório
git clone git@github.com:erinardo-data/Projeto_Final_Tecnicas_de_Programacao_I.git

# 2. Acesse a pasta
cd Projeto_Final_Tecnicas_de_Programacao_I

# 3. Crie e ative o ambiente virtual
uv venv .venv3.12
source .venv3.12/bin/activate

# 4. Instale as dependências
uv pip install pandas numpy matplotlib seaborn jupyter

# 5. Baixe o dataset e salve como AirbnbRJRentals.csv na raiz do projeto

# 6. Abra o notebook
jupyter notebook Projeto_Final.ipynb
```

---

## 📁 Estrutura do repositório

```
Projeto_Final_Tecnicas_de_Programacao_I/
├── Projeto_Final.ipynb       # Notebook principal
├── AirbnbRJRentals.csv       # ⚠️ NÃO versionado — baixar separadamente
├── .gitignore
└── README.md
```

---

## 👥 Equipe

- Erinardo Moura Araujo
- [Nome do colega 2]
- [Nome do colega 3]