import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="App de Gastos Personales",
    page_icon="💰",
    layout="wide"
)

st.title("App de Gastos 💸")

df = pd.read_csv("gastos.csv")

df["fecha"] = pd.to_datetime(df["fecha"])

# Mostrar datos
st.subheader("Datos")
st.dataframe(df)

# Gasto total
gasto_total = df["monto"].sum()
st.subheader("Gasto Total")
st.write(f"${gasto_total}")

# Agrupar por categoría
gasto_categoria = df.groupby("categoria")["monto"].sum()

# Gráfico de barras
st.subheader("Gastos por Categoría")
fig1, ax1 = plt.subplots()
gasto_categoria.plot(kind="bar", ax=ax1)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# Gráfico de torta
st.subheader("Distribución de Gastos")
fig2, ax2 = plt.subplots()
gasto_categoria.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
plt.tight_layout()
st.pyplot(fig2)
