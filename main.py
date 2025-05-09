from yahooquery import Ticker
import yahooquery
from flask import Flask, request, render_template
import time
import yfinance as yf
import requests
app = Flask(__name__)

def normalizeToMillion(value):
    return 0


def makeAPICall(ticker):
    apiKey = "Ewo20G2Yib55qkuDxwi97LqSF1XOVByp"
    financialStatments = {}
    print("Getting Income Statment...")
    financialStatments["incomeStatement"] = requests.get(f"https://financialmodelingprep.com/stable/income-statement?symbol={ticker}&apikey={apiKey}").json()
    time.sleep(1)
    print("Getting Balance Sheet...")
    financialStatments["balancesheet"] = requests.get(f"https://financialmodelingprep.com/stable/balance-sheet-statement?symbol={ticker}&apikey={apiKey}").json()
    time.sleep(1)
    print("Getting Cash Flow...")
    financialStatments["cashFlow"] = requests.get(f"https://financialmodelingprep.com/stable/cash-flow-statement?symbol={ticker}&apikey={apiKey}").json()
    return financialStatments
@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/financials', methods=['GET', 'POST'])
def financials():
    if request.method == 'POST':
        ticker = request.form.get("ticker")
        print(ticker)
        financialStatments = makeAPICall(ticker)
        incomeStatement = financialStatments["incomeStatement"]
        balanceSheet =  financialStatments["balancesheet"]
        cashFlow = financialStatments["cashFlow"]
        print(incomeStatement)
        print(balanceSheet)
        print(cashFlow)
    return render_template('financials.html', 
                           ticker=ticker,
                           incomeStatement = incomeStatement,
                           balanceSheet = balanceSheet,
                           cashFlow = cashFlow)
if __name__ == '__main__':
    app.run(debug=True)