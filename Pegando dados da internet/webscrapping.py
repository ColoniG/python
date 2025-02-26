import pandas as pd
                                                          # TABELAS -> Dataframes (no Python)
# Extrai os dados da tabela a partir do link da Web.
tabelas_tudo = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria")

# Lista com as tabelas
  ###print(tabelasTudo)

# Pegando a primeira tabela da lista
tabela = tabelas_tudo[0]

# Visualizando tabela
   ###print(tabela)

# Filtro a tabela com as colunas que eu quero
tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]
   ###print(tabela_filtrada)
   ###tabela_filtrada.info()

# Trato meus dados e tranformo em valores numéricos
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(" ", "")

#  Aqui fiz uma gambiarra - estavadando  erro ao colocar   '.astype("int64")'  acima
tabela_filtrada["Bilheteria (US$)"] = pd.to_numeric(tabela_filtrada["Bilheteria (US$)"], errors='coerce')
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].astype("Int64")

'''
print("#" * 150, "\n")
tabela_filtrada.info()
print("#" * 150, "\n")
print(tabela_filtrada)
print("#" * 150, "\n")  '''

# Faço o agrupamento por diretor
tabela_filtrada.groupby("Diretor(a)")