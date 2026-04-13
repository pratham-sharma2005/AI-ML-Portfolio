import streamlit as st

st.title("Chai Taste Poll")

col1 , col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://i.ytimg.com/vi/TMLSaMOQsVk/maxresdefault.jpg", width= 1000)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://moonrice.net/wp-content/uploads/2023/08/Chai-05.jpg", width= 500 )
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2:
    st.success("Thanks for voting for Adrak Chai")