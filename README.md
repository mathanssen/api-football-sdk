# Alts Digital - API Football

Este projeto utiliza a **API Football** para capturar e analisar dados de diferentes competições de futebol, incluindo **Libertadores**, **Copa do Brasil** e **Sulamericana**. O objetivo é criar um conteúdo baseado em estatísticas para apostadores e gerar insights relevantes sobre as competições.

## Estrutura do Projeto

- `api_football/`
  - `src/`: Contém o código-fonte principal para chamadas de API e utilitários.
    - `fixtures.py`: Lida com fixtures de futebol (jogos, resultados).
    - `leagues.py`: Gerencia dados das ligas.
    - `config.py`: Configurações de API.
    - `utils.py`: Funções auxiliares, como requisições à API.
    - `exporters/`: Módulo para exportar dados para formatos como CSV.
  - `tests/`: Contém os arquivos de teste unitário para as funcionalidades implementadas.
  - `notebooks/`: Notebooks Jupyter para análise exploratória dos dados.
  - `requirements.txt`: Lista de bibliotecas necessárias para rodar o projeto.

## Requisitos

- Python 3.8+
- Instalar as dependências:
```bash
  pip install -r requirements.txt
```

## Uso

1. Configure sua chave da API no arquivo `config.py`.
2. Utilize as funções em `src` para capturar dados de competições, exportar para CSV e realizar análises.
3. Para rodar os testes:
```bash
   python -m unittest discover -s api_football/tests
```

## Exportando Dados

O módulo `csv_exporter` localizado em `src/exporters` pode ser utilizado para exportar dados capturados da API para arquivos CSV.

### Exemplo de Uso

```python
from api_football.src.exporters.csv_exporter import export_fixtures_data_to_csv


# Exportar dados dos jogos da Libertadores 2024 para um arquivo CSV
export_fixtures_data_to_csv(13, "2024", "libertadores_2024.csv")
```

Essa função gera um arquivo CSV contendo informações sobre os jogos, como times, gols, cartões e escanteios.

Para mais detalhes sobre como utilizar outras funções de exportação, consulte os arquivos no diretório src/exporters.

## Análises no Jupyter Notebooks

Você pode utilizar o diretório `notebooks` para realizar análises mais aprofundadas utilizando os dados exportados em CSV. Exemplos de análise incluem:

- **Média de Gols**: Análise de gols marcados nas competições da Libertadores, Copa do Brasil e Sulamericana.
- **Média de Escanteios e Cartões**: Investigação sobre padrões de cartões e escanteios por fase de competição.
- **Análise de Acréscimos**: Tendência no aumento do tempo de acréscimos.

Exemplo de importação de dados em um notebook:

```python
import pandas as pd

df = pd.read_csv("libertadores_2024_fixtures.csv")
df.head()
```

Esses notebooks são usados para gerar insights detalhados e auxiliar na criação de conteúdo para apostadores.