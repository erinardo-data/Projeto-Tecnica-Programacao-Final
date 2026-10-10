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