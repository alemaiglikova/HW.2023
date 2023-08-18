from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/valute')
def get_random_data():
    currencies = ['USD', 'EUR', 'JPY', 'GBP']
    random_currency = random.choice(currencies)
    random_value = round(random.uniform(0.5, 2.0), 2)
    data = {
        'currency': random_currency,
        'value': random_value
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
