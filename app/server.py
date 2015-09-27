from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def view_home():
    return render_template('home.html')


@app.route("/day/<date>")
def view_day(date):
    return render_template('day.html', day=date)


if __name__ == "__main__":
    app.run(debug=True)
