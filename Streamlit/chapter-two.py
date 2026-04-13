import streamlit as st

st.title("chai Maler app")


add_masala = st.checkbox("Masala chai")

if add_masala:
    st.write("Masala added to your chai")


tea_type = st.radio("Pick your chai base: ",["Milk","water","almond milk","honey"])

st.write(f"Selcted base is:{tea_type}")

flavour = st.selectbox("Pick the flavour" , [" Adrak " , " Kesar " , " Elaichi " ," Cinnamon "])

sugar = st.slider("Sugar level:" , 0 , 10 ,2)


cups = st.number_input("How many cups?", min_value = 1 , max_value = 10 , step = 1 ) 

name = st.text_input("Write your name ")

if name:
    st.write(f"Welcome {name} , your chai is on the way ")


dob = st.date_input("Select your DOB")

if st.button("make chai"):
    st.success("Your chai is being brewed")