from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from jinja2 import Undefined
from customers import get_cust_by_nric
from products import get_product
from sqlalchemy import create_engine
from database import *
import json


@app.route('/', methods=["POST", "GET"])
def login():
    # session = Session()
    session["cart_content"] = [{}]
    if request.method == "POST":
        print("POST login")
        user = request.form["nric_input"].upper()
        user_result = get_cust_by_nric(user)
        
        if (user_result != "" and user_result != None):
            session["user_nric"] = user_result.nric
            session["user_name"] = user_result.name
            session["user_vocation"] = user_result.vocation
            session["user_credit"] = user_result.credit
            print("DELETE THIS ONLY TEST: ", session["user_credit"])
            return redirect(url_for("pos_ui"))
        else:
            return render_template('loginfail.html')
    else:
        print("GET login")
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/posui', methods=["POST", "GET"])
def pos_ui():
    if request.method == 'GET':
        return render_template('posui.html')
    elif request.method == 'POST':
         # p_result = get_product(request.form["barcode_input"].upper())
        # return jsonify({"num clicked:": session["num"]})
        session["cart_content"] = request.form["barcode_input"].upper()
        if session["cart_content"] == "":
            return "EMPTY"
        else:
             return render_template('posui.html')
            # return redirect(url_for("pos_ui"))

@app.route('/test')
def my_link():
    print("Clicked for HTML")
    session['test'] = "Private Kendo club"
    return render_template('posui.html')


@app.route('/pos2')
def tempt():
    return render_template('posui.html')


@app.route("/cart")
def cart():
    if session["cart_content"] == "" or session["cart_content"] == [{}]:
        return "EMPTY"
    else:
        return session["cart_content"]
        

# @app.route('/cart', methods=["PUT"])
# def cart():
#     title = "cart"
#     content = "conttttent"


if __name__ == "__main__":
    app.secret_key = 'my secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
    # app.run(host="0.0.0.0")