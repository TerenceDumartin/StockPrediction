import app1
import prediction
import app3
import app4
import streamlit as st
PAGES = {
    "Homepage": app1,
    "Prediction": prediction,
    "Screener": app3,
    "Trackers": app4,
}

st.sidebar.title('DollyFlow')
st.sidebar.markdown('''

    ''')
st.sidebar.write('Everything you need to know to become **lethal** on stock market')
st.sidebar.markdown('''

    ''')

selection = st.sidebar.selectbox("Navigation", ('Homepage', 'Prediction', 'Screener', 'Trackers'))
page = PAGES[selection]
page.app()

if selection == 'Prediction':

    st.sidebar.markdown('''

        ''')
    stocks = st.sidebar.text_input('Ticker symbol', 'AAPL')

    st.sidebar.markdown('''

        ''')
    selection_pred = st.sidebar.radio("", ('Overview', 'Prediction', 'Twitter Tracker', 'News Trackers'))

