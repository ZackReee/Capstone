from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print("HELLO WORLD")
        user = request.form["nric_input"]
        return redirect(url_for("pos_ui", nric=user))
    else:
        print("Not working")
        return render_template('login.html')


@app.route('/posui<nric>', methods=["POST", "GET"])
def pos_ui(nric):
    return render_template('posui.html', nric=nric)

        
# @app.route('/test_out<t_arg>')
# def test_out(t_arg):
#     return render_template('testoutput.html', tst=t_arg)


if __name__ == "__main__":
    app.run(debug=True)