import pandas as pd
import plotly.express as px

def muertes_sexo_departamento(df, divipola):

    # Agrupar por departamento y sexo
    df_group = df.groupby(["COD_DEPARTAMENTO", "SEXO"]).size().reset_index(name="MUERTES")

    # Unir con nombres de departamento
    divipola_dep = divipola[["COD_DEPARTAMENTO", "DEPARTAMENTO"]].drop_duplicates()
    df_final = df_group.merge(divipola_dep, on="COD_DEPARTAMENTO", how="left")

    # Cambiar valores de sexo
    df_final["SEXO"] = df_final["SEXO"].replace({
        1: "Masculino",
        2: "Femenino"
    })

    # Crear gráfico de barras apiladas
    fig = px.bar(
        df_final,
        x="DEPARTAMENTO",
        y="MUERTES",
        color="SEXO",
        title="Muertes por sexo en cada departamento",
        barmode="stack"
    )

    return fig