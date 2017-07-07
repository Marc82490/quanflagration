from flask import jsonify, request, render_template, redirect, url_for
from app import app, db, models, helpers
from werkzeug.security import generate_password_hash, check_password_hash

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
    
    # return the rows in JSON format
    return jsonify(results)

@app.route("/login", methods=["GET", "POST"])
def login():
    # """Log user in."""

    # # forget any user_id
    session.clear()

    # # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

    #     # ensure username was submitted
        if not request.form.get("username"):
            return 'Invalid username'

    #     # ensure password was submitted
        elif not request.form.get("password"):
            return 'Invalid password'

    #     # query database for username


    #     # ensure username exists and password is correct


    #     # remember which user has logged in
        session["user_id"] = rows[0]["id"]

    #     # redirect user to home page
        return redirect(url_for("index"))

    # # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
@helpers.login_required
def logout():
    return 'TODO'
    # """Log user out."""

    # # forget any user_id
    session.clear()

    # # redirect user to login form
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register user """
    # if reached by POST, as by submitting form
    if request.method == "POST":
        
        # check that user provided a username
        if not request.form.get("username"):
            return render_template("error.html", error="Please provide username.")
        
        # check that username is unique by querying database
        username = request.form.get("username")
        rows = models.User.query.filter_by(user_name=username).first()
        print(rows)

        if rows:
            return render_template("error.html", error="Username already taken")
        
        # check that password and confirmation are both provided
        if not request.form.get("password") or not request.form.get("confirmation"):
            return render_template("error.html", error="Please provide and confirm password.")
        
        # check that password and confirmation match
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("error.html", error="Passwords must match.")
        
        # insert new user
        new_user = models.User(user_name=username, pass_hash=generate_password_hash(request.form["password"]))
        db.session.add(new_user)
        db.session.commit()
        
        # redirect user
        return redirect(url_for("index"))
    
    # if reached by GET, as by link or redirect
    else:
        return render_template("register.html")