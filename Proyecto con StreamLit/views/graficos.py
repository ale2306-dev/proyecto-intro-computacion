import streamlit as st
# Creamos una clase que contenga la estructura de la pestaña
class Graficos:

    def __init__(self):
        pass

# Cabeza de pestaña
    def header():
        st.header("Graficos Relevantes")
# Contenido de pestaña
    def body():
        if st.session_state.df is not None:
            from components.plots import plot_d,plot_h
            st.subheader("Historigrama")
            plot_h()
            st.subheader("Gráfico de Dispersión")
            plot_d()
        else:
            st.warning("Aún no se ha cargado ningún archivo", icon="❗")