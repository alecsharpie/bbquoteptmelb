import streamlit as st

from bbquoteptmelb.lib import get_quote

st.header('Breaking Bad Quotes')

st.write(get_quote())
