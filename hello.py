from flask import Flask, render_template,url_for
import os
app = Flask(__name__)
@app.route('/')
def index():
    return url_for('show_user_profile',username='Edgie')

@app.route('/user/<username>')
def show_user_profile(username):
    #Show user profile for that user
    return "User %s" % username
    
@app.route('/hello')
def hello_world():
    return "Hello World"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id
# WHen debugging we can see our errors in the next page
if __name__=='__main__':
    # We can call from the terminal
    host = os.getenv('ip','0.0.0.0')
    port = int(os.getenv('Port','8080'))
    print(host,port)
    #app.debug=True
    app.run(host=host,port=port)