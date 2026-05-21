import pandas as pd
import streamlit as st
@st.cache_data
def cargar_datos():
    df = pd.read_excel("datos/NoFetal2019.xlsx")
    divipola = pd.read_excel("datos/Divipola.xlsx")
    causas = pd.read_excel("datos/CodigosDeMuerte.xlsx", skiprows=8)
    return df, divipola, causas
