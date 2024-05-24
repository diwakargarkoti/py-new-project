import streamlit as st
st.title("Diwakar New Test")

name = st.text_input("Enter Name:- ")
mobile = st.number_input("Enter Mobile no.:- ")
add = st.text_area("Enter your Address:- ")
age = st.number_input("Enter your age:- ")
Child = st.selectbox("Enter Total Child:-" ,(1,2,3,4))

button = st.button("Done")
