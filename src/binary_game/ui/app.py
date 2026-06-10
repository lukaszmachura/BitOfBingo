import streamlit as st

from binary_game.core.engine import BinaryGameEngine
from binary_game.core.converter import BinaryGameConverter
from binary_game.core.presenter import BinaryPresenter
from binary_game.translations import TRANSLATIONS


def parse_system(system, lang="pl"):
    SYSTEMS_EN = {
        "U1": "U1",
        "U2": "U2",
        "NKB": "Natural Binary Code",
        "ZM": "Signed Magnitude",
        "STD BIAS": "Standard Bias",
        "8421": "8421",
        "NUDING": "Nuding",
        "STIBITZ": "Stibitz",
        "DIAMOND": "Diamond",
    }
    SYSTEMS_PL = {
        "U1": "U1",
        "U2": "U2",
        "NKB": "Naturalny Kod Binarny",
        "ZM": "Znak-Moduł",  
        "STD BIAS": "Standardowe przesunięcie (bias)",
        "8421": "8421",
        "NUDING": "Nuding",
        "STIBITZ": "Stibitz",
        "DIAMOND": "Diamond",
    }
    SYSTEMS = {
        "en": SYSTEMS_EN,
        "pl": SYSTEMS_PL,
    }
    return SYSTEMS.get(lang, SYSTEMS_EN).get(system, system)


if "lang" not in st.session_state:
    st.session_state.lang = "en"
language = st.session_state.lang

col1, col2, col3 = st.columns([6, 1, 1])
with col2:
    if st.button("🇬🇧"):
        language = "en"

with col3:
    if st.button("🇵🇱"):
        language = "pl"

st.session_state.lang = language
t = TRANSLATIONS[language]

with col1:
    st.title(t["title"])

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

if "engine" not in st.session_state:
    engine = BinaryGameEngine()
    st.session_state.engine = engine

if "converter" not in st.session_state:
    converter = BinaryGameConverter(bits=8)
    st.session_state.converter = converter

if "presenter" not in st.session_state:
    presenter = BinaryPresenter()
    st.session_state.presenter = presenter

engine = st.session_state.engine
converter = st.session_state.converter
presenter = st.session_state.presenter

if "task" not in st.session_state:
    value, system = engine.next()
    st.session_state.task = (value, system)
    st.session_state.show = False


value, system = st.session_state.task
binary = converter.encode(value, system)


st.code(parse_system(system, lang=language))
st.code(binary)

if st.session_state.show:
    st.success(f"DEC: {value}")


col1, col2, col3 = st.columns(3)

with col1:
    if st.button(t["show_dec"]):
        st.session_state.show = True

with col2:
    if st.button(t["next"]):
        st.session_state.task = engine.next()
        st.session_state.show = False
        st.rerun()

with col3:
    if st.button(t["new_game"]):
        engine.reset()
        st.session_state.task = engine.next()
        st.session_state.show = False
        st.rerun()