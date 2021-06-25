from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from tempfile import mkdtemp

db = SQL("sqlite:///DataBase.db")

app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def Home_Page():
    return render_template("index.html")

@app.route('/index.html')
def Home():
    return render_template("index.html")


@app.route('/About.html', methods=["GET", "POST"])
def About():
    if request.method == "POST":
        opinions =request.form.get("opinion")
        Problems = request.form.get("Problems")
        Suggestions = request.form.get("Suggestions")
        Any = request.form.get("Any")
        db.execute('INSERT INTO "FeedBacks" ("opinions","Problems","Suggestions", "Any") VALUES (:op,:pro,:sug,:a)'
        , op=opinions, pro=Problems, sug=Suggestions, a=Any)
        return redirect("/")
    if request.method == "GET":
        return render_template("About.html")

@app.route('/Leonardo da Vinci.html', methods=["GET"])
def Leonardo():
    return render_template("Leonardo da Vinci.html")

@app.route('/Isaac Newton.html', methods=["GET"])
def isaac():
    return render_template("Isaac Newton.html")

@app.route('/Albert Einstein.html', methods=["GET"])
def albert():
    return render_template("Albert Einstein.html")




if __name__ == '__main__':
    app.run()
