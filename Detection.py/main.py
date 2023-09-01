import streamlit as st
import base64
# Custom CSS styling
st.markdown(
    """
    <style>
    .title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .container {
        width: 50%;
        margin: auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI layout
st.title("Welcome to Image Classification Site")
st.markdown('<p class="title">Classify Different Images</p>', unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.write(
    "Image classification is a fundamental task in computer vision. It involves categorizing images into predefined classes or categories. "
    "Here are some practical applications:"
)

st.markdown(
    """
    <ol>
        <li>Object Recognition: Recognizing and labeling objects in images.</li>
        <li>Medical Imaging: Diagnosing medical conditions from X-rays, MRIs, etc.</li>
        <li>Security and Surveillance: Identifying threats in security camera feeds.</li>
        <li>Automated Vehicles: Recognizing pedestrians, road signs, etc.</li>
        <li>Agriculture: Identifying crop diseases, pests, etc.</li>
        <li>E-commerce: Product categorization, recommendation systems.</li>
        <li>Social Media: Content moderation, image tagging.</li>
        <li>Natural Sciences: Classifying species, celestial objects.</li>
        <li>Quality Control: Inspecting products for consistency.</li>
        <li>Document Analysis: Reading handwriting, converting scans to text.</li>
    </ol>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


#FOR BACKGROUND IMAGE
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

st.markdown(f'<a href="https://storyset.com/business">Business illustrations by Storyset</a>', unsafe_allow_html=True)


