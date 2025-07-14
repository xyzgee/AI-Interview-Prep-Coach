import streamlit as st
from chatbot import generate_answer

st.set_page_config(page_title="Zephyr", page_icon="🤖")
st.title("Zephyr - AI Interview Prep Coach")

question = st.selectbox("Pick a sample interview question:", [
    "Tell me about yourself",
    "Why should we hire you?",
    "What are your strengths and weaknesses?",
    "Explain OOPs in Java",
    "Describe a recent project you worked on"
])

user_input = st.text_area("Your Answer:")

if st.button("Submit for Feedback"):
    if user_input.strip() == "":
        st.warning("Please write an answer before submitting.")
    else:
        with st.spinner("Analyzing..."):
            feedback = generate_answer(user_input)
            st.markdown(f"### 🧠 AI Coach's Feedback:\n{feedback}")
