from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hi')
def say_hi():
    return '<h1>Hi there!</h1>'

@app.route('/hello')
def say_hello():
    return '<h1>Hello...</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

