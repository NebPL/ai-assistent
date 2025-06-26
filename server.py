from flask import Flask, json, request, jsonify
import subprocess
import os
import threading

#from main import stopProgram

app = Flask(__name__)

@app.route('/update',  methods=['POST'])
def update():
    #subprocess.run(["zsh", "/Users/ben/home/programming/personal/python_server/test.sh"], capture_output=True, text=True)

    #result = subprocess.run(["git", "pull"], cwd="/Users/ben/home/programming/personal/ai-assistent", capture_output=True, text=True)
    #subprocess.run(["zsh", "/Users/ben/home/programming/personal/python_server/startup.sh"])
   
#    stopProgram()
    print("Update")
    os._exit(0)
    return "OK"

def start_flask():
    app.run(port=5000)
    
threading.Thread(target=start_flask, daemon=True).start()
