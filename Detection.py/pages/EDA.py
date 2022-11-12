import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as html
header=st.container()
with header:
    st.write(f'<h1 style="color:white;font-size:35px;">{"Analysis and preprocessing for detection of skin cancer. Coming Soon!"}</h1>', unsafe_allow_html=True)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('asset/—Pngtree—abstract background gaming futuristic banner_1235846.jpg')
st.container()
with st.container():
    st.image('asset/Growth analytics-amico.png')
