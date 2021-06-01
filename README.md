Link -> [Stock Prediction](http://tradingprediction.herokuapp.com/)

# V0 - Stock Prediction

[Stock Prediction](http://tradingprediction.herokuapp.com/) allow you to make prediction based on whatever stockmarket you want.<br/>
This version is made using:
- Yahoo Finance API
- Facebook Prophet
- Streamlit


# V(n+) - Next Build
Working on:
- Display all info on a company
- News tracker based of a company
- Sentiment Analysis of every news (Good News / Neutral News / Bad News) -> Allow us to get prepare to Long / Short a stock.
- Stock Market Pattern Detection
- Email - SMS alert for reversal market


# Install

Go to `https://github.com/{group}/StockPrediction` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/StockPrediction.git
cd StockPrediction
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
StockPrediction-run
```
