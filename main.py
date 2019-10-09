from flask import Flask, flash, request, render_template, url_for, redirect
from QABot import max_qa_bot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    query = request.form['query']
    question = request.args.get('q', query)
    return render_template("home.html") + '<br>' + max_qa_bot(question)

if __name__ == "__main__":
    app.run(debug=True)
