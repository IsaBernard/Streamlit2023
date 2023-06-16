import streamlit as st
import yfinance as yf
import pandas as pd



st.write("""
## Stock Price and volume since Jan 2010
Stock **closing price** and **volume** of Amazon (AMZN) 
""")

# define the ticker symbol
tickerSymbol = 'AMZN'
# get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='Id', start='2010-01-01', end='2023-06-15')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

