from flask import Flask, render_template, Blueprint
import chartkick
from app.youtube import all_videos
from app.weather import weather_data
from app.utils import has_next_day
from app.utils import has_previous_day

app = Flask(__name__)

# Chartkick initialization
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(),
               static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")


@app.route("/")
def view_home():
    return render_template('home.html', videos=all_videos)


@app.route("/<int:year>/<int:month>/<int:day>")
def view_day(year, month, day):
    try:
        video_id = all_videos[year][month][day].videoid
        print("Show video %s for day %s-%s-%s." % (video_id, year, month, day))
    except:
        video_id = None
        print("No video for day.")

    weather = weather_data.get("%04d%02d%02d" % (year, month, day))
    return render_template('day.html',
                           video_id=video_id, weather=weather, day=day,
                           prev_day=has_previous_day(all_videos,
                                                     year, month, day),
                           next_day=has_next_day(all_videos,
                                                 year, month, day))

if __name__ == "__main__":
    app.run(debug=True)
