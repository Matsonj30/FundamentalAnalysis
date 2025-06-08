from dotenv import load_dotenv
import os
from flask import Flask, request, render_template
import time
import requests
import math
import ratios
app = Flask(__name__)


#next is notes that can save
#MAKE sure these ratios are the best ones for research? idk


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
    return financialStatements

def calculateRatios(financialStatements):
    incomeStatements = financialStatements["incomeStatement"]
    balanceSheets =  financialStatements["balancesheet"]
    cashFlows = financialStatements["cashFlow"]

    calculatedRatios = {}
    #add the dates tab so we can keep track
    calculatedRatios["date"] = [statement["date"] for statement in incomeStatements]
    calculatedRatios["fiscalYear"] = [statement["fiscalYear"] for statement in incomeStatements]
   
    # Then add the actual ratio calculations
    calculatedRatios.update({
        "grossProfitMargin": ratios.grossProfitMargin(incomeStatements),
        "SGA": ratios.SGA(incomeStatements),
        "RD": ratios.RD(incomeStatements),
        "depreciationAsPercent": ratios.depreciationAsPercent(incomeStatements, cashFlows),
        "interestAsPercent": ratios.interestAsPercent(incomeStatements),
        "netEarningsAsPercent": ratios.netEarningsAsPercent(incomeStatements),
        "ROA": ratios.ROA(incomeStatements, balanceSheets),
        "ROE": ratios.ROE(incomeStatements, balanceSheets),
        "adjustedROE": ratios.adjustedROE(incomeStatements, balanceSheets),
        "debtToEquity": ratios.debtToEquity(balanceSheets),
        "currentRatio": ratios.currentRatio(balanceSheets),
        "capExAsPercent": ratios.capExAsPercent(incomeStatements, cashFlows)
    })
  
    #print(calculatedRatios)
    return calculatedRatios

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
    
    ratiosToSubmit = calculateRatios(financialStatements)

    return cleanFinancialStatements(financialStatements), ratiosToSubmit


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/financials', methods=['GET', 'POST'])
def financials():
    
    if request.method == 'POST':
        ticker = request.form.get("ticker")
        print(ticker)
        financialStatements, ratiosToSubmit = makeAPICall(ticker)
        incomeStatements = financialStatements["incomeStatement"]
        balanceSheets =  financialStatements["balancesheet"]
        cashFlows = financialStatements["cashFlow"]

    return render_template('financials.html', 
                           ticker=ticker,
                           incomeStatements = incomeStatements,
                           balanceSheets = balanceSheets,
                           cashFlows = cashFlows,
                           ratios = ratiosToSubmit)
if __name__ == '__main__':
    app.run(debug=True)


