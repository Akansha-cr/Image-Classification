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

#model
csv_path = "HAM10000_metadata.csv"
skin_df = pd.read_csv(csv_path)

path = Path('HAM10000_metadata.csv')
Path.BASE_PATH = path
path.ls()

short_to_full_name_dict = {
    "akiec" : "Bowen's disease", # very early form of skin cancer 
    "bcc" : "basal cell carcinoma" , # basal-cell cancer or white skin cancer
    "bkl" : "benign keratosis-like lesions", # non-cancerous skin tumour
    "df" : "dermatofibroma", # non-cancerous rounded bumps 
    "mel" : "melanoma", # black skin cancer
    "nv" : "melanocytic nevi", # mole non-cancerous
    "vasc" : "vascular lesions", # skin condition
}

# returns only dx and image id column
img_to_class_dict = skin_df.loc[:, ["image_id", "dx"]] 
# returns columns as lists in a dict
img_to_class_dict = img_to_class_dict.to_dict('list')  
# returns a dict mapping image id to disease name
img_to_class_dict = {img_id : short_to_full_name_dict[disease] for img_id,disease in zip(img_to_class_dict['image_id'], img_to_class_dict['dx']) } 

# path.stem returns the filename without suffix
def get_label_from_dict(path):
    return img_to_class_dict[path.stem] 

from fastai.vision.data import *
dblock = DataBlock(
    # Designation the independent and dependent variables
    blocks = (ImageBlock, CategoryBlock), 
    # To get a list of those files,and returns a list of all of the images in that path
    get_items = get_image_files, 
    # Split our training and validation sets randomly
    splitter = RandomSplitter(valid_pct=0.2, seed=42),
    # We are telling fastai what function to call to create the labels in our dataset, in our case is independet variable
    get_y = get_label_from_dict,
    # DihedralItem all 4 90 deg roatations and for each: 
    #2 horizonntal flips -> 8 orientations
    item_tfms=[Resize(448), DihedralItem()],
    # Picks a random scaled crop of an image and resize it to size
    batch_tfms=RandomResizedCrop(size=224, min_scale=0.75, max_scale=1.0))

img_path = 'Data/samples/'
# create dataloader using img_path   
dls = dblock.dataloaders(img_path, bs=64) # bs = batch size
sample = dls.show_batch(max_n=15)
st.markdown(sample)
#resnet = vision_learner(dls,
  #                  resnet18,
 #                   metrics=accuracy)
#resnet.fine_tune(1)
#resnet.eval()

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
	resnet = models.resnet34(dls, pretrained=False)
	resnet.eval()
	out = resnet(batch_img_tensor)
	with open('HAM10000_metadata.csv') as f:
		labels = [line.strip() for line in f.readlines()]
	_, index = torch.max(out, 1)
	percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
	print(labels[index[0]], percentage[index[0]].item())
	_, indices = torch.sort(out, descending=True)
	[(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]


	
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
