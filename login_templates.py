from flask import Flask, render_template,url_for, request
import os
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        return "User %s logged in" % request.form['username']
    else:
        return render_template('login.html')

if __name__=='__main__':
    # We can call from the terminal
    host = os.getenv('ip','0.0.0.0')
    port = int(os.getenv('Port','8080'))
    print(host,port)
    app.debug=True
    app.run(host=host,port=port)