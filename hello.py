from flask import Flask, render_template
import os
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"
    
if __name__=='__main__':
    # We can call from the terminal
    host = os.getenv('ip','0.0.0.0')
    port = int(os.getenv('Port','8080'))
    print(host,port)
    app.run(host=host,port=port)