#Importação da base de dados com biblioteca pandas
import pandas as pd

#.to_string() serve para ver mais linhas da planilha
tabela_vendas = pd.read_excel(r"C:\Users\nicol\OneDrive\Desktop\Datasets\Vendas+-+Base+de+Dados.xlsx")
print(tabela_vendas)

#calculando, filtrando e ordenando dados
tab_quantidade_vendida = tabela_vendas.groupby('Produto').sum()
tab_quantidade_vendida = tab_quantidade_vendida[['Quantidade', 'Valor Unitário']]

#sort_values e Ascending função para organizar a ordem, true(menor para o maior) false(maior para o menor)
tab_quantidade_vendida = tab_quantidade_vendida.sort_values(by='Quantidade', ascending=False)
print(tab_quantidade_vendida)
#calculando produtos mais vendidos em faturamento
tabela_vendas['Faturamento'] = tabela_vendas['Quantidade'] * tabela_vendas['Valor Unitário']
tb_faturamento_produto = tabela_vendas.groupby('Produto').sum()
tb_faturamento_produto = tb_faturamento_produto[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tb_faturamento_produto)
#calcular a loja/estado que mais vendeu em faturamento
tb_faturamento_loja = tabela_vendas.groupby('Loja').sum()
tb_faturamento_loja = tb_faturamento_loja[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tb_faturamento_loja)