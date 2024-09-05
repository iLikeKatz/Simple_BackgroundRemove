from rembg import remove
from PIL import Image
import streamlit as st

def RemoveBackground(input_image):
    output_image = remove(input_image)
    return output_image

input = st.file_uploader("Upload your Image")
if input:
    image = Image.open(input)
    st.image(image, caption="Uploaded Image")

    if st.button("Remove Background"):
        removed_image = RemoveBackground(image)
        st.image(removed_image, caption="Background Removed")
