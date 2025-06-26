from flask import Flask, json, request, jsonify


app = Flask(__name__)

@app.route('/update',  methods=['PUT'])
def update():
    print("test")

if __name__ == '__main__':
    app.run(port=5000)
