import streamlit as st

from llm.dumbest_llm import DumbestLLM

st.set_page_config(page_title='Dumb Chat', layout='wide')

if 'input' not in st.session_state:
    st.session_state.input = ''

if 'output' not in st.session_state:
    st.session_state.output = ''


@st.cache_resource
def get_llm():
    return DumbestLLM()


llm = get_llm()


def update_chat():
    st.session_state.output = llm.chat(st.session_state.input)


st.title("Let's Chat")


st.session_state.input = st.text_area('User', '')

st.button("Get Chat", on_click=update_chat)

st.markdown(st.session_state.output)
