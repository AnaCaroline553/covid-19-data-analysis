import pandas as pd
import matplotlib.pyplot as plt
import requests

# URL de um conjunto de dados simples da COVID-19 (exemplo)
# Você pode substituir por um link de dados mais atualizado ou de sua preferência
DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
FILE_NAME = "covid_data.csv"

def download_data(url, filename):
    """Baixa o arquivo CSV do URL especificado."""
    print(f"Baixando dados de: {url}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Dados baixados e salvos como {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar os dados: {e}")
        exit()

def analyze_data(filepath):
    """
    Carrega os dados e realiza análises básicas.
    """
    print(f"Analisando dados de: {filepath}")
    try:
        df = pd.read_csv(filepath)

        # Exibe as primeiras linhas do dataframe
        print("\nPrimeiras 5 linhas do DataFrame:")
        print(df.head())

        # Informações gerais sobre o dataframe
        print("\nInformações do DataFrame:")
        df.info()

        # Seleciona dados de um país específico (exemplo: Brazil)
        country_data = df[df['location'] == 'Brazil']

        if not country_data.empty:
            print("\nDados de COVID-19 no Brasil (últimas 5 entradas):")
            print(country_data[['date', 'total_cases', 'new_cases', 'total_deaths']].tail())

            # Plotar total de casos no Brasil ao longo do tempo
            plt.figure(figsize=(12, 6))
            plt.plot(pd.to_datetime(country_data['date']), country_data['total_cases'], label='Total de Casos')
            plt.plot(pd.to_datetime(country_data['date']), country_data['new_cases'], label='Novos Casos Diários')
            plt.title('Evolução dos Casos de COVID-19 no Brasil')
            plt.xlabel('Data')
            plt.ylabel('Número de Casos')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('total_cases_brazil.png')
            print("\nGráfico 'total_cases_brazil.png' gerado com sucesso.")
            # plt.show() # Descomente para exibir o gráfico imediatamente

            # Plotar total de mortes no Brasil ao longo do tempo
            plt.figure(figsize=(12, 6))
            plt.plot(pd.to_datetime(country_data['date']), country_data['total_deaths'], color='red', label='Total de Mortes')
            plt.title('Evolução das Mortes por COVID-19 no Brasil')
            plt.xlabel('Data')
            plt.ylabel('Número de Mortes')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('total_deaths_brazil.png')
            print("Gráfico 'total_deaths_brazil.png' gerado com sucesso.")
            # plt.show() # Descomente para exibir o gráfico imediatamente
        else:
            print(f"Não foram encontrados dados para 'Brazil' no conjunto de dados.")

    except FileNotFoundError:
        print(f"Erro: O arquivo {filepath} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a análise dos dados: {e}")

if __name__ == "__main__":
    download_data(DATA_URL, FILE_NAME)
    analyze_data(FILE_NAME)
