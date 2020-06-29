from flask import Flask
from db import run_query, ordering

app = Flask(__name__)

@app.route('/customers/')
def customers():
    query = '''
        SELECT * FROM customers
        '''

    country = request.args.get('country')
    if country:
        param = f" WHERE Country ='{country}'"
        query += param

    order = request.args.get('ordering')
    if order:
        param = f" ORDER BY {ordering(order)}"
        query += param

    query += ';'
    print(query)
    return str(run_query(query))

if __name__ == '__main__':
    app.run(port=5053, debug=True)