import streamlit as st
import matplotlib.pyplot as plt

# Función que genera el Historigrama (7)
def plot_h():

    fig, ax = plt.subplots()
    df = st.session_state["df"]
    ax.hist(df["AvgTemperature"], color="darkblue", edgecolor= "black")
    ax.set_title("Historigrama")
    ax.set_xlabel("Temperatura (°F)")
    ax.set_ylabel("Frecuencia")
    ax.grid(axis="y", alpha=0.75)

    st.pyplot(fig)

# Función que genera el Grafico de Dispersion (8)
def plot_d():

    fig, ax = plt.subplots()
    df = st.session_state["df"]
    ax.scatter(df["Day"],df["AvgTemperature"], color="blue")
    ax.set_title("Gráfico de dispersión")
    ax.set_xlabel("Dias de Enero")
    ax.set_ylabel("Temperatura (°F)")
    ax.grid(axis="y", alpha=0.75)

    st.pyplot(fig)
