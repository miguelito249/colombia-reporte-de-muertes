import pandas as pd
import plotly.express as px

def muertes_por_edad(df):

    # Diccionario de categorías
    categorias = {
        (0, 4): "Neonatal",
        (5, 6): "Infantil",
        (7, 8): "Primera infancia",
        (9, 10): "Niñez",
        (11, 11): "Adolescencia",
        (12, 13): "Juventud",
        (14, 16): "Adultez temprana",
        (17, 19): "Adultez intermedia",
        (20, 24): "Vejez",
        (25, 28): "Longevidad",
        (29, 29): "Edad desconocida"
    }

    # Función para clasificar
    def clasificar_edad(valor):
        for (min_, max_), nombre in categorias.items():
            if min_ <= valor <= max_:
                return nombre
        return "Otro"

    # Aplicar clasificación
    df["GRUPO_EDAD_CAT"] = df["GRUPO_EDAD1"].apply(clasificar_edad)

    # Agrupar
    df_edad = df.groupby("GRUPO_EDAD_CAT").size().reset_index(name="MUERTES")

    # Gráfico
    fig = px.bar(
        df_edad,
        x="GRUPO_EDAD_CAT",
        y="MUERTES",
        title="Distribución de muertes por grupo de edad"
    )

    return fig