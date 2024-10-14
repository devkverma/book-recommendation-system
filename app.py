import streamlit as st
import pandas as pd
import pickle

with open("books.pkl","rb") as file:
    books_dict = pickle.load(file)

books = pd.DataFrame(books_dict)

with open("sm.pkl","rb") as file:
    similarities = pickle.load(file)

def recommend(bookName):
    index = books.index[books['title'] == bookName][0]
    book_indices = []
    for i,sim in sorted(enumerate(similarities[index]),reverse=True,key=lambda x:x[1])[1:6]:
        book_indices.append(i)
    book_list = []
    for i in book_indices:
        book_list.append(books['title'][i])
    return book_list

st.title("Books Recommendation System")

option = st.selectbox(
    "Choose a Book",
    books['title']
)

_, mid_col, _ = st.columns(3)

if mid_col.button("Recommend"):
    book_list = recommend(option)

    col0, col1, col2, col3, col4 = st.columns(5)

    col = {0:col0, 1:col1, 2:col2, 3:col3, 4:col4}

    for i,book in enumerate(book_list):
        col[i].write(book)