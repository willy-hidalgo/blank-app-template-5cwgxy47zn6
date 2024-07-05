import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write('Hello *world!*')

df = pd.read_csv('my_data.csv')
st.line_chart(df)
