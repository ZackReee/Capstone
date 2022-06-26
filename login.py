from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print("HELLO WORLD")
        user = request.form["nric_input"]
        return redirect(url_for("pos_ui", nric=user))
    else:
        print("Not working")
        return render_template('login.html')

@app.route('/test', methods=["POST", "GET"])
def test():
    if request.method == "POST":
        print("HELLO WORLD")
        # user = request.form["test"]
        # return redirect(url_for("pos_ui", nric=user))
        return("<h1>Welcome user</h1>")
    else:
        print("Not working")
        return render_template('test.html')


@app.route('/posui<nric>', methods=["POST", "GET"])
def pos_ui(nric):
    # return render_template('posui.html')
    return f"<h1> {nric} </h1>"

if __name__ == "__main__":
    app.run(debug=True)