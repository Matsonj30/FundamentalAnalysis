import dotenv

from flask import Flask, request, render_template
import time
import requests
app = Flask(__name__)

#HAVE IT SO WHEN WE HOVER A BOX, INSTEAD FO EXTENDING ITS WIDTH IT JUST OPENS A MINI WINDOW
#LIKE ON TWITCH TITLES
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
        incomeStatements = financialStatments["incomeStatement"]
        balanceSheets =  financialStatments["balancesheet"]
        cashFlows = financialStatments["cashFlow"]

        
       # print(incomeStatements)
       # print(balanceSheets)
       # print(cashFlows)
    return render_template('financials.html', 
                           ticker=ticker,
                           incomeStatements = incomeStatements,
                           balanceSheets = balanceSheets,
                           cashFlows = cashFlows)
if __name__ == '__main__':
    app.run(debug=True)