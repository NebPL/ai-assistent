from flask import Flask, json, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/update',  methods=['PUT'])
def update():
    result = subprocess.run(["zsh", "/Users/ben/home/programming/personal/python_server/test.sh"], capture_output=True, text=True)

    print("Ausgabe:")
    print(result.stdout)


if __name__ == '__main__':
    app.run(port=5000)
