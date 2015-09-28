from flask import Flask, render_template, Blueprint
import chartkick
from app.youtube import daily_videos
from app.weather import daily_data

app = Flask(__name__)

# Chartkick initialization
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(),
               static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")


@app.route("/")
def view_home():
    return render_template('home.html', videos=daily_videos)


@app.route("/day/<date>")
def view_day(date):
    mock_data = [{'data': [['2013-04-01 00:00:00 UTC', 52.9],
                           ['2013-05-01 00:00:00 UTC', 50.7],
                           ['2013-06-01 00:00:00 UTC', 46.7],
                           ['2013-07-01 00:00:00 UTC', 59.7],
                           ['2013-08-01 00:00:00 UTC', 55.7],
                           ['2013-09-01 00:00:00 UTC', 74.7],
                           ['2013-10-01 00:00:00 UTC', 60.7]],
                  'name': 'Chrome'},
                 {'data': [['2013-04-01 00:00:00 UTC', 27.7],
                           ['2013-05-01 00:00:00 UTC', 32.9],
                           ['2013-06-01 00:00:00 UTC', 54.9],
                           ['2013-07-01 00:00:00 UTC', 38.9],
                           ['2013-08-01 00:00:00 UTC', 30.9],
                           ['2013-09-01 00:00:00 UTC', 15.9],
                           ['2013-10-01 00:00:00 UTC', 60.9]],
                  'name': 'Firefox'}]
    date = int(date)
    try:
        video_id = daily_videos[date].videoid
        print("Show video %s for day %s." % (video_id, date))
    except:
        video_id = None
        print("No video for date.")

    days = list(daily_videos.keys())
    this_index = days.index(int(date))

    try:
        assert this_index != 0
        prev_day = days[this_index - 1]
    except:
        prev_day = None

    try:
        next_day = days[this_index + 1]
    except:
        next_day = None

    return render_template('day.html',
                           video_id=video_id, weather_data=daily_data.get(date),
                           day=date, prev_day=prev_day, next_day=next_day)

if __name__ == "__main__":
    app.run(debug=True)
