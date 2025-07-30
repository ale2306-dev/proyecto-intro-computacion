import streamlit as st
import pandas as pd

#Función para cargar csv (1)
def cargar_csv():

    if "df" not in st.session_state:
        st.session_state.df = None

    if st.session_state.df is not None:
        st.success("El archivo se ha cargado correctamente", icon="💾")
    else:
        archivo = st.file_uploader("Cargar Archivo CSV", ["csv"])
        if archivo != None:
            df = pd.read_csv(archivo)
            st.session_state.df = df
            st.success("Archivo Cargado con Exito", icon="💾")

#Función para ver csv (9)
def ver_csv():

        df = st.session_state["df"]

        st.dataframe(df)