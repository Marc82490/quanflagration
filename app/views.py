from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/chart')
def chart():
    return render_template("graph.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return 'TODO'
    # """Log user in."""

    # # forget any user_id
    # session.clear()

    # # if user reached route via POST (as by submitting a form via POST)
    # if request.method == "POST":

    #     # ensure username was submitted
    #     if not request.form.get("username"):
    #         return 'Invalid username'

    #     # ensure password was submitted
    #     elif not request.form.get("password"):
    #         return 'Invalid password'

    #     # query database for username


    #     # ensure username exists and password is correct


    #     # remember which user has logged in
    #     session["user_id"] = rows[0]["id"]

    #     # redirect user to home page
    #     return redirect(url_for("index"))

    # # else if user reached route via GET (as by clicking a link or via redirect)
    # else:
    #     return render_template("login.html")

@app.route("/logout")
def logout():
    return 'TODO'
    # """Log user out."""

    # # forget any user_id
    # session.clear()

    # # redirect user to login form
    # return redirect(url_for("login"))