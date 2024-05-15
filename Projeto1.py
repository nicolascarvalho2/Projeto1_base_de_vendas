#Importação da base de dados com biblioteca pandas
import pandas as pd

tabela_vendas = pd.read_excel(r"C:\Users\nicol\OneDrive\Desktop\Datasets\Vendas+-+Base+de+Dados.xlsx")
print(tabela_vendas.to_string())
#calculando filtrando e ordenando dados
tab_quantidade_vendida = tabela_vendas.groupby('Produto').sum()
tab_quantidade_vendida = tab_quantidade_vendida[['Quantidade', 'Valor Unitário']]
print(tab_quantidade_vendida)