import streamlit as st
from PIL import Image

from utils.tools import PUBLIC_PATH


def app():
    image = Image.open(f"{PUBLIC_PATH}/business.png")

    st.image(image, width=250)

    st.title("Real-Time Financial Data Analysis")
    st.markdown(
        """
    This app retrieves stock --- from the **---**!

    """
    )

    st.markdown(
        """
    ## Welcome
    ### Let's analyze together!
    ### Let's go!
    """
    )
