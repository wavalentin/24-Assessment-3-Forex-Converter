from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    access_key = 'ccc2578009f8e0ac24af4c42d55dd40a'
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    url = 'http://api.exchangerate.host/convert'
    params = {
        "access_key": access_key,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['success']:
        info = {
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "result": data["result"]
        }
        return render_template("index.html", info=info)
    else:
        return render_template("index.html", error="failed to convert currency.")

    if __name__ == '__main__':
        app.run(debug=True)
