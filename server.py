from crypt import methods
from flask import Flask, render_template, session, redirect, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'zxcvb'

# ROUTES
@app.route('/')
def index():
    if 'gold' not in session:
      session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
      session['gold'] += random.randint(10,20)
    elif request.form['building'] == 'cave':
      session['gold'] += random.randint(5,10)
    elif request.form['building'] == 'house':
      session['gold'] += random.randint(2,5)
    elif request.form['building'] == 'casino':
      session['gold'] += random.randint(0,50)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)