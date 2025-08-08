# 📊 Gross Profit Margin
# Formula: (Revenue - COGS) / Revenue
# What it shows: Pricing power and product advantage.
# Target: >40% = Excellent, <20% = Red flag
def grossProfitMargin(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        revenue = statement["revenue"]
        cost = statement["costOfRevenue"]
        if revenue == 0:
            ratios.append("NA")
        else:
            gpm = (revenue - cost) / revenue
            ratios.append(round(gpm * 100, 2))  # percentage
    return ratios

# 💼 SG&A as % of Gross Profit
# Formula: SG&A / Gross Profit
# What it shows: Operational efficiency.
# Target: <30% = Ideal, >100% = Red flag (except in certain sectors)
def SGA(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        gross_profit = statement.get("grossProfit", 0)
        sga = statement.get("sellingGeneralAndAdministrativeExpenses", 0)
        if gross_profit == 0:
            ratios.append("NA")
        else:
            sgas = sga / gross_profit
            ratios.append(round(sgas * 100, 2))  # percentage
    return ratios
# 🔬 R&D as % of Gross Profit
# Formula: R&D / Gross Profit
# What it shows: Need for constant innovation.
# Target: Low = Durable product, High = Vulnerability to competition
def RD(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        gross_profit = statement.get("grossProfit", 0)
        rd = statement.get("researchAndDevelopmentExpenses", 0)
        if gross_profit == 0:
            ratios.append("NA")
        else:
            rds = rd / gross_profit
            ratios.append(round(rds * 100, 2))  # percentage
    return ratios

# 🏭 Depreciation as % of Operating Profit
# Formula: Depreciation / Operating Income
# What it shows: Capital intensity.
# Target: <10% = Great, >30–50% = Heavy CapEx business (e.g., GM)
def depreciationAsPercent(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        op_income = income.get("operatingIncome", 0)
        depreciation = cash.get("depreciationAndAmortization", 0)
        if op_income == 0:
            ratios.append("NA")
        else:
            dap = depreciation / op_income
            ratios.append(round(dap * 100, 2))  # percentage
    return ratios


# 💳 Interest as % of Operating Income
# Formula: Interest Expense / Operating Income
# What it shows: Debt burden and financial risk.
# Target: <15% = Excellent, >50% = Danger zone
def interestAsPercent(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        interest = statement.get("interestExpense", 0)
        operating_income = statement.get("operatingIncome", 0)
        if operating_income == 0:
            ratios.append("NA")
        else:
            iap = interest / operating_income
            ratios.append(round(iap * 100, 2))  # percentage
    return ratios

# 📈 Net Earnings as % of Revenue
# Formula: Net Income / Total Revenue
# What it shows: True profitability.
# Target: >20% = Excellent, <10% = Caution
def netEarningsAsPercent(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        net_income = statement.get("netIncome", 0)
        revenue = statement.get("revenue", 0)
        if revenue == 0:
            ratios.append("NA")
        else:
            neap = net_income / revenue
            ratios.append(round(neap * 100, 2))  # percentage
    return ratios


# 🧮 Return on Assets (ROA)
# Formula: Net Income / Total Assets
# What it shows: Efficiency in asset usage.
# Target: Higher is better. Compare within industry.
def ROA(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        net_income = income.get("netIncome", 0)
        total_assets = balance.get("totalAssets", 0)
        if total_assets == 0:
            ratios.append("NA")
        else:
            roas = net_income / total_assets
            ratios.append(round(roas * 100, 2))  # percentage
    return ratios


# 📘 Return on Equity (ROE)
# Formula: Net Income / Shareholders' Equity
# What it shows: Profitability of reinvested earnings.
# Target: >20–30% = Strong
def ROE(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        net_income = income.get("netIncome", 0)
        equity = balance.get("totalStockholdersEquity", 0)
        if equity == 0:
            ratios.append("NA")
        else:
            roes = net_income / equity
            ratios.append(round(roes * 100, 2))  # percentage
    return ratios


# 🔁 Adjusted Return on Equity
# Formula: Net Income / (Equity + Treasury Stock)
# What it shows: ROE excluding effects of buybacks.
# Use when equity is reduced due to treasury stock.
def adjustedROE(incomeStatements, balanceSheets):
    ratios = []
    for income, balance in zip(incomeStatements, balanceSheets):
        net_income = income.get("netIncome", 0)
        equity = balance.get("totalStockholdersEquity", 0)
        treasury = balance.get("treasuryStock", 0)

        # Version 2: equity only
        denominator = equity

        # Version 3: adjusted to exclude treasury stock (uncomment to use)
        # denominator = equity + treasury

        if denominator == 0:
            ratios.append("NA")
        else:
            aroe = net_income / denominator
            ratios.append(round(aroe * 100, 2))  # percentage
    return ratios

# ⚖️ Debt to Shareholders' Equity Ratio
# Formula: Total Liabilities / Shareholders' Equity
# What it shows: Leverage and financial risk.
# Target: <0.80 (adjusted) = Durable, higher = more risk
#Should not be a percent NEED TO FIX
def debtToEquity(balanceSheets):
    ratios = []
    for statement in balanceSheets:
        liabilities = statement.get("totalLiabilities", 0)
        equity = statement.get("totalStockholdersEquity", 0)
        if equity == 0:
            ratios.append("NA")
        else:
            dte = liabilities / equity
            ratios.append(round(dte, 2))
    return ratios


# 🧾 Current Ratio
# Formula: Current Assets / Current Liabilities
# What it shows: Short-term liquidity.
# Target: >1 = Can cover debts. Some top companies run <1 due to reinvestment.
def currentRatio(balanceSheets):
    ratios = []
    for statement in balanceSheets:
        current_assets = statement.get("totalCurrentAssets", 0)
        current_liabilities = statement.get("totalCurrentLiabilities", 0)
        if current_liabilities == 0:
            ratios.append("NA")
        else:
            ratio = current_assets / current_liabilities
            ratios.append(round(ratio, 2))
    return ratios


# 🏗️ CapEx as % of Net Income
# Formula: CapEx / Net Income
# What it shows: Capital efficiency over time.
# Target: <50% = Great, <25% = Exceptional, >100% = Potential overextension
def capExAsPercent(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        capex = abs(cash.get("capitalExpenditure", 0))
        net_income = income.get("netIncome", 0)
        if net_income == 0:
            ratios.append("NA")
        else:
            ratio = capex / net_income
            ratios.append(round(ratio * 100, 2))  # percentage
    return ratios



def interestCoverage(incomeStatements):
    ratios = []
    for statement in incomeStatements:
        interest = statement.get("interestExpense", 0)
        operating_income = statement.get("operatingIncome", 0)
        if interest > 0:
            ratio = operating_income / interest
            ratios.append(round(ratio, 2))
        else:
            ratios.append("NA")
    return ratios


def freeCashFlowMargin(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        fcf = cash.get("freeCashFlow", 0)
        revenue = income.get("revenue", 0)
        if revenue == 0:
            ratios.append("NA")
        else:
            ratio = fcf / revenue
            ratios.append(round(ratio * 100, 2))  # percentage
    return ratios

def cashConversionRatio(incomeStatements, cashFlows):
    ratios = []
    for income, cash in zip(incomeStatements, cashFlows):
        ocf = cash.get("operatingCashFlow", 0)
        net_income = income.get("netIncome", 0)
        if net_income == 0:
            ratios.append("NA")
        else:
            ratio = ocf / net_income
            ratios.append(round(ratio * 100, 2))  # percentage
    return ratios


def ROIC(incomeStatements, balanceSheets):
    ratios = []

    for income, balance in zip(incomeStatements, balanceSheets):
        try:
            # Step 1: NOPAT = operatingIncome × (1 - tax rate)
            ebit = income["operatingIncome"]
            income_before_tax = income["incomeBeforeTax"]
            income_tax = income["incomeTaxExpense"]

            tax_rate = income_tax / income_before_tax if income_before_tax else 0
            nopat = ebit * (1 - tax_rate)

            # Step 2: Invested Capital = Short-Term Debt + Long-Term Debt + Equity - Cash
            short_term_debt = balance.get("shortTermDebt", 0)
            long_term_debt = balance.get("longTermDebt", 0)
            total_equity = balance["totalStockholdersEquity"]
            cash = balance["cashAndCashEquivalents"]

            invested_capital = short_term_debt + long_term_debt + total_equity - cash

            # Avoid division by zero
            if invested_capital == 0:
                ratios.append("N/A")
            else:
                ratios.append(round(((nopat / invested_capital) * 100),2))

        except (KeyError, ZeroDivisionError):
            ratios.append("N/A")

    return ratios
