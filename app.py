# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:07:21 2022

@author: ksmok
"""

from flask import Flask, render_template,request
import joblib
app = Flask(__name__)
## __name__ is a way that python want to confirm that you are the one who write this application. 
## By default, __name__ = __main__. But you can always change __name__ = abc, so whoever who takes your source code, they cannot run cause they are not abc
@app.route("/", methods=["GET", "POST"]) ## decorator -> if you want to run a program, you will need to run a decorator first before you can run the def index (below)
def index(): 
    if request.method == "POST": ## when you first run the flask, the request.method = nothing since the person haven't pressed anything (ie goes to else). Only whn the person enters the result, then it falls into the IF
    ## Enter the AI MODEL below
        rates = float(request.form.get("rates"))
        print(rates)
        model1=joblib.load("regression_DBS")
        pred1=model1.predict([[rates]])
        model2=joblib.load("tree_DBS")
        pred2=model2.predict([[rates]])
        return(render_template("index.html",result1=pred1,result2=pred2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))

### This is for CLOUD, to make ssure that you are the ownder of the code ####
if __name__=="__main__":    ### So if you put in __name__=="CM", then you're just marking that this is your code. So the other person you cannot run if their name is not CM
    app.run()