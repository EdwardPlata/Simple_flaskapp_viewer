from flask import Flask, render_template,url_for, request
import os
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)
if __name__=='__main__':
    # We can call from the terminal
    host = os.getenv('ip','0.0.0.0')
    port = int(os.getenv('Port','8080'))
    print(host,port)
    #app.debug=True
    app.run(host=host,port=port)