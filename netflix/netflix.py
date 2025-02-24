import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos(n_filmes=1000):
    try:
        df = pd.read_csv("netflix/movies.csv", encoding="utf-8", nrows=n_filmes)
    except UnicodeDecodeError:
        df = pd.read_csv("netflix/movies.csv", encoding="latin1", nrows=n_filmes)  # Alternativa en caso de error
    return df

movies_df = cargar_datos()

st.markdown("<h1 style='text-align: center; color: #A32CC4;'>Netflix Recommender System 🍿💜</h1>", unsafe_allow_html=True)
st.write("🎬 **Encuentra y filtra tus películas favoritas de Netflix!**")

sidebar = st.sidebar
sidebar.markdown("<h2 style='text-align: center; color: #A32CC4;'>🌸 Carlitarp</h2>", unsafe_allow_html=True)
st.sidebar.image("https://raw.githubusercontent.com/carlitaRP/nosql-S1/master/netflix/carlita.jpg", width=160)
sidebar.markdown("<h4 style='text-align: center; color: #A32CC4;'>💜 S20006731 ISW</h4>", unsafe_allow_html=True)
st.sidebar.markdown("### 📩 Contacto")
st.sidebar.markdown("[✉️ zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")

st.sidebar.markdown("______")

st.sidebar.header("📽️ Opciones de Visualización")
mostrar_todos = st.sidebar.checkbox("🎬 Mostrar todas las peliculas")

if mostrar_todos:
    cantidad_total = len(movies_df)
    st.markdown(f"<h3 style='color: #A32CC4;'>Lista de películas - ({cantidad_total} registros):</h3>", unsafe_allow_html=True)
    st.dataframe(movies_df)
    st.markdown("______")

st.sidebar.header("🔎 Buscar Pelicula por Título")
titulo_busqueda = st.sidebar.text_input("📌 Ingrese el título")

if st.sidebar.button("🔍 Buscar"):
    resultado_busqueda = movies_df[movies_df["name"].str.contains(titulo_busqueda, case=False, na=False)]
    cantidad_busqueda = len(resultado_busqueda)
    st.markdown(f"<h4 style='color: #A32CC4;'>Se encontraron {cantidad_busqueda} coincidencias</h4>", unsafe_allow_html=True)
    st.dataframe(resultado_busqueda)

st.sidebar.header("🎬 Filtrar peliculas por Director")
director_seleccionado = st.sidebar.selectbox("🎥 Seleccione un director:", movies_df["director"].dropna().unique())

if st.sidebar.button("🎭 Filtrar por Director"):
    filmes_director = movies_df[movies_df["director"] == director_seleccionado]
    cantidad_director = len(filmes_director)
    st.markdown(f"<h4 style='color: #A32CC4;'>Películas dirigidas por {director_seleccionado} ({cantidad_director} registros):</h4>", unsafe_allow_html=True)
    st.dataframe(filmes_director)
