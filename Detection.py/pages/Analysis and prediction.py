#libraries
import streamlit as st
from PIL import Image
import base64
import os
import tensorflow as tf
from tensorflow import keras
import pickle
import fastai
from fastai.vision.all import *
from fastai.metrics import *
import pandas as pd
from pathlib import Path
from fastai.callback.all import *
from fastai.vision.data import *
import torch
from torchvision import models
from torchvision import transforms

device = torch.device("cuda")

#div
title_temp ="""
	<div style="background-color:#4C00A0;padding:9px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">PREDICTION</h1>
	</div>
	"""
st.markdown(title_temp, unsafe_allow_html= True)
st.markdown("______________________________________________________________________________________________________________")
st.image('asset/image1.png')


#file uploader
st.markdown(f'<h1 style="color:white;font-size:20px;">{"Please upload a file"}</h1>',  unsafe_allow_html=True)
image_file = st.file_uploader("Analysis and Prediction")

#prediction
if image_file is not None:
	file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
	st.write(file_details)
	st.image(image_file)
	

submit = st.button("PREDICT")
if submit:
	st.write("Processing...")
	#loading the img from user
	img = Image.open(image_file).convert('RGB')
	preprocess = transforms.Compose([
		transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
			mean=[0.485, 0.456, 0.406],
			std=[0.229, 0.224, 0.225]
		)])
	img_preprocessed = preprocess(img)
	batch_img_tensor = torch.unsqueeze(img_preprocessed, 0)
	resnet = models.resnet34(pretrained=True)
	resnet.eval()
	out = resnet(batch_img_tensor)
	with open('HAM10000_metadata.csv') as f:
		labels = [line.strip() for line in f.readlines()]
	_, index = torch.max(out, 1)
	percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
	print(labels[index[0]], percentage[index[0]].item())
	_, indices = torch.sort(out, descending=True)
	[(labels[idx], percentage[idx].item()) for idx in indices[0][:4]]
	
	
#Background image
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
