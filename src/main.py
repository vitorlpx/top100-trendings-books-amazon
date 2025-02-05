import streamlit as st
import pandas as pd
import plotly.express as px

# Config da página do streamlit
st.set_page_config(page_title="Amazon Top 100 Treending Books", layout="wide")

# Carregando os dados
dt_customers_review = pd.read_csv('datasets/customers_review.csv')
dt_top100_trending_books = pd.read_csv('datasets/top100_trending_books.csv')

# Pegando o preço máximo e mínimo dos livros
price_max = dt_top100_trending_books["book price"].max()
price_min = dt_top100_trending_books["book price"].min()

# Sidebar com slider para filtrar os livros por preço
max_price = st.sidebar.slider("Prince Range", price_min, price_max, price_max)

# Exibindo os dados juntamente com o filtro de preço com slider
df_books = dt_top100_trending_books[dt_top100_trending_books["book price"] <= max_price]
# Estamos acessando o dataset dt_top100_trending_books, verificando a tabela de preço dos livros e filtrando os livros que estão dentro do range de preço.
st.title("Top 100 trending books on Amazon!")
df_books

st.title("Graphs")
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)
