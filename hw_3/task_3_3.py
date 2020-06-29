from flask import Flask
from db import run_query, ordering

app = Flask(__name__)

@app.route('/tracks/')
def tracks():
    query = '''
        SELECT COUNT(*) FROM tracks;
        '''
    return str(run_query(query))

if __name__ == '__main__':
    app.run(port=5052, debug=True)