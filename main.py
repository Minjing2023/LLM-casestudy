import streamlit as st

from utils import generate_casestudy


st.header("Case Study AI generator ✏️")
st.markdown("This is a tool for generating case studies based on your name, major, and career objective.")
st.markdown("Chapter 1: Accrual Basis Accounting")
with st.sidebar:
    openai_api_key = st.text_input("Please input OpenAI API key：", type="password")
    st.markdown("[To get your OpenAI API key](https://platform.openai.com/account/api-keys)")

theme = st.text_input("Please input your name, major, and career objective.")
submit = st.button("Generate")

if submit and not openai_api_key:
    st.info("Please input OpenAI API key.")
    st.stop()
if submit and not theme:
    st.info("Please input your name, major, and career objective.")
    st.stop()
if submit:
    with st.spinner("AI is working hard on this, please wait..."):
        result = generate_casestudy(theme, openai_api_key)
    st.divider()

    st.markdown("Title:")
    st.write(result.titles[0])


    st.markdown("Case study:")
    st.write(result.content)
