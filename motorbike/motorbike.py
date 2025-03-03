import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos con caché para optimizar la aplicación
@st.cache_data
def cargar_datos(n_mb=39420):
    df = pd.read_csv("all_bike.csv", encoding="utf-8", nrows=n_mb)
    return df

# Cargar datos
motob_df = cargar_datos()

# Sidebar con información personal
sidebar = st.sidebar
sidebar.markdown("<h2 style='text-align: center; color: #FF4C4C;'>🌼Carlitarp🌼</h2>", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("<h4 style='text-align: center; color: #CCCCCC;'>🧡S20006731 ISW🧡</h4>", unsafe_allow_html=True)
sidebar.markdown("### 📩 Contacto")
sidebar.markdown("[✉️ zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
sidebar.markdown("______")
sidebar.header("🏍️ Opciones de Visualización")

# Búsqueda por modelo específico
modelo_busqueda = sidebar.text_input("🔎 Buscar por Modelo")

# Filtro por Marca
marca_seleccionada = sidebar.selectbox("🏷️ Selecciona una marca:", ['Todas'] + motob_df['Brand'].unique().tolist())
if marca_seleccionada != "Todas":
    df_filtrado = motob_df[motob_df["Brand"] == marca_seleccionada]
else:
    df_filtrado = motob_df

# Filtro por Año
anio_seleccionado = sidebar.slider("📅 Año", int(motob_df['Year'].min()), int(motob_df['Year'].max()), 
                                   (int(motob_df['Year'].min()), int(motob_df['Year'].max())))

# Filtro por Categoría
categoria_seleccionada = sidebar.multiselect("⚙️ Categoría", options=motob_df['Category'].unique())

# Filtro por Transmisión
transmision_seleccionada = sidebar.selectbox("⚡ Transmisión", options=['Todas'] + motob_df['Transmission type'].unique().tolist())

# Filtrado de datos
df_filtrado = motob_df.copy()
if modelo_busqueda:
    df_filtrado = df_filtrado[df_filtrado['Model'].str.contains(modelo_busqueda, case=False, na=False)]

if marca_seleccionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['Brand'] == marca_seleccionada]

if transmision_seleccionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['Transmission type'] == transmision_seleccionada]

df_filtrado = df_filtrado[(df_filtrado['Year'] >= anio_seleccionado[0]) & (df_filtrado['Year'] <= anio_seleccionado[1])]

if categoria_seleccionada:
    df_filtrado = df_filtrado[df_filtrado['Category'].isin(categoria_seleccionada)]

# 🔥 Título Principal con estilo deportivo
st.markdown("<h1 style='text-align: center; color: #FF4C4C;'>🔥 Catálogo de Motos 🔥</h1>", unsafe_allow_html=True)
st.subheader("🏁 **Velocidad, potencia y rendimiento en un solo lugar**")

# Total de registros
st.write(f"**📊 Total de registros filtrados: {len(df_filtrado)}**")
st.dataframe(df_filtrado)

# 🏆 Motor con Más Torque
if not df_filtrado.empty:
    motor_torque = df_filtrado.loc[df_filtrado['Torque (Nm)'].idxmax()]
    st.write(f"**💪 Motor con más torque:** {motor_torque['Model']} - {motor_torque['Torque (Nm)']} Nm")

# 📊 Histograma de Desplazamiento
st.markdown("___")
if not df_filtrado.empty:
    st.write("📊 **Distribución de cilindrada (ccm)**")
    st.write("Este gráfico muestra cuántas motos hay en cada rango de cilindrada, permitiendo identificar las más comunes.")
    fig_hist = px.histogram(df_filtrado, x='Displacement (ccm)', title="Distribución de Desplazamiento (ccm)",
                            nbins=30, color='Brand', opacity=0.7)
    st.plotly_chart(fig_hist)

# ⚡ Dispersión de Potencia vs. Desplazamiento
st.markdown("___")
if not df_filtrado.empty:
    st.write("⚡ **Potencia vs. Desplazamiento**")
    st.write("Compara la cilindrada con la potencia de las motos para analizar su relación.")
    fig_potencia = px.scatter(df_filtrado, x='Displacement (ccm)', y='Power (hp)', color='Brand',
                              title="Potencia vs. Desplazamiento",
                              hover_data=['Model'])
    st.plotly_chart(fig_potencia)

# 📈 Línea de Potencia Promedio por Año
st.markdown("___")
if not df_filtrado.empty:
    st.write("📈 **Evolución de la Potencia Promedio**")
    st.write("Observa cómo ha cambiado la potencia promedio de las motos a lo largo del tiempo.")
    potencia_anual = df_filtrado.groupby('Year')['Power (hp)'].mean().reset_index()
    fig_potencia_anual = px.line(potencia_anual, x='Year', y='Power (hp)', title="Evolución de la Potencia Promedio",
                                 markers=True)
    st.plotly_chart(fig_potencia_anual)

# 🏆 Top 5 Marcas con Mayor Potencia
top_5_marcas = motob_df.groupby("Brand")["Power (hp)"].mean().nlargest(5).reset_index()
st.markdown("## 🏁 Top 5 Marcas con Mayor Potencia")
fig_top5 = px.bar(top_5_marcas, x="Brand", y="Power (hp)", text="Power (hp)", color_discrete_sequence=['#00A8FF'])
st.plotly_chart(fig_top5)

# ⚖️ Dispersión de Peso vs. Capacidad de Combustible
st.markdown("___")
if not df_filtrado.empty:
    st.write("⚖️ **Peso vs. Capacidad de Combustible**")
    st.write("Analiza si las motos más pesadas tienen mayor capacidad de combustible.")
    fig_peso = px.scatter(df_filtrado, x='Dry weight (kg)', y='Fuel capacity (lts)', color='Brand',
                          title="Peso vs Capacidad de Combustible",
                          hover_data=['Model'])
    st.plotly_chart(fig_peso)

# 🌡️ Resumen de Refrigeración
st.sidebar.subheader("🌡️ Resumen de Refrigeración")
refrigeracion = df_filtrado['Cooling system'].value_counts()
st.sidebar.write(refrigeracion)
