import yahooquery as yq
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/financials')
def financials(ticker):
    ticker = request.form.get("ticker")
    return render_template('financials.html', ticker=ticker)
if __name__ == '__main__':
    app.run(debug=True)