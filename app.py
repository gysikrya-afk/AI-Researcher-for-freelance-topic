import streamlit as st

pages = {
    'Главная':[
        st.Page('./src/client/pages/main_page.py',title='Главная страница',icon='👋')
    ],
    'Агент':[
        st.Page('./src/client/pages/agent_page.py',title='ИИ-Агент',icon='🤖')
    ]
}

pg = st.navigation(pages=pages,position='top')
pg.run()
