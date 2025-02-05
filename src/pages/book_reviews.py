import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amazon Top 100 Treending Books", layout="wide")

df_customers_review = pd.read_csv('datasets/customers_review.csv')
df_top100_trending_books = pd.read_csv('datasets/top100_trending_books.csv')

list_books = df_top100_trending_books["book title"].unique()
selected_book = st.sidebar.selectbox("**Select a book**", list_books)

rating_max = df_customers_review["reviewer rating"].max()
rating_min = df_customers_review["reviewer rating"].min()

max_rating = st.sidebar.slider("Reviewer Rating", rating_min, rating_max, rating_max)

df_book = df_top100_trending_books[df_top100_trending_books["book title"] == selected_book]
df_reviews_filter = df_customers_review[df_customers_review["book name"] == selected_book]

book_title = df_book["book title"].iloc[0] 
book_genre = df_book["genre"].iloc[0] 
book_price = df_book["book price"].iloc[0] 
book_rating = df_book["rating"].iloc[0] 
book_year = df_book["year of publication"].iloc[0] 

st.title(f":blue[Book:] {book_title}")
st.subheader(f":blue[Genre:] {book_genre}")

col1, col2, col3 = st.columns(3)

col1.metric(":green[Price]", f"US$ {book_price}", border=True)
col2.metric(":red[Rating]", book_rating, border=True)
col3.metric("Year", book_year, border=True)

st.divider()

if df_reviews_filter.empty:
  st.error("No reviews found for this book :/")
else:
  df_ratings = df_reviews_filter[df_reviews_filter["reviewer rating"] >= max_rating]
  df_ratings.sort_index(ascending=False)
  for row in df_ratings.values:
    message = st.chat_message(f"{row[4]}")
    message.metric(f"**:blue[Reviewer:]** {row[3]}", f"{row[2]}")
    message.write(f"**Description:** {row[5]}")