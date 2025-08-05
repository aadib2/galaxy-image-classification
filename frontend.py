#import necessary libraries
import streamlit as st
from PIL import Image

import torch
import torch.nn as nn
import torchvision.transforms as transforms

import pandas as pd

# import necessary methods
from utils import preprocess_image_st, predict, visualize_predictions_st


# Header stuff and basic info
st.title("Galaxy Classification Frontend")
st.write("Purpose of this website is to classify images of galaxies based on their morphological characteristics")
st.write("Currently we can classify images of size 227x227 into 3 types: Spiral (S), Elliptical (E) and Spiral Barred (SB)")
st.markdown("Our model's accuracy is **86.59%**")

st.markdown('*Note: Until an image is uploaded, you will see an error message regarding a null image_tensor. Ignore this message.*')

# prompt user to enter an image
uploaded_file = st.file_uploader("⋆⭒˚.⋆🔭 Upload a galaxy image...", type = ["jpg", "jpeg", "png"])

# if image was uploaded
if uploaded_file is not None:
    # Open the image using PIL library
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.success("Image uploaded successfully!")
else:
    st.error("Image not uploaded")


# resize the image and apply appropriate transformations
transform = transforms.Compose({
    transforms.Resize((227,277)),
    transforms.ToTensor(),
})

# Apply preprocessing and display the transformed image
if uploaded_file is not None:
    image_tensor = preprocess_image_st(image, transform)

    # Display the transformed image
    st.image(image_tensor.squeeze(0).permute(1, 2, 0).numpy(), caption="Transformed Image", use_container_width=True)


# Define model
from GalaxyImageClassifierModel import GalaxyImageClassifier

# Load the trained model
model = GalaxyImageClassifier(num_classes=3)
model.load_state_dict(torch.load('./galaxy_classifier.pth', map_location=torch.device('cpu')))

# set up device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Predict using the model
predicted_class = predict(model, image_tensor, device)

#print(f'Predicted Class: {predicted_class}')

# display predictions and final result
class_names = {0: 'E', 1: 'S', 2: 'SB'}

visualize_predictions_st(predicted_class, class_names)


