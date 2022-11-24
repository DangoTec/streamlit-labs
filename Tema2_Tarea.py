import pandas as pd
import streamlit as st
import datetime

data_link = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv '
data = pd.read_csv(data_link)

# Create the title for the web app
st.title("""Tema 2: Tarea 
        Daniel Porras A00827490""")
st.write("Proyecto de visualización de analítica de datos para WalMart USA")

# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(data)
st.markdown("___")

# radio 
selected_class = st.sidebar.radio("Select Class", data['Ship Mode'].unique())
st.write("Selected Class:", selected_class)
db1=data[data["Ship Mode"]==selected_class]

# Select discount
optionals = st.sidebar.expander("Descuento", True)
fare_min = optionals.slider(
    "Discount",
    min_value=float(db1['Discount'].min()),
    max_value=float(db1['Discount'].max())
)
db1=db1[db1["Discount"]>=fare_min]

#Select Category
selected_Cat = st.sidebar.selectbox("Select Category", db1['Category'].unique())
st.write(f"Selected Option: {selected_Cat!r}")
db2=db1.query(f"""Category==@selected_Cat""")
st.write(db2)
st.write(f"Number of records with {fare_min} discount en {selected_Cat}:{db2.shape[0]}")
st.markdown("___")
