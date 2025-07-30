import streamlit as st

# Función de datos generales de temperatura (2,3,4)
def datos_temperatura():
    
    df = st.session_state["df"]

    col1, col2 , col3 = st.columns(3)

    with col1:
        st.metric("Temperatura Promedio", f"{df["AvgTemperature"].mean():.2f} °F", width= "stretch")
    with col2:
        st.metric("Temperatura Más Baja", f"{df["AvgTemperature"].min():.2f} °F", width= "stretch")
    with col3:
        st.metric("Temperatura Más Alta", f"{df["AvgTemperature"].max():.2f} °F", width= "stretch")

    