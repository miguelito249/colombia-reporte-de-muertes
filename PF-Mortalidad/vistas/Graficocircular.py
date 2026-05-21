import pandas as pd
import plotly.express as px

def ciudades_menor_mortalidad(df, divipola):

    # 🔥 AGRUPAR POR COD_DANE (CLAVE)
    df_ciudad = df.groupby("COD_DANE").size().reset_index(name="MUERTES")

    # Unir con nombres
    divipola_mun = divipola[["COD_DANE", "MUNICIPIO"]].drop_duplicates()

    df_final = df_ciudad.merge(divipola_mun, on="COD_DANE", how="inner")

    # Limpiar
    df_final = df_final.dropna(subset=["MUNICIPIO"])

    # Evitar ruido
    df_final = df_final[(df_final["MUERTES"] >= 5) & (df_final["MUERTES"] <= 20)]

    # Top 10 menor mortalidad
    df_bottom = df_final.sort_values(by="MUERTES", ascending=True).head(10)

    # Gráfico
    fig = px.pie(
        df_bottom,
        names="MUNICIPIO",
        values="MUERTES",
        title="10 ciudades con menor número de muertes"
    )

    return fig