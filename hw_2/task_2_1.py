from flask import Flask

app = Flask(__name__)

@app.route('/requirements/')
def file_open():
    file = open('requirements.txt', 'r')
    return file.read()
    f.close()

if __name__ == "__main__":
    app.run(port=5085)
