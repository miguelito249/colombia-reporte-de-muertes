import pandas as pd
import plotly.express as px
import json

def mapa_departamentos(df, divipola):

    # 1. Agrupar muertes por departamento
    df_dep = df.groupby("COD_DEPARTAMENTO").size().reset_index(name="MUERTES")

    # 2. Unir con nombres de departamentos
    divipola_dep = divipola[["COD_DEPARTAMENTO", "DEPARTAMENTO"]].drop_duplicates()
    df_final = df_dep.merge(divipola_dep, on="COD_DEPARTAMENTO", how="left")

    # 3. Convertir nombres a mayúsculas (para que coincidan con GeoJSON)
    df_final["DEPARTAMENTO"] = df_final["DEPARTAMENTO"].str.upper()

    # 4. Cargar el geojson
    with open("Mapgeoj/mapacol.geojson", encoding="utf-8") as f:
        geojson = json.load(f)

    # 5. Crear mapa
    fig = px.choropleth(
        df_final,
        geojson=geojson,
        locations="DEPARTAMENTO",
        featureidkey="properties.NOMBRE_DPT",
        color="MUERTES",
        hover_name="DEPARTAMENTO",
        title="Muertes por departamento en Colombia (2019)"
    )

    # 6. Ajustar vista del mapa
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    return fig