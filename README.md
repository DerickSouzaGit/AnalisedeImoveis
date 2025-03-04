# Análise de Dados Imobiliários: DF e SP

Este projeto foi desenvolvido com o intuito de **estudar e aprender sobre análise de dados** aplicados ao mercado imobiliário, utilizando duas bases de dados obtidas do Kaggle. O foco está na exploração dos preços dos imóveis, bem como na relação desses preços com variáveis como área, número de quartos, tipo de imóvel e bairro.

---

## Objetivo

- **Investigar a distribuição dos preços** dos imóveis e identificar padrões que possam ser relevantes para compradores, investidores e interessados no mercado.
- **Analisar as relações** entre o preço e outras variáveis (ex.: área, quartos, tipo de imóvel e bairro) utilizando técnicas de limpeza e visualização de dados.

---

## Metodologia

### 1. Coleta de Dados

- **Distrito Federal (DF):**  
  - Base de dados: `dados/ImóveisDF.csv` (com separador `;`).
- **São Paulo (SP):**  
  - Base de dados: `dados/ImóveisSP.csv`.

### 2. Preparação e Limpeza dos Dados

- **Conversão de Variáveis:**  
  - Converte colunas como preço, área, quartos, etc., para formato numérico usando `pd.to_numeric`.
  - Converte colunas de datas (no dataset de SP) para o tipo `datetime`.
- **Tratamento de Valores Nulos:**  
  - Preenche os valores faltantes com a mediana dos respectivos campos.
- **Filtragem:**  
  - Remove registros com preços ou áreas menores ou iguais a zero.

### 3. Análise Exploratória

- **Estatísticas Descritivas:**  
  - Utiliza o método `describe()` para sumarizar os dados.
- **Visualizações:**  
  - **Histograma:** Exibe a distribuição dos preços.
  - **Gráficos de Barras:**  
    - Para o DF: Compara o preço médio por tipo de imóvel e por bairro.
    - Para SP: Analisa o preço médio em relação ao número de quartos.

---

## Resultados

### Distrito Federal (DF)

- **Distribuição dos Preços:**  
  - Exibida através de um histograma, evidenciando a frequência e dispersão dos preços.
- **Preço Médio por Tipo e Bairro:**  
  - Gráficos de barras demonstram a variação do preço médio de acordo com o tipo de imóvel e o bairro.

### São Paulo (SP)

- **Distribuição dos Preços:**  
  - Histograma que mostra a frequência dos preços.
- **Preço Médio por Número de Quartos:**  
  - Gráfico de barras que relaciona o número de quartos com o preço médio dos imóveis.

---

## Instruções de Execução

### Pré-requisitos

Certifique-se de ter o [Python 3.x](https://www.python.org/) instalado e as seguintes bibliotecas:

- pandas
- matplotlib
- seaborn

Você pode instalar as dependências utilizando o arquivo `requirements.txt`:

```txt
pandas
matplotlib
seaborn
