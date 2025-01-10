"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os


def convertir_a_formato_fecha(fecha):
    try:
        return pd.to_datetime(fecha, format="%d/%m/%Y")
    except:
        return pd.to_datetime(fecha, format="%Y/%m/%d")


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    # Cargar los datos
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")

    df = df.copy()
    df = df.dropna()
    df = df.drop(columns=["Unnamed: 0"])
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["barrio"] = df["barrio"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["estrato"] = df["estrato"].astype(int)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(convertir_a_formato_fecha)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"[^\d.]", "", regex=True
    )
    df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df = df.drop_duplicates()

    # si la carpeta ouput no existe, la crea
    if not os.path.exists("files/output"):
        os.makedirs("files/output")

    # Guardar el archivo limpio
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)


pregunta_01()
