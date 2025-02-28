from flask import Flask 

# WSGI application (web server gateway interface)
app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to this best flask course. this should be an amazing course "

@app.route("/index")
def index():
    return "Welcome to index page"


if __name__=="__main__":
    app.run(debug=True)
