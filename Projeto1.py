#Importação da base de dados com biblioteca pandas
import pandas as pd

tabela_vendas = pd.read_excel(r"C:\Users\nicol\OneDrive\Desktop\Datasets\Vendas+-+Base+de+Dados.xlsx")
print(tabela_vendas) #.to_string() serve para ver mais linhas da planilha
#calculando, filtrando e ordenando dados
tab_quantidade_vendida = tabela_vendas.groupby('Produto').sum()
tab_quantidade_vendida = tab_quantidade_vendida[['Quantidade', 'Valor Unitário']]
tab_quantidade_vendida = tab_quantidade_vendida.sort_values(by='Quantidade', ascending=False)
print(tab_quantidade_vendida)