import streamlit as st
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("Receipt OCR")
st.write("Upload a receipt image to extract text.")

uploaded_file = st.file_uploader(
    "Choose a receipt image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    file_bytes = uploaded_file.read()

    with open("temp.jpg", "wb") as f:
        f.write(file_bytes)

    img = cv2.imread("temp.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    st.image(img, caption="Uploaded Receipt")

    st.subheader("Extracted Text")

    st.text(text)