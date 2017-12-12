from flask import Flask, render_template

app_html = Flask(__name__)

@app_html.route('/')
def hello_html():
    return render_template('hello.html')