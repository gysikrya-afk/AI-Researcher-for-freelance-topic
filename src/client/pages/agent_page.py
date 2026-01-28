import streamlit as st

from src.server.agent import create_agent
from src.server.config import SYSTEM_PROMPT

st.title('ИИ-Агент')

with st.sidebar:
    api_key = st.text_input('Gemini Key',type='password')
    topic = st.text_input('Введите тему для поиска на фрилансе')

if st.button('Начать поиск'):
    if not api_key:
        st.warning('Введите Gemini Key')
    elif not topic:
        st.warning('Введите тему')
    else:
        try:
            with st.spinner('Подготовка агента...'):
                agent = create_agent(model='gemini-2.5-flash-lite',api_key=api_key)
            with st.spinner('Подготовка ответа...'):
                responce = agent.invoke(f'{SYSTEM_PROMPT}.Тема:{topic}')
            
            st.markdown('### Готово!')
            st.write(responce)
        except Exception as e:
            st.error(f'Ошибка :{e}!')
