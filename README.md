# Projeto: Análise de Dados Geoespaciais de Acidentes de Trânsito

### Introdução

Este projeto consiste na análise de um grande conjunto de dados de acidentes de trânsito nos Estados Unidos. O objetivo é identificar áreas de alto risco, padrões de acidentes e visualizar esses dados em um mapa interativo para obter insights que podem auxiliar na segurança viária.

### Tecnologias Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas e ferramentas:

* **Pandas:** Para manipulação e limpeza dos dados.
* **Folium:** Para a criação de mapas interativos.
* **Matplotlib:** Para visualizações complementares.
* **Jupyter Notebook:** Para a documentação e execução interativa da análise.
* **Git & GitHub:** Para controle de versão e hospedagem do projeto.

### Estrutura do Projeto

A estrutura de pastas foi organizada para manter o projeto limpo e organizado:


├── data/
│   └── US_Accidents_March23.csv
├── notebooks/
│   └── analise_acidentes.ipynb
├── reports/
│   └── mapa_acidentes.html
└── scripts/
└── visualizacao_geoespacial.py


### Análise e Resultados

#### 1. Limpeza e Pré-processamento

A etapa de limpeza dos dados incluiu:
-   Carregamento de um subconjunto de colunas essenciais para a análise geoespacial (`Start_Lat`, `Start_Lng`, `Severity`, `City`).
-   Remoção de linhas com valores ausentes de latitude e longitude para garantir que todos os pontos pudessem ser plotados no mapa.
-   Criação de uma amostra menor do dataset original para permitir que a visualização seja rápida e eficiente.

#### 2. Visualização de Padrões Geoespaciais

O mapa interativo gerado com a biblioteca Folium revelou os seguintes insights:
-   **Distribuição de Acidentes:** O mapa mostra visualmente as áreas com maior densidade de acidentes, permitindo a identificação imediata de pontos críticos.
-   **Severidade:** Os marcadores no mapa podem ser usados para indicar a severidade dos acidentes, ajudando a priorizar áreas para ações de segurança.
-   **Análise por Cidade:** O mapa permite filtrar e visualizar acidentes em cidades específicas, o que é útil para análises mais detalhadas.

### Como Executar o Projeto

1.  **Clone o repositório:**
    `git clone https://github.com/dencode7/analise-acidentes.git`
2.  **Navegue para a pasta do projeto:**
    `cd analise-acidentes`
3.  **Instale as dependências necessárias:**
    `pip install -r requirements.txt` (ou instale manualmente `pandas`, `folium`, `matplotlib`).
4.  **Inicie o Jupyter Notebook:**
    `jupyter notebook`
5.  Abra o arquivo `notebooks/analise_acidentes.ipynb` para ver a análise completa e interativa.
