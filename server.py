
from flask import Flask, render_template, session, redirect, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'zxcvb'

# ROUTES
@app.route('/')
def index():
    if 'gold' and 'activities' not in session:
      session['gold'] = 0
      session['activities'] = ''
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
      session['gold'] += random.randint(-50,50)
    
    if session['gold'] < 0:
        session['message'] = f'<p>You lost all of your money in at the MGM Grand in Vegas. You have lost: {session["gold"]}</p>'
    else:
        session['message'] = f'<p>You commited a Vegas Heist. Total Price: {session["gold"]}</p>'
    
    session['activities'] += session['message']
    
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)