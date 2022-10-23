from faulthandler import disable
import streamlit as st
st.set_page_config(page_title="Cool Website",layout="wide",page_icon=":tada:")
st.markdown("---")
st.header("Welcome to My Website :smile:")
st.markdown("---")
st.title("My Social Media Link")
if st.button("Facebook"):
    st.info("@SomeonesFB")
if st.button('Instagram'):
    st.error("@SomeonesInsta")
if st.button('Whatsapp'):
    st.success("+91 3445468243")
if st.button('Mail',key="a"):
    st.warning("someone@example.com")
st.markdown("---")
st.caption("Join Team")
name = st.text_input("Name")
if st.button("Join Team."):
    st.info(f"Welcome to the team, {name}.")
st.markdown("---")
st.title("Admin Login")
username = st.text_input("Username")
password = st.text_input("Password",type="password")
if st.button("Log. in"):
    if username == "Swastik" and password == "2009":
        st.success("Loged In, Successfly.")
        st.code("Here you can write something that only admins can view")
    else:
        st.error("Login, Failed")
st.markdown("---")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1rs6os {visibility: hidden;}
            .css-17ziqus {visibility: hidden;}
            """
st.markdown(hide_st_style,unsafe_allow_html=True)
