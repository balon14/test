import streamlit as st
from sbert_punc_case_ru import SbertPuncCase
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import string



def lang_detection(input_text):
    try:
        detected_text = detect(input_text)
        if detected_text != 'ru':
            st.error("Язык введенного текста не русский! Попробуйте ввести \
                текст еще раз.")
            return "Язык введенного текста не русский! " + \
                "Попробуйте ввести текст еще раз."
        else:
            lowercase_text = input_text.lower()
            text_to_punctuate = lowercase_text.translate(str.maketrans('', '',
                                                         string.punctuation))
