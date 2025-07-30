import streamlit as st

# Creamos una clase que contenga la estructura de la pestaña
class ManejoCSV:

    def __init__(self):
        pass

# Cabeza de la ventana
    def header():
        from components.cargar_datos import cargar_csv
        cont1 = st.container(border=True)
        with cont1:
            cargar_csv()
# Contenido
    def body():
        from components.datos_temperatura import datos_temperatura
        from components.cargar_datos import ver_csv
        from components.filtro import filtrar
        if st.session_state.df is not None:
            with st.container(border= True):
                st.subheader("Visualización del Archivo")
                ver_csv()
            with st.container(border=True):
                st.subheader("Datos de Temperatura")
                datos_temperatura()
            with st.container(border=True):
                st.subheader("Filtrado de Datos")
                filtrar()
        else:
            st.warning("No hay ningún archivo cargado, por favor, cargue el archivo", icon="💾")
