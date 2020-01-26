from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    return render_template("submit.html", user_name=request.form['name'], location=request.form['dojo_location'], language=request.form['favorite_language'], com=request.form['comment'])


if __name__ == "__main__":
    app.run(debug=True)
