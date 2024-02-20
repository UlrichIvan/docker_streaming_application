import streamlit as st
from PIL import Image


def app():
    image = Image.open("./public/business.png")

    st.image(image, width=250)

    st.title("Real-Time Financial Data Analysis")

    st.markdown(
        """
    ## Monitor the application for being informed about the new functionnalities that we provide to the application, in order to send us your feedback on them and improve you customer experience.
    """
    )
