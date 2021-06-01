import streamlit as st
from datetime import date
import pandas as pd

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import plotly.graph_objects as goj

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction")

stocks = st.text_input('Ticker symbol', 'AAPL')

@st.cache(allow_output_mutation=True)
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace = True)
    return data

data_load_state = st.text("Load data...")
data = load_data(stocks)
data_load_state.text("Loading data... done!")
data['Date'] = pd.to_datetime(data['Date']).dt.date

st.subheader('Raw data')
st.write('*Data Available for the models*', data.shape[0] * data.shape[1])
st.write(data[::-1])

def plot_chart_raw_data():
    fig3 = go.Figure(data=[goj.Candlestick(x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'])])
    fig3.update_xaxes(type="category")
    fig3.update_layout(title_text="Candlestick Chart", height=600)
    st.plotly_chart(fig3, use_container_width=True)

plot_chart_raw_data()

# def plot_raw_data():
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
#     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
#     fig.layout.update(title_text="Chart", xaxis_rangeslider_visible=True)
#     st.plotly_chart(fig)

# plot_raw_data()

st.write('''
    <style>
        div.row-widget.stRadio > div{flex-direction:row;}
        .row-widget.stButton{text-align:center}
    </style>''', unsafe_allow_html=True)
n_years = st.radio('Years of predictions', (1, 2, 3, 4))
period = n_years * 365

if st.button(f"Predict the next {n_years} years"):
    #Forecasting
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={'Date': 'ds', 'Close': 'y'})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Forecast Data')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.subheader('Forecast Intervales')
    fig2 = m.plot_components(forecast)
    st.write(fig2)








