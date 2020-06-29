from flask import Flask
from db import run_query, ordering

app = Flask(__name__)

@app.route('/tracks-sec/')
def trackssec():
    query = '''
        SELECT TrackId, Name, Milliseconds*0.001 FROM tracks;
        '''
    print(query)
    return str(run_query(query))

if __name__ == '__main__':
    app.run(port=5053, debug=True)