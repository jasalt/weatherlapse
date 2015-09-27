from flask import Flask
app = Flask(__name__)


@app.route("/")
def view_home():
    return "TODO tervehdi käyttäjää ja näytä kalenteri. \nViimeisin päivä olisi myös mukava näyttää tässä."


@app.route("/day/<day>")
def view_day(day):
    return "Näkymä päivälle " + day


if __name__ == "__main__":
    app.run()
