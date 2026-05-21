import pandas as pd
import plotly.express as px

def ciudades_mas_violentas(df, divipola):

    # 🔥 FILTRAR SOLO HOMICIDIOS (X95)
    df_homicidios = df[df["COD_MUERTE"].astype(str).str.startswith("X95")]

    # 🔥 AGRUPAR POR COD_DANE (CLAVE)
    df_ciudad = df_homicidios.groupby("COD_DANE").size().reset_index(name="MUERTES")

    # Unir con nombres
    divipola_mun = divipola[["COD_DANE", "MUNICIPIO"]].drop_duplicates()

    df_final = df_ciudad.merge(divipola_mun, on="COD_DANE", how="inner")

    # 🔥 TOP 5 MÁS VIOLENTAS
    df_top = df_final.sort_values(by="MUERTES", ascending=False).head(5)

    # Gráfico de barras
    fig = px.bar(
        df_top,
        x="MUNICIPIO",
        y="MUERTES",
        title="Top 5 ciudades más violentas (homicidios por arma de fuego)",
        color="MUERTES"
    )

    return fig