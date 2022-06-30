from flask import Flask, redirect, url_for, render_template, request
from jinja2 import Undefined
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print("POST login")
        user = request.form["nric_input"].upper()
        if (user=="" or user==Undefined):
            return render_template('login.html')
        else:
            return redirect(url_for("pos_ui", nric=user))
    else:
        print("GET login")
        return render_template('login.html')


@app.route('/posui<nric>')
def pos_ui(nric):
    return render_template('posui.html', nric=nric)

@app.route('/posui')
def redirect_pos_ui():
    return redirect(url_for("login"))

        
# @app.route('/test_out<t_arg>')
# def test_out(t_arg):
#     return render_template('testoutput.html', tst=t_arg)


if __name__ == "__main__":
    app.run(debug=False)