import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos con cache
@st.cache_data
def cargar_datos(n_registros=500):
    df = pd.read_csv("Employees.csv", nrows=n_registros)
    return df

employees = cargar_datos()

st.markdown("<h1 style='text-align: center; color: #A32CC4;'>🏢 Análisis de Empleados</h1>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align: center; font-size:18px; color:#A32CC4;">
Esta aplicación permite analizar datos de empleados mediante filtros, gráficos y estadísticas.
</p>
""", unsafe_allow_html=True)

sidebar = st.sidebar
sidebar.markdown("<h2 style='text-align: center; color: #A32CC4;'>🌸 Carlitarp</h2>", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("<h4 style='text-align: center; color: #A32CC4;'>💜 S20006731 ISW</h4>", unsafe_allow_html=True)
st.sidebar.markdown("### 📩 Contacto")
st.sidebar.markdown("[✉️ zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")

st.sidebar.markdown("______")
st.sidebar.header("🔍 Opciones de Visualización")

mostrar_todos = st.sidebar.checkbox("📋 Mostrar todos los empleados")
if mostrar_todos:
    st.markdown(f"<h3 style='color: #A32CC4;'>📊 Total de registros: {len(employees)}</h3>", unsafe_allow_html=True)
    st.dataframe(employees)
    st.markdown("____")
st.sidebar.markdown("____")

@st.cache_data
def buscar_empleados(df, emp_id=None, hometown=None, unit=None):
    if emp_id:
        df = df[df["Employee_ID"].astype(str) == str(emp_id)]
    if hometown:
        df = df[df["Hometown"].str.contains(hometown, case=False, na=False)]
    if unit:
        df = df[df["Unit"].str.contains(unit, case=False, na=False)]
    return df

st.sidebar.header("🔎 Búsqueda de Empleados")
emp_id = st.sidebar.text_input("🆔 Buscar por ID de Empleado")
hometown = st.sidebar.text_input("🏡 Buscar por Ciudad de Origen")
unit = st.sidebar.text_input("🏢 Buscar por Unidad Funcional")
if st.sidebar.button("🔍 Buscar"):
    resultados = buscar_empleados(employees, emp_id, hometown, unit)
    st.markdown(f"<h3 style='color: #A32CC4;'>📌 Total encontrados: {len(resultados)}</h3>", unsafe_allow_html=True)
    st.dataframe(resultados)
    st.markdown("____")
st.sidebar.markdown("____")

st.sidebar.header("🎓 Filtrar por Nivel Educativo")
nivel_educativo = st.sidebar.selectbox("📚 Selecciona un nivel", employees["Education_Level"].unique())
if nivel_educativo:
    filtrados = employees[employees["Education_Level"] == nivel_educativo]
    st.markdown(f"<h3 style='color: #A32CC4;'>🎓 Total empleados con nivel {nivel_educativo}: {len(filtrados)}</h3>", unsafe_allow_html=True)
    st.dataframe(filtrados)
    st.markdown("____")

st.sidebar.header("🏙️ Filtrar por Ciudad")
ciudad = st.sidebar.selectbox("🌆 Selecciona una ciudad", employees["Hometown"].unique())
if ciudad:
    empleados_ciudad = employees[employees["Hometown"] == ciudad]
    st.markdown(f"<h3 style='color: #A32CC4;'>🏙️ Total empleados en {ciudad}: {len(empleados_ciudad)}</h3>", unsafe_allow_html=True)
    st.dataframe(empleados_ciudad)
    st.markdown("____")

st.sidebar.header("🏢 Filtrar por Unidad Funcional")
unidad = st.sidebar.selectbox("💼 Selecciona una unidad", employees["Unit"].unique())
if unidad:
    empleados_unidad = employees[employees["Unit"] == unidad]
    st.markdown(f"<h3 style='color: #A32CC4;'>🏢 Total empleados en la unidad {unidad}: {len(empleados_unidad)}</h3>", unsafe_allow_html=True)
    st.dataframe(empleados_unidad)
    st.markdown("____")

# Gráficos con emojis 📊
st.markdown("<h2 style='color: #A32CC4;'>📊 Distribución de Edad de los Empleados</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
ax.hist(employees["Age"], bins=20, color="#A32CC4", edgecolor="black")
ax.set_xlabel("Edad")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
st.markdown("____")

st.markdown("<h2 style='color: #A32CC4;'>🏢 Cantidad de Empleados por Unidad Funcional</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
employees["Unit"].value_counts().plot(kind="bar", color="#A32CC4", ax=ax)
ax.set_xlabel("Unidad Funcional")
ax.set_ylabel("Número de Empleados")
st.pyplot(fig)
st.markdown("____")

st.markdown("<h2 style='color: #A32CC4;'>🌆 Ciudades con Mayor Índice de Deserción</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
city_turnover = employees.groupby("Hometown")["Attrition_rate"].mean().sort_values(ascending=False)
city_turnover.plot(kind="bar", color="#A32CC4", ax=ax)
ax.set_xlabel("Ciudad")
ax.set_ylabel("Índice de Deserción")
st.pyplot(fig)
st.markdown("____")

st.markdown("<h2 style='color: #A32CC4;'>📉 Relación entre Edad y Tasa de Deserción</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(data=employees, x="Age", y="Attrition_rate", color="#A32CC4", ax=ax)
ax.set_xlabel("Edad")
ax.set_ylabel("Índice de Deserción")
st.pyplot(fig)
st.markdown("____")

st.markdown("<h2 style='color: #A32CC4;'>📈 Relación entre Tiempo de Servicio y Tasa de Deserción</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(data=employees, x="Time_of_service", y="Attrition_rate", color="#A32CC4", ax=ax)
ax.set_xlabel("Tiempo de Servicio (años)")
ax.set_ylabel("Índice de Deserción")
st.pyplot(fig)
