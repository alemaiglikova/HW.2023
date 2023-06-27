from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()
    amount = data['amount']
    from_currency = data['from']
    to_currency = data['to']



    converted_amount = amount * 2

    result = {
        'converted_amount': converted_amount,
        'from': from_currency,
        'to': to_currency
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
