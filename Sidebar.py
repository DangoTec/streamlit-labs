import streamlit as st
import numpy as np
import pandas as pd

# Crear el título para la aplicación web
st.title("Mi Primera App con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")


st.header("Información sobre el Conjunto de Datos")

st.header("Descripción de los datos ")

st.write("""
Este es un simple ejemplo de una app para predecir

¡Esta app predice mis datos!

""")

if sidebar.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=["a","b","c"])

    st.dataframe(chart_data)