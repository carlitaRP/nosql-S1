import pandas as pd
import streamlit as st
import datetime

titanic_link = 'titanic.csv'

titanic_data = pd.read_csv(titanic_link)

# Create the title for the web app
st.title("Titanic App")
sidebar = st.sidebar
sidebar.markdown("## 🌸 Carlitarp", unsafe_allow_html=True)
sidebar.image('carlita.jpg', width=160)
sidebar.markdown("### 💜 S20006731 ISW", unsafe_allow_html=True)
sidebar.markdown("[📧 zS20006731@estudiantes.uv.mx](mailto:zS20006731@estudiantes.uv.mx)")
sidebar.markdown("---")

# Give user the current date
today = datetime.date.today()
today_date = st.date_input('Current date', today)

st.success('Current date: `%s`' % (today_date))

# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.checkbox("show DataSet Overview ? ")
if agree: st.dataframe(titanic_data)

# Select the embark town of the passanger and then display the dataset with this selection
selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())

st.write("Selected Embark Town:", selected_town)

st.write(titanic_data.query(f"""embark_town==@selected_town"""))

st.markdown("___")

# Select a range of the fare and then display the dataset with this selection
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
(fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

# Display of the dataset
st.dataframe(subset_fare)