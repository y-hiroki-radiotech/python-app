from flask import Flask, render_template, url_for, request, redirect, flash
from email_validator import validate_email, EmailNotValidError
import logging
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
app.config["DEBUG"] = True
app.logger.setLevel(logging.DEBUG)
# リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCETP_REDIRECTS"] = False
# DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    return "Hello, FlaskBook!!"

# htmlのクラス感覚でできる？
@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))  # 入力チェックが失敗した場合にリダイレクト

        # メールを送る（ここにメール送信の処理を追加）

        # 正常な処理
        flash("問い合わせありがとうございました。")
        return redirect(url_for("contact_complete"))  # 入力が有効な場合にリダイレクト

    return render_template("contact_complete.html")  # GETリクエストの場合にテンプレートをレンダリング
