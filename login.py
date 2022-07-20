from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Undefined
from customers import get_cust_by_nric, deduct_credit
from products import get_product
from sqlalchemy import create_engine
from database import *
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs
import math

app.secret_key = 'my secret key'
app.config['SESSION_TYPE'] = 'filesystem'
cart_content = {}

@app.route('/', methods=["POST", "GET"])
def login():
    init_session()
    if request.method == "POST":
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

@app.route("/purchase", methods=["POST", "GET"])
def make_purchase():
    if request.method == "POST":
        to_deduct = float(request.form["t_price"])
        print("OK SO FAR : ", type(session["user_credit"]))
        session["user_credit"] = float(session["user_credit"]) - to_deduct
        deduct_credit(session["user_nric"], to_deduct)
        return render_template("purchase.html")

@app.route("/remove", methods=["POST", "GET"])
def remove():
    if request.method == 'POST':
        to_remove = request.form["t_val"]
        indi_cost = cart_content[to_remove]["t_price"]/cart_content[to_remove]["qty"]
        cart_content[to_remove]["qty"] -= 1
        cart_content[to_remove]["t_price"] = indi_cost *  cart_content[to_remove]["qty"]
        if(cart_content[to_remove]["qty"] <=0):
            cart_content.pop(to_remove)
        session["cart_content"] = cart_content
        return redirect(url_for("pos_ui"))
    else:
        redirect(url_for("cart"))
        

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


# def receipt(obj):
#     obj_name = obj.name
#     obj_price = obj.price
    
#     if obj_name not in cart_content:
#         cart_content[obj_name] = {"u_price":obj_price, "qty":1, "t_price": obj_price}
#     elif obj_name in cart_content:
#         cart_content[obj_name]["qty"] +=1
#         cart_content[obj_name]["t_price"] += obj_price
#     session["cart_content"] = cart_content
#     session["buy"] = False

@app.route('/discount', methods=["GET", "POST"])
def discount():
    if request.method == "POST":
        # return jsonify(session["discount"])
        session["discount"] = request.form["d_val"]
        print("got the form: ", request.form["d_val"])
        return redirect(url_for("pos_ui"))
    elif request.method == "GET":
        # return jsonify(session["discount"])
        return session["discount"]
    
@app.route('/setd<val>', methods=["GET"])
def set_discount(val):
    if request.method == "GET":
        # return jsonify(session["discount"])
        session["discount"] = val
        return session["discount"]

def init_session():
    global cart_content 
    cart_content= {}
    session["cart_content"] = {}
    session["user_nric"] = ""
    session["user_name"] = ""
    session["discount"] = "0.05"
    session["tax"] = "0.07"
    session["user_vocation"] = ""
    session["user_credit"] = ""
    
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    # app.run(host="0.0.0.0")
