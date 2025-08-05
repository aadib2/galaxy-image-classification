# 🌌 Galaxy-Image-Classifier

A deep learning web app for classifying galaxy morphologies using a convolutional neural network (CNN). Built with **PyTorch**, **scikit-learn**, and **Streamlit**, this project was trained on the Galaxy Zoo-2 dataset and deployed as an interactive image classifier for Elliptical, Spherical, and Barred Spiral galaxies. 

This project was a part of the Fall 2024 SDSU AI Club Semesterly Projects and completed by Aadi Bery, Manav Mittal, and Adam MacFarlane.

---

## 🚀 Live Demo Site

👉 [Live App on Streamlit](https://galaxy-image-classification.streamlit.app/)

🧠 Sample model accuracy: **86%** on validation data set  
📁 Dataset: [Kaggle](https://www.kaggle.com/datasets/robertmifsud/resized-reduced-gz2-images/data), [Google Drive link](https://drive.google.com/file/d/1WxgtI3oDXed2ATKneyxCWz7C-uOAsV6R/view)

> A note about the dataset available via Kaggle: For the sake of the project and computational resources, we only used the images in the 'images_E_S_SB_227x227_a_03' folder (the 227x227 pixel images). The google drive link goes to a zip file with that data.
---

## 🧠 Project Overview

- **Goal**: Classify galaxy images into one of three morphological types:
  - **Elliptical**
  - **Spherical**
  - **Barred Spiral**

- **Model**: CNN trained with PyTorch (used pre-trained 'efficientnet_b0' model via timm library)
- **Training Details**:
  - Optimizer: Adam
  - Loss: CrossEntropy
  - Data split: Train / Validation / Test
- **Web App**: Users can upload images and receive real-time predictions with visual feedback of model's probability predictions.

---

## 🛠️ Tech Stack

| Tool                            | Purpose                          |
|---------------------------------|----------------------------------|
| Python                          | Core programming language        
| PyTorch                         | Model building and training      
| scikit-learn                    | Evaluation metrics and train test split 
| Streamlit                       | Web application interface
| matplotlib / pandas             | Displaying visualizations / performance
| PIL / torchvision.transforms    | Image preprocessing 

---

## 📍 To run Streamlit site locally:
  - Clone git repository
  - Open folder in code editor (e.g. VS Code)
  - Ensure streamlit and other dependencies used are installed (streamlit, torch, etc...) -> pip install -r requirements.txt
  - Run command: "streamlit run frontend.py"
  - Upload or drag in a galaxy image and see what the model predicts! (there is a test image called "galaxy.jpg" in files you can try)

## 🔍 Acknowledgements:
- Authors / Creators of [Galaxy Zoo-2 Image Dataset](https://www.kaggle.com/datasets/robertmifsud/resized-reduced-gz2-images/data?select=images_E_S_SB_227x227_a_03) available via Kaggle
- Streamlit community for tutorials
- [SDSU AI Club](https://aiclub.sdsu.edu/) for organizing this project!

