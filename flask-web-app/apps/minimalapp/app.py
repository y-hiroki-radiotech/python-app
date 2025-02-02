from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, FlaskBook!!"

# htmlのクラス感覚でできる？
@app.route("/hello",
           methods=["GET"],
           endpoint="hello-endpoint")
def hello():
    return "Hello, Worlds!!!"
