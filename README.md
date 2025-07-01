# Análise Simplificada de Dados da COVID-19

Este projeto em Python é uma demonstração básica de como manipular e visualizar dados da COVID-19. Ele baixa um conjunto de dados público, realiza algumas análises exploratórias simples e gera gráficos para visualização.

**Objetivo:**

O objetivo principal deste projeto é demonstrar minhas habilidades básicas em:
* **Python:** Leitura, manipulação e análise de dados.
* **Bibliotecas Comuns:** Uso de `pandas` para manipulação de dados, `matplotlib` para visualização e `requests` para download de arquivos.
* **Organização de Projetos:** Estrutura de um projeto Python e uso de `requirements.txt`.
* **Controle de Versão:** Familiaridade com o Git e GitHub para gerenciar o código.

---

## Como Executar

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/SEU_USUARIO/covid-19-data-analysis.git](https://github.com/SEU_USUARIO/covid-19-data-analysis.git)
    cd covid-19-data-analysis
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script principal:**

    ```bash
    python main.py
    ```

    Ao executar o script, ele fará o download do arquivo CSV com os dados da COVID-19, realizará a análise e gerará dois gráficos (`total_cases_brazil.png` e `total_deaths_brazil.png`) na mesma pasta do projeto.

---

## Saída Esperada

O script irá imprimir informações básicas sobre o conjunto de dados no console e gerar os seguintes arquivos de imagem:

* `total_cases_brazil.png`: Gráfico da evolução do total e novos casos de COVID-19 no Brasil.
* `total_deaths_brazil.png`: Gráfico da evolução do total de mortes por COVID-19 no Brasil.

---

## Melhorias Futuras (Ideias para você explorar)

* Adicionar mais opções de países para análise.
* Implementar filtros por período de tempo.
* Calcular métricas adicionais (ex: taxa de letalidade).
* Utilizar bibliotecas de visualização mais avançadas como `seaborn` ou `plotly`.
* Adicionar testes unitários.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir "issues" ou "pull requests" com sugestões de melhoria ou correções.
