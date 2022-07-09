from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from jinja2 import Undefined
from customers import get_cust_by_nric
from products import get_product
from sqlalchemy import create_engine
from database import *
import json

# TO DO: TRY TO FIX CART CONTENT
# SESS DONT WORK SO TRY MAYBE GLOBAL VAR
cart_content = {}

@app.route('/', methods=["POST", "GET"])
def login():
    init_session()
    # session = Session()
    # session["cart_content"] = [{}]
    if request.method == "POST":
        print("POST login")
        user = request.form["nric_input"].upper()
        user_result = get_cust_by_nric(user)
        if (user_result != "" and user_result != None):
            session["logged_in"] = True
            session["user_nric"] = user_result.nric
            session["user_name"] = user_result.name
            session["user_vocation"] = user_result.vocation
            session["user_credit"] = user_result.credit
            return redirect(url_for("pos_ui"))
        else:
            return render_template('loginfail.html')
    elif request.method == "GET":
        print("GET login")
        return render_template('login.html')

@app.route('/logout', methods=["POST", "GET"])
def logout():
    if request.method=="GET":
        session.clear()
        global cart_content
        cart_content = {}
        session["cart_content"] = {}
        return render_template('logout.html')
    else:
        init_session()
    # session = Session()
    # session["cart_content"] = [{}]
    if request.method == "POST":
        print("POST login")
        user = request.form["nric_input"].upper()
        user_result = get_cust_by_nric(user)
        if (user_result != "" and user_result != None):
            session["logged_in"] = True
            session["user_nric"] = user_result.nric
            session["user_name"] = user_result.name
            session["user_vocation"] = user_result.vocation
            session["user_credit"] = user_result.credit
            return redirect(url_for("pos_ui"))
        else:
            return render_template('loginfail.html')
        

@app.route('/posui', methods=["POST", "GET"])
def pos_ui():
    if request.method == 'POST':
        print("POSTING: ", request.form["barcode_input"])
        try:
            p_result = get_product(request.form["barcode_input"].upper())
            add_to_cart(p_result)
        except:
            print("RETRIEVAL ERROR")
        return redirect(url_for("pos_ui"))
    elif(request.method == 'GET'):
        try:
            a = session["logged_in"]
        except:
            return redirect(url_for("login"))
    return render_template('posui.html')


@app.route("/cart")
def cart():
    if len(cart_content) == 0:
        return {}
    else:
        return jsonify(session["cart_content"])
    
@app.route("/credit")
def credit():
    return jsonify(session["user_credit"])
        

def add_to_cart(obj):
    obj_name = obj.name
    obj_price = obj.price
    
    if obj_name not in cart_content:
        cart_content[obj_name] = {"u_price":obj_price, "qty":1, "t_price": obj_price}
    elif obj_name in cart_content:
        cart_content[obj_name]["qty"] +=1
        cart_content[obj_name]["t_price"] += obj_price
    session["cart_content"] = cart_content
    session["buy"] = False

def init_session():
    global cart_content 
    cart_content= {}
    session["cart_content"] = {}
    session["user_nric"] = ""
    session["user_name"] = ""
    session["user_vocation"] = ""
    session["user_credit"] = ""

if __name__ == "__main__":
    app.secret_key = 'my secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
    # app.run(host="0.0.0.0")