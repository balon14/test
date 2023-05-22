import io
import streamlit as st
from PIL import Image
from transformers import YolosFeatureExtractor, YolosForObjectDetection
import requests
import re


# Получение имени пользователя и вывод приветствия
name = st.text_input("Enter your name", "")
st.write(f"Hello, {name}!")


def load_image():
    """Создание формы для загрузки изображения"""
    # Форма для загрузки изображения средствами Streamlit
    uploaded_file = st.file_uploader(
        label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице средствами Streamlit
        st.image(image_data)
        # Возврат изображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None

# Выводим заголовок страницы средствами Streamlit     
st.title('Классификация изображений')
# Вызываем функцию создания формы загрузки изображения
img = load_image()


feature_extractor = YolosFeatureExtractor.from_pretrained('hustvl/yolos-tiny')
model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')


inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)


# model predicts bounding boxes and corresponding COCO classes
logits = outputs.logits
bboxes = outputs.pred_boxes
