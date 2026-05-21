import pandas as pd
import plotly.express as px

def grafico_lineas(df):
    # Agrupar por mes
    df_mes = df.groupby("MES").size().reset_index(name="MUERTES")

    # Ordenar meses
    df_mes = df_mes.sort_values("MES")

    # Crear gráfico
    fig = px.line(
        df_mes,
        x="MES",
        y="MUERTES",
        title="Muertes por mes en Colombia (2019)"
    )

    return fig