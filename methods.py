from flask import Flask, render_template,url_for, request
import os
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    # PAss variables using the GET method
    #if request.values:
    if request.method =='POST':
        return 'username is '+request.values["username"] # Request values is holding all the inputs
    else:
        #return '<form method="get" action="/login"><input type = "text" name="username" /><p><button type ="submit">Submit</button></form>'
        return '<form method="post" action="/login"><input type = "text" name="username" /><p><button type ="submit">Submit</button></form>'
if __name__=='__main__':
    # We can call from the terminal
    host = os.getenv('ip','0.0.0.0')
    port = int(os.getenv('Port','8080'))
    print(host,port)
    #app.debug=True
    app.run(host=host,port=port)