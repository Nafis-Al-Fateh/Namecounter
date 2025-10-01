import streamlit as st

# Title
st.title("Character Counter App")

# Input from user
student = st.text_input("Please Input Your Name:")

if student:  # only run when input is given
    # Dictionary: each character and how many times it appears
    dictionary = {ch: student.count(ch)}

    # Show results
    st.write("### Your Name:")
    st.write(student)

    st.write("### Character Count Dictionary:")
    st.json(dictionary)  # pretty display
