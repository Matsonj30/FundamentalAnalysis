# 📊 Gross Profit Margin
# Formula: (Revenue - COGS) / Revenue
# What it shows: Pricing power and product advantage.
# Target: >40% = Excellent, <20% = Red flag
def grossProfitMargin(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        gpm = (statement["revenue"] - statement["costOfRevenue"]) / statement["revenue"]
        ratios.append(round(gpm * 100, 2))  # percentage
    return ratios

# 💼 SG&A as % of Gross Profit
# Formula: SG&A / Gross Profit
# What it shows: Operational efficiency.
# Target: <30% = Ideal, >100% = Red flag (except in certain sectors)
def SGA(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        sgas = statement["sellingGeneralAndAdministrativeExpenses"] / statement["grossProfit"]
        ratios.append(round(sgas * 100, 2))
    return ratios

# 🔬 R&D as % of Gross Profit
# Formula: R&D / Gross Profit
# What it shows: Need for constant innovation.
# Target: Low = Durable product, High = Vulnerability to competition
def RD(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        rds = statement["researchAndDevelopmentExpenses"] / statement["grossProfit"]
        ratios.append(round(rds * 100, 2))
    return ratios

# 🏭 Depreciation as % of Operating Profit
# Formula: Depreciation / Operating Income
# What it shows: Capital intensity.
# Target: <10% = Great, >30–50% = Heavy CapEx business (e.g., GM)
def depreciationAsPercent(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        dap = cash["depreciationAndAmortization"] / income["operatingIncome"]
        ratios.append(round(dap * 100, 2))
    return ratios

# 💳 Interest as % of Operating Income
# Formula: Interest Expense / Operating Income
# What it shows: Debt burden and financial risk.
# Target: <15% = Excellent, >50% = Danger zone
def interestAsPercent(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        iap = statement["interestExpense"] / statement["operatingIncome"]
        ratios.append(round(iap * 100, 2))
    return ratios

# 📈 Net Earnings as % of Revenue
# Formula: Net Income / Total Revenue
# What it shows: True profitability.
# Target: >20% = Excellent, <10% = Caution
def netEarningsAsPercent(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        neap = statement["netIncome"] / statement["revenue"]
        ratios.append(round(neap * 100, 2))
    return ratios

# 🧮 Return on Assets (ROA)
# Formula: Net Income / Total Assets
# What it shows: Efficiency in asset usage.
# Target: Higher is better. Compare within industry.
def ROA(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        roas = income["netIncome"] / balance["totalAssets"]
        ratios.append(round(roas * 100, 2))
    return ratios

# 📘 Return on Equity (ROE)
# Formula: Net Income / Shareholders' Equity
# What it shows: Profitability of reinvested earnings.
# Target: >20–30% = Strong
def ROE(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        roes = income["netIncome"] / balance["totalStockholdersEquity"]
        ratios.append(round(roes * 100, 2))
    return ratios

# 🔁 Adjusted Return on Equity
# Formula: Net Income / (Equity + Treasury Stock)
# What it shows: ROE excluding effects of buybacks.
# Use when equity is reduced due to treasury stock.
def adjustedROE(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        aroe = income["netIncome"] / (balance["totalStockholdersEquity"] + balance["treasuryStock"])
        ratios.append(round(aroe * 100, 2))
    return ratios

# ⚖️ Debt to Shareholders' Equity Ratio
# Formula: Total Liabilities / Shareholders' Equity
# What it shows: Leverage and financial risk.
# Target: <0.80 (adjusted) = Durable, higher = more risk
def debtToEquity(balanceSheets):
    ratios = []
    for statement in balanceSheets:
        dte = statement["totalLiabilities"] / statement["totalStockholdersEquity"]
        ratios.append(round(dte * 100, 2))
    return ratios

# 🧾 Current Ratio
# Formula: Current Assets / Current Liabilities
# What it shows: Short-term liquidity.
# Target: >1 = Can cover debts. Some top companies run <1 due to reinvestment.
def currentRatio(balanceSheets):
    ratios = []
    for statement in balanceSheets:
        ratio = statement["totalCurrentAssets"] / statement["totalCurrentLiabilities"]
        ratios.append(round(ratio, 2))
    return ratios

# 🏗️ CapEx as % of Net Income
# Formula: CapEx / Net Income
# What it shows: Capital efficiency over time.
# Target: <50% = Great, <25% = Exceptional, >100% = Potential overextension
def capExAsPercent(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        ratio = abs(cash["capitalExpenditure"]) / income["netIncome"]
        ratios.append(round(ratio * 100, 2))
    return ratios
