import streamlit as st

st.title("Hello Chai APP")

st.subheader("Brewed with Streamlit")
st.text("Welcome to your first interactive app")

st.write("Choose your favourite type of Chai")

chai = st.selectbox("Your favouriet Chai",["lemon Chai","masala chai","normal chai","adrak chai"])

st.write(f"Your choice {chai}. Excellent Choice ")

st.success("Your chai has been brewed")