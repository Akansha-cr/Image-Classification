import streamlit as st
import streamlit.components.v1 as html
from PIL import Image
import base64
header=st.container()
with header:
    st.write(f'<h1 style="color:white;font-size:25px;">{"About and Contact.."}</h1>', unsafe_allow_html=True)
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
#form
st.write(f'<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSe5cb9DhQxHWm5GwSYlHx1vVAcOkRbtEgCS-h20k9vG8Wefeg/viewform?embedded=true" width="640" height="948" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html= True)

