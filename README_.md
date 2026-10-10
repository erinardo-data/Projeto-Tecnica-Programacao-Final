Fala pessoal, sobre a organização do nosso repositório Git. Criei e organizei três branches com propósitos específicos:
• main: É a nossa branch principal. Ela contém o código oficial, estável e pronto para produção.
• backup: Criei esta branch (a partir da branch inicial estava aprendendo a mexer no git, inicialmente se chamava limpeza) para servir como um ponto de restauração seguro do código antigo antes das novas mudanças.
• backup_felipe: É a minha branch de trabalho atual, criada hoje (10/10/2026). Ela nasceu como uma cópia exata da main e é onde vou desenvolver minhas tarefas e commits a partir de agora, sem risco de quebrar o código principal.
(Aproveito para avisar que a branch antiga chamada limpeza será deletada do servidor para manter o repositório limpo, essa é a cópia inicial, não tinha gostado do nome).

1. Apresentação da base e das perguntas
A estrutura deste arquivo corresponde ao padrão do **Inside Airbnb**, um projeto independente de código aberto que extrai dados públicos diretamente do site do Airbnb para analisar o impacto dos aluguéis de curta duração nas cidades ao redor do mundo. Este arquivo específico é a versão resumida (`listings.csv`) focada exclusivamente na cidade do Rio de Janeiro, cobrindo 152 bairros.

O arquivo captura o estado da plataforma até o final de 2022. O registro de hospedagens baseado nas datas da última avaliação (`last_review`) abrange o período de **21 de fevereiro de 2012 a 30 de dezembro de 2022**. O indicador de atividades recentes (ltm - *last twelve months*) abrange o ano de 2022.

METADADOS das 16 colunas:

* **id:** Código identificador único do anúncio no sistema do Airbnb.
* **name:** Título do anúncio criado pelo anfitrião.
* **host_id:** Código identificador único do anfitrião na plataforma.
* **host_name:** Nome (ou primeiro nome) do anfitrião.
* **neighbourhood:** Bairro onde a propriedade está localizada.
* **latitude:** Coordenada de latitude para mapeamento.
* **longitude:** Coordenada de longitude para mapeamento.
* **room_type:** Tipo de espaço oferecido (Casa/Apto inteiro, Quarto Privado, Quarto Compartilhado ou Quarto de Hotel).
* **price:** Preço cobrado por uma noite de estadia (em Reais).
* **minimum_nights:** Número mínimo de noites que o hóspede precisa reservar.
* **number_of_reviews:** Quantidade total de avaliações que o anúncio já recebeu ao longo da vida.
* **last_review:** Data em que ocorreu a última avaliação do imóvel.
* **reviews_per_month:** Média de avaliações que o imóvel recebe por mês desde que foi publicado.
* **calculated_host_listings_count:** Quantidade total de anúncios ativos que este mesmo anfitrião possui na cidade (útil para identificar investidores e empresas de gestão imobiliária).
* **availability_365:** Número de dias, dentro de um período de 1 ano (365 dias no futuro a partir da data de extração), em que o imóvel está disponível para reserva.
* **number_of_reviews_ltm:** Total de avaliações recebidas pelo imóvel nos últimos 12 meses.

Perguntas relacionadas com preço e localização.
Qual é a média, a mediana e o valor máximo das diárias na cidade?
Quais são os 10 bairros mais caros e os 10 mais baratos em média?
Quais bairros concentram a maior quantidade de anúncios do Airbnb?

Perguntas relacionadas com demanda.
Imóveis mais populares?
Existem imóveis com melhor custo benefício? Com base em que podemos avaliar isso?

2. Diagnóstico de qualidade
- Dimensões, tipos, uso de memória

Dimensões: 28301 linhas e 16 colunas
Uso de Memória: 11.19 MB

Tipos de dados por coluna:
id                                  int64
name                                  str
host_id                             int64
host_name                             str
neighbourhood                         str
latitude                          float64
longitude                         float64
room_type                             str
price                               int64
minimum_nights                      int64
number_of_reviews                   int64
last_review                           str
reviews_per_month                 float64
calculated_host_listings_count      int64
availability_365                    int64
number_of_reviews_ltm               int64
dtype: object

- Faltantes por coluna (quantidade e percentual)
                   Faltantes (Qtd)  Percentual (%)
reviews_per_month             8518       30.097876
last_review                   8518       30.097876
name                            29        0.102470
host_name                        3        0.010600

- Duplicados, categorias inconsistentes, valores inválidos
Linhas perfeitamente duplicadas: 0
Distribuição de Tipos de Quarto (room_type):
room_type
Entire home/apt    22093
Private room        5685
Shared room          470
Hotel room            53
Name: count, dtype: int64
Anúncios com preço R$ 0 ou negativo: 6
Anúncios com noites mínimas zeradas ou negativas: 0

- Identificação de outliers com método justificado (IQR ou z-score)
Método Justificado: IQR (Intervalo Interquartil)
Q1 (25%): R$ 317.00 | Q3 (75%): R$ 1071.00
Limite Superior de Corte: R$ 2202.00
Total de Outliers encontrados: 2450 anúncios (8.66% da base)