import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def cargar_datos(n_registros=1000):
    try:
        df = pd.read_csv("bike/citibike.csv", encoding="utf-8", nrows=n_registros)
    except UnicodeDecodeError:
        df = pd.read_csv("bike/citibike.csv", encoding="latin1", nrows=n_registros)
    
    df.rename(columns={"start_lat": "lat", "start_lng": "lon"}, inplace=True)
    df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")
    
    return df

df = cargar_datos()

st.title("💜 Análisis de recorridos en bicicleta 🚲")

sidebar = st.sidebar
sidebar.markdown("<h2 style='text-align: center; color: #A32CC4;'>🌸 Carlitarp</h2>", unsafe_allow_html=True)
st.sidebar.image("https://raw.githubusercontent.com/carlitaRP/nosql-S1/master/bike/carlita.jpg", width=160)
sidebar.markdown("<h4 style='text-align: center; color: #A32CC4;'>💜 S20006731 ISW</h4>", unsafe_allow_html=True)
st.sidebar.markdown("### 📩 Contacto")
st.sidebar.markdown("[✉️ zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
st.sidebar.markdown("______")
st.sidebar.markdown("<h3 style='color: #A32CC4;'>⚙️ Opciones de Visualización</h3>", unsafe_allow_html=True)

mostrar_todos = st.sidebar.checkbox("Mostrar todos los registros")
if mostrar_todos:
    st.markdown("<h4 style='color: #A32CC4;'>📋 Total de registros recuperados</h4>", unsafe_allow_html=True)
    st.write(f"Total de registros: {len(df)}")
    st.dataframe(df)
    st.markdown("______")

mostrar_grafica = st.sidebar.checkbox("📊 Mostrar gráfica de recorridos", value=False)

st.sidebar.markdown("<h3 style='color: #A32CC4;'>📌 Gráfica de recorridos por hora</h3>", unsafe_allow_html=True)

df["hour"] = df["started_at"].dt.hour
conteo_horas = df["hour"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(conteo_horas.index, conteo_horas.values, color="#A32CC4")  # 💜 Cambio de color
ax.set_xlabel("Hora del día - 24hrs")
ax.set_ylabel("Número de recorridos")

hora_seleccionada = st.sidebar.slider("⏰ Seleccione una hora del día", min_value=0, max_value=23, value=12)

df_filtrado = df[df["hour"] == hora_seleccionada]

st.markdown(f"<h4 style='color: #A32CC4;'>🗺️ Mapa de recorridos iniciados a las {hora_seleccionada}:00 hrs</h4>", unsafe_allow_html=True)
st.map(df_filtrado)

st.markdown("____")

if mostrar_grafica:
    st.markdown("<h3 style='color: #A32CC4;'>📈 Gráfica de recorridos por hora</h3>", unsafe_allow_html=True)
    st.pyplot(fig)
