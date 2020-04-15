from flask import Flask, render_template, request, url_for, redirect
import cgi
# FLASK LIBRARY AND SPECIFIC MODULES.

app = Flask("MyApp")
# FLASK REDEFINED AS 'APP'.

@app.route("/")
def index ():
    return render_template("welcome.html")

@app.route("/gold")
def contact ():
    return render_template("gold.html")

@app.route('/gold', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['genre'] == "Research":
            return redirect(url_for('research'))
        if request.form['genre'] == "Industrial":
            return redirect(url_for('industrial'))
        if request.form['genre'] == "Personal":
            return redirect(url_for('personal'))
        else:
            error = 'We do not provide this service'
    return render_template('welcome.html', error=error)

@app.route("/Research")
def rock():
    return render_template("research.html")

@app.route("/Industrial")
def classical():
    return render_template("industrial.html")

@app.route("/Personal")
def jazz():
    return render_template("personal.html")

app.run(debug=True)
