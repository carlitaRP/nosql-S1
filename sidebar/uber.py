import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

sidebar = st.sidebar
sidebar.markdown("## 🌸 Carlitarp", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("### 💜 S20006731 ISW", unsafe_allow_html=True)
sidebar.markdown("[📧 zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
sidebar.markdown("---")

DATE_COLUMN = 'date/time'
DATA_URL = 'uber_dataset.csv'

@st.cache  
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(columns=lowercase, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
