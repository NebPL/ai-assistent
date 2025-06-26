from flask import Flask, json, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/update',  methods=['POST'])
def update():
    subprocess.run(["zsh", "/Users/ben/home/programming/personal/python_server/test.sh"], capture_output=True, text=True)
    os._exit(0)


if __name__ == '__main__':
    app.run(port=5000)
