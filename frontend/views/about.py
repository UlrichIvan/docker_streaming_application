import streamlit as st
from PIL import Image


def app():
    expander_bar = st.expander("About")
    expander_bar.markdown(
        """
    * **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
    * **Data source:** ---.
    * **Credit:** ---.
    """
    )

    st.markdown(
        """
    ## M&M Dashboard For Traders is a web application designed for empowering your trading game by leveraging data visualization, fundamental and technical analysis but also discover the real time insights behind your data.
    """
    )
