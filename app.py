from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return f'olicek inşallah guzum hadi bakalım'

if __name__ == '__main__':
    app.run()