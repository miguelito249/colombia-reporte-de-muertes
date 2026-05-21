import streamlit as st


@st.cache_data
def cargar_datos():
    # Añadimos la subcarpeta 'PF-Mortalidad' al inicio de cada ruta
    df = pd.read_excel("PF-Mortalidad/datos/NoFetal2019.xlsx")
    divipola = pd.read_excel("PF-Mortalidad/datos/Divipola.xlsx")
    causas = pd.read_excel("PF-Mortalidad/datos/CodigosDeMuerte.xlsx", skiprows=8)
    return df, divipola, causas