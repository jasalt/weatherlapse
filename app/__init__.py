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


@app.route("/<int:year>/<int:month>/<int:day>")
def view_day(year, month, day):
    try:
        video_id = daily_videos[year][month][day].videoid
        print("Show video %s for day %s-%s-%s." % (video_id, year, month, day))
    except:
        video_id = None
        print("No video for day.")

    # days = list(daily_videos.keys())

    # TODO fix pagination
    this_index = 0  # days.index(int(day))
    
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
                           video_id=video_id,
                           weather_data=daily_data.get(day),
                           day=day, prev_day=prev_day, next_day=next_day)

if __name__ == "__main__":
    app.run(debug=True)
