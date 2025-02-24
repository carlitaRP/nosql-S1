import pandas as pd
import streamlit as st

sidebar = st.sidebar
sidebar.markdown("## 🌸 Carlitarp", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("### 💜 S20006731 ISW", unsafe_allow_html=True)
sidebar.markdown("[📧 zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
sidebar.markdown("---")

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title("Streamlit and pandas")
st.dataframe(names_data)