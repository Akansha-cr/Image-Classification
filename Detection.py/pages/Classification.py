import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as html
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

#file uploader
st.markdown(f'<h1 style="color:white;font-size:20px;">{"Please upload a file"}</h1>',  unsafe_allow_html=True)
image_file = st.file_uploader("Classify images by uploading them here")

#prediction
if image_file is not None:
	file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
	st.write(file_details)
	st.image(image_file)
    
prediction = st.button("SUBMIT")
if prediction:
	model = ResNet50(weights='imagenet')
	Image.open(image_file).convert('RGB')
	img = image.load_img(image_file, target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	preds = model.predict(x)
	pred1= (decode_predictions(preds, top=3)[0])
	st.markdown(pred1)
    
   
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
