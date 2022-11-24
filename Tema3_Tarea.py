import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as plt
import plotly.express as px

data_link = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv '
data = pd.read_csv(data_link)

# Create the title for the web app
st.title("""Tema 3: Tarea 
        Daniel Porras A00827490""")
st.write("Proyecto de visualización de analítica de datos para WalMart USA")

#Histograma
fig, ax = plt.subplots()
ax.hist(data["Category"])
st.header("Histograma de datos - Cantidad de productos por categorías")
st.pyplot(fig)
st.markdown("___")

#Barras
fig2, ax2 = plt.subplots()

y_pos = data['Category']
x_pos = data['Sales']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Category")
ax2.set_xlabel("Sales")

st.header("Grafica de Barras - Ventas por categoría")
st.pyplot(fig2)
st.markdown("___")

#Pastel
fig3=px.pie(data,names="Ship Mode")

st.header("Grafica de Pastel - Dispersión de Ship Mode")
st.plotly_chart(fig3)