import streamlit as st

from src.server.config import DESCRIPTION

st.title('Главная страница')

st.markdown(DESCRIPTION)
