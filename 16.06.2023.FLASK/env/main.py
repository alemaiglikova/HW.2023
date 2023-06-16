import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/send_dict', methods=['GET'])
def send_dict():
    my_dict = {"key1": "value1", "key2": "value2"}


    json_data = json.dumps(my_dict)


    response = requests.post('http://127.0.0.1:8000/home', data=json_data)

    return 'Success'

if __name__ == '__main__':
    app.run()