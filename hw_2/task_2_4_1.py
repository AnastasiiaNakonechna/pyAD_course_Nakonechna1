import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route('/space/')
def show_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return str(r.json()['number'])

if __name__ == "__main__":
    app.run(port=5090)
