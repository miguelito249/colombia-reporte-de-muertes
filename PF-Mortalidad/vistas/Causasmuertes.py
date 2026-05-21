import pandas as pd
import plotly.express as px

def top_causas(df, causas):

    # 1. Limpiar nombres de columnas
    causas.columns = causas.columns.str.strip()

    # 2. Detectar columnas automáticamente (evita errores por espacios/tildes)
    col_codigo = [col for col in causas.columns if "tres caracteres" in col][0]
    col_desc = [col for col in causas.columns if "Descripción" in col and "tres" in col][0]

    # 3. Renombrar
    causas = causas.rename(columns={
        col_codigo: "COD_MUERTE",
        col_desc: "DESCRIPCION"
    })

    causas = causas.drop_duplicates(subset="COD_MUERTE")

    # 4. Agrupar muertes
    df_causas = df.groupby("COD_MUERTE").size().reset_index(name="MUERTES")

    # 5. Limpiar datos
    df_causas["COD_MUERTE"] = df_causas["COD_MUERTE"].astype(str).str.strip().str[:3]
    causas["COD_MUERTE"] = causas["COD_MUERTE"].astype(str).str.strip().str[:3]

    # 6. Unir
    df_final = df_causas.merge(causas, on="COD_MUERTE", how="left")
    df_final = df_final.drop_duplicates(subset="DESCRIPCION")

    # 7. Top 10
    df_top = df_final.sort_values(by="MUERTES", ascending=False).head(10)
    df_top = df_top.dropna(subset=["DESCRIPCION"])

    # 8. Gráfico
    fig = px.bar(
        df_top,
        x="MUERTES",
        y="DESCRIPCION",
        orientation="h",
        text="MUERTES",
        title="Top 10 causas de muerte en Colombia (2019)"
    )

    return fig