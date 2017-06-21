from flask import jsonify, request, render_template
from app import app, db, models


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")

@app.route('/search')
def search():
    """ Search for places that match entry """

    # get query from GET request and append wildcard
    q = request.args.get("q")

    # select rows from the database that are LIKE the query
    rows = models.Symbol.query.filter(models.Symbol.ticker_symbol.like(q+'%')).all()
    results=[row.serialize() for row in rows]
    print(results)
    
    # return the rows in JSON format
    return jsonify(results)

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