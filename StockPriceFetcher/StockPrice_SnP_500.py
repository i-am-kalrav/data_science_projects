import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date as dt

tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]['Symbol'].tolist()
#print(tickers)

st.write("""
# Stock Price App
""")

selected_stock = st.selectbox("Select a Stock (ticker) from the S & P 500", tickers)
st.write(f"You selected: {selected_stock}")

msg = "Below are the stock closing price and volume of " + str(selected_stock) + " since it became public:"
st.write(msg)

tSymbol = str(selected_stock)
tickerData = yf.Ticker(tSymbol)
tickerDf = tickerData.history(period='1d', start='1602-01-01', end=str(dt.today()))

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)
