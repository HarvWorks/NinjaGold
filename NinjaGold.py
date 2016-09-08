from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret1'

import random
import time

@app.route('/')
def index():
    if not "gold" in session:
        session["gold"] = 0
    if not "activity" in session:
        session["activity"] = ""
    return render_template("index.html", gold = session["gold"], activity = session["activity"])

@app.route('/farm', methods = ['POST'])
def farm():
    tempGold = random.randrange(10,20)
    session["gold"] += tempGold
    session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from farming backwheat! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    return redirect('/')

@app.route('/house', methods = ['POST'])
def house():
    tempGold = random.randrange(10,12)
    session["gold"] += tempGold
    session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from cleaning someone's filty house! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    return redirect('/')

@app.route('/cave', methods = ['POST'])
def cave():
    tempGold = random.randrange(0,30)
    session["gold"] += tempGold
    session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from exploring a creepy cave! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    return redirect('/')

@app.route('/seaside', methods = ['POST'])
def seaside():
    tempGold = random.randrange(5,15)
    session["gold"] += tempGold
    session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from looking for sea shells! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    return redirect('/')

@app.route('/casino', methods = ['POST'])
def casino():
    tempGold = random.randrange(-120,100)
    session["gold"] += tempGold
    if tempGold >= 0:
        session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from playing blackjack! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    else:
        session["activity"] += "<p style='color:red;'>Lost " + str(tempGold) + " gold coins from playing the slots... You should stop gambling and losing your life savings! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
    return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset():
    session["gold"] = 0
    session["activity"] = ""
    return redirect('/')

app.run(debug=True)
