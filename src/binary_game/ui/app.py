import streamlit as st

from binary_game.core.engine import BinaryGameEngine
from binary_game.core.converter import BinaryGameConverter
from binary_game.core.presenter import BinaryPresenter


st.set_page_config(layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        font-size: 20px;
    }

    .stMarkdown, .stText, .stButton, .stSuccess {
        font-size: 20px !important;
    }

    code {
        font-size: 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

engine = BinaryGameEngine()
converter = BinaryGameConverter(bits=8)
presenter = BinaryPresenter()

if "task" not in st.session_state:
    value, system = engine.next()
    st.session_state.task = (value, system)
    st.session_state.show = False


value, system = st.session_state.task
binary = converter.encode(value, system)


st.title("Binary Bingo")

st.code(system)
st.code(binary)

if st.session_state.show:
    st.success(f"DEC: {value}")


col1, col2 = st.columns(2)

with col1:
    if st.button("Show Answer"):
        st.session_state.show = True

with col2:
    if st.button("Next"):
        st.session_state.task = engine.next()
        st.session_state.show = False
        st.rerun()