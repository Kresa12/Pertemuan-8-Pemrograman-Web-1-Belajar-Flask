from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    myname = "Palpale"
    return render_template('index.html')

@app.route('/about')
def about():
    return "selamat datang di halaman about"