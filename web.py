from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

### The code given in comment is to apply animation and images but not able to do so,ignore it.

# Find more emojis here:http://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

#----LOAD ASSETS

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        
local_css("style/style.css")        
    
lottie_coding=load_lottieurl("https://lottie.host/54d652b4-dd3e-484e-879e-d5e9d807de18/CI7aZiQ82W.json")
img_lottie_animation=Image.open("images/abc.png")
# img_contact_form=Image.open("images/abc.jpg")
#-----Header----#
st.subheader("Hi,I am Banta singh :wave:")
st.title("A Python Programmer from  India")
st.write("I am passionate about Python and Cricket")
st.write("[About Cricket >](https://fateh-cricket-academy-ground.business.site/)")


#----What I Do-----#
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Skills")
        st.write("##")
        st.write(
            """
            I am in college and pursuing B.Tech CSE:
            - Python Programming.
            - Web development in Python.
            - Django/Flask Developer.
            - Mongodb(Database).
            - Put content on YouTube for entertainment
            """
            )  
        st.write("[YouTube Channel >](https://youtube.com/@bantasingh9617?si=bOiN8mzVmtinNeGF)")
with right_column:
    st_lottie(lottie_coding,height=300,key="coding")

#---My projects---#
with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column,text_column =st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
        with text_column:
          st.subheader("Streamline#")
          st.write(
            """
            Learn how to use steamline in web designing#.
            """
        )
          st.markdown("[Watch Video...](https://youtu.be/VqgUkExPvLY?si=1QU_Pfd_3AFU3ivK)")
          
#contact form    
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")   
    st.write("##")  
    contact_form="""
    <form action="https://formsubmit.co/singhbanta84@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea> 
     <button type="submit">Send</button>
</form>
"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()


