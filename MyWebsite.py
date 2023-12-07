from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

img_ha_Spinda= Image.open("Thumbnail HA Spinda.png")
img_louie_larong= Image.open("Profile_picture.png")

with st.container():
    st.subheader("Hi!, I am Louie Larong :wave:")
    st.title("A BSCpE - 1A Student from SNSU")
    st.write("I created this website to share my content about a game called PokeMMO.")
    st.write("[Learn More >](https://www.youtube.com/@akiraarkangel7286)")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_louie_larong)   
    with text_column:
        st.title("My Profile")
        st.write("""
        Name: Louie Jay H. Larong
        Course: BS Computer Engineering
        Section: 1A
        """)
        

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("In Game Statistics:")
        st.write("##")
        st.write("In Game Name(IGN): AkiraArkangel")
        st.write(
            """
            - In Game Hours Played🕑: 400+ Hours
            - Shiny Count🌟: N/A
            - Net worth💵: 30+ Million Pokeyen
            """)
        st.write("I started playing PokeMMO back in early 2022 when my friend recommended it to me. I've been inactive here an there as I am a still a student and now" 
                 "starting to go into a university. I'm looking forward to make more progress towards the betterment of me as a content creators, a student, and a PokeMMO player.")
    with right_column:
        st.empty()

with st.container():
    st.write("---")
    st.header("My Content")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ha_Spinda)
        with text_column:
            st.subheader("Catching Alpha Pokemons without HA Spinda")
            st.write(
                 """
                Easily catch Alpha pokemons without HA Spinda. In this video I'll be showing you an easy alternative in catching Alpha pokemons.
                This is not a hundred percent catch rate but this tutorial works almost all the time.
                 """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=IyfuE4HWdt0)")

with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/jaymarcortez.141997@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your Name" required>
        <input type="email" name="email" placeholder= "Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column= st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
