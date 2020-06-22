from faker import Faker
from flask import Flask, request

app = Flask(__name__)

@app.route('/generate-users/') #
def generate_users() -> str:

    length = int(request.args['length'])

    fake = Faker()
    fake.name()
    fake.email()

    f = ''
    for _ in range(length):

        f += fake.name()+' '+fake.email()
        #print(f)

    return f



if __name__ == "__main__":
    app.run(port=5087)