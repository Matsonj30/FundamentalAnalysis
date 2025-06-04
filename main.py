from dotenv import load_dotenv
import os
from flask import Flask, request, render_template
import time
import requests
app = Flask(__name__)


#next is notes that can save, and ratios


def cleanFinancialStatements(financialStatements):
    documentTypes = ["incomeStatement", "balancesheet", "cashFlow"]
    #useless columns to remove
    columnsToDrop = ["symbol", "reportedCurrency", "cik", "filingDate", "acceptedDate", "period"]
    #Get income sheet / balance sheet
    for documentType in documentTypes:
        #get a document for a year
        #we have to get it through key because each document type starts with "IncomeStatement" for example
        for annualDocument in financialStatements[documentType]:
            for column in columnsToDrop:
                annualDocument.pop(column)
        
    #clean values and divide by 1000
    for documentType in documentTypes:
        for annualDocument in financialStatements[documentType]:
            for entry in annualDocument:
                if type(annualDocument[entry]) == int:
                    scaledValue =  annualDocument[entry] / 1000000 #date seems to be a string so we should be okay
                    annualDocument[entry] = scaledValue
                    #annualDocument[entry] = "{:,.0f}".format(scaledValue)
    return financialStatements


def makeAPICall(ticker):
    load_dotenv()
    apiKey = os.getenv("API_KEY")
    financialStatements = {}
    print("Getting Income Statment...")
    financialStatements["incomeStatement"] = requests.get(f"https://financialmodelingprep.com/stable/income-statement?symbol={ticker}&apikey={apiKey}").json()
    time.sleep(1)
    print("Getting Balance Sheet...")
    financialStatements["balancesheet"] = requests.get(f"https://financialmodelingprep.com/stable/balance-sheet-statement?symbol={ticker}&apikey={apiKey}").json()
    time.sleep(1)
    print("Getting Cash Flow...")
    financialStatements["cashFlow"] = requests.get(f"https://financialmodelingprep.com/stable/cash-flow-statement?symbol={ticker}&apikey={apiKey}").json()
    
    return cleanFinancialStatements(financialStatements)
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

    return render_template('financials.html', 
                           ticker=ticker,
                           incomeStatements = incomeStatements,
                           balanceSheets = balanceSheets,
                           cashFlows = cashFlows)
if __name__ == '__main__':
    app.run(debug=True)