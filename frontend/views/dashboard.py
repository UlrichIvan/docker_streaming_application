import streamlit as st
from utils.helpers import (
    get_figure,
    get_static_data_from_symbol,
)
from utils.tools import SYMBOLS


def app():

    st.title("Candlestick chart for tickers in tab section below")

    st.text("This dashboard allow user to show chart associate to specific ticker.")

    st.subheader("Click on ticker tab below that you want to show the chart")

    tabs = st.tabs(tabs=SYMBOLS)

    for i, tab in enumerate(tabs):

        with tab:
            data_ticker = get_static_data_from_symbol(symbol=SYMBOLS[i])
            if len(data_ticker) > 0:
                st.subheader(f"Candlestick Chart for {SYMBOLS[i]} ticker ")
                fig = get_figure(data_ticker=data_ticker, symbol=SYMBOLS[i])
                st.plotly_chart(fig)
            else:
                st.write(f"Candlestick Chart for {SYMBOLS[i]} not available ")
