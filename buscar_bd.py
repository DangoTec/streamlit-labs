import streamlit as st
import pandas as pd

st.title("Streamlit - Search Names")

Data_URL="dataset.csv"

@st.cache
def load_data():
    data=pd.read_csv(Data_URL)
    return data

@st.cache
def load_data_bysex(sex):
    filtered_data_bysex=data[data["sex"]==sex]
    return filtered_data_bysex

data=load_data()
selected_sex=st.selectbox("Select sex",data["sex"].unique())
btnFilterbysex=st.button("Filter by sex")

if btnFilterbysex:
    filterbysex=load_data_bysex(selected_sex)
    count_row=filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)