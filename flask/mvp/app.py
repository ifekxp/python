from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'data': 'This is home page'})

@app.route('/about', methods=['GET'])
def about():
    return jsonify({'data': 'This is about page'})

@app.route('/welcome/<name>', methods=['GET'])
def welcome(name):
    return jsonify({'data': 'Welcome ' + name})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
