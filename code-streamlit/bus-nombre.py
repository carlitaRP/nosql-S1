import streamlit as st
import pandas as pd

sidebar = st.sidebar
sidebar.markdown("## 🌸 Carlitarp", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("### 💜 S20006731 ISW", unsafe_allow_html=True)
sidebar.markdown("[📧 zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
sidebar.markdown("---")

@st.cache_data
def cargar_datos():
    return pd.read_csv("dataset.csv")

datos = cargar_datos()

def validar_columna():
    if "name" not in datos.columns:
        st.error("El archivo CSV debe contener una columna llamada 'nombre'")
        return False
    return True

if validar_columna():
    st.header("Explorador de Nombres en CSV")
    
    entrada_busqueda = st.text_input("Escriba un nombre o parte de él:", placeholder="Ejemplo: Ana, Pe, Juan")
    
    if entrada_busqueda:
        resultados = datos[datos["name"].str.contains(entrada_busqueda, case=False, na=False)]
        
        st.subheader(f"Resultados encontrados: {len(resultados)}")
        
        st.dataframe(resultados)
    else:
        st.info("Ingrese un término en el campo de búsqueda para visualizar coincidencias.")
