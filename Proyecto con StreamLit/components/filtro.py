import streamlit as st


#Función de filtrado (5,6)
def filtrar():
    
    df = st.session_state.df

    num = round(st.number_input("Limite de la temperatura (°F)", df["AvgTemperature"].min(), df["AvgTemperature"].max()), 2)

    col1, col2 = st.columns(2)

    if col1.button(f"Filtrar Por Debajo de {num} °F"):
        df_filt = df[df["AvgTemperature"] <= num]

        st.dataframe(df_filt)
    if col2.button(f"Filtrar Por Arriba de {num} °F"):
        df_filt = df[df["AvgTemperature"]>= num]

        st.dataframe(df_filt)
