import streamlit as st
st.title("Diwakar New Test")

name = st.text_input("Enter Name:- ")
mobile = st.number_input("Enter Mobile no.:- ")
add = st.text_area("Enter your Address:- ")
age = st.slider("Enter your age:- ",0, 100)
Child = st.selectbox("Enter Total Child:-" ,(1,2,3,4))

button = st.button("Done")
if button:
    st.markdown(f"""
    name: {name}
    mobile: {mobile}
    address: {add}
    age: {age}
    Child: {Child}""")