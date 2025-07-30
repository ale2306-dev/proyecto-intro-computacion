import streamlit as st

st.title("Explorador de Datos Climáticos")

#Creación de pestañas
tab1, tab2 = st.tabs(["Datos", "Gráficos"])

with tab1:
    from views.manejo_csv import ManejoCSV as tab
    #Contenido de la primera pestaña
    tab.header()
    tab.body()
with tab2:
    from views.graficos import Graficos as tab
    #Contenido de la segunda pestaña
    tab.header()
    tab.body()