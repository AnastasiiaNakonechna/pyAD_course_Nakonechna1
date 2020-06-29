from flask import Flask
from db import run_query, ordering

app = Flask(__name__)

@app.route('/names/')
def names():
    query = '''
        SELECT DISTINCT FirstName FROM customers ORDER BY FirstName ASC;
        '''
    return str(run_query(query))

if __name__ == '__main__':
    app.run(port=5051, debug=True)