import email
import streamlit as st


def signup_function():
    print("running")
    st.write("Sign up here")
    with st.form("Signup_form"):
        st.write("Singup Here")
        email = st.text_area('Email ID')
        # Every form must have a submit button.
        submit_button = st.form_submit_button(label="✨ Get me the data!")
        if not submit_button:
            st.stop()
        st.write("slider",)
    print(email)    

if __name__ == '__main__':
    signup_function()
