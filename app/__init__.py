from flask import Flask, render_template, Blueprint, request
import chartkick
from app.youtube import all_videos
from app.weather import weather_data
from app.utils import has_next_day
from app.utils import has_previous_day
import os
from glob import glob
from werkzeug import secure_filename
from functools import wraps
from flask import request, Response
from app.utils import get_env
from flask import send_from_directory


app = Flask(__name__)
UPLOAD_PATH = os.environ['HOME'] + '/last-capture'
if not os.path.exists(UPLOAD_PATH):
    os.makedirs(UPLOAD_PATH)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

# Chartkick initialization
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(),
               static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")


last_capture = ''
@app.route("/")
def view_home():
    try:
        last_capture = os.path.basename(glob(app.config['UPLOAD_FOLDER'] + '/*')[0])[:-4]
    except:
        last_capture = None
    return render_template('home.html',
                           last_capture=last_capture,
                           videos=all_videos)


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

@app.route("/last-capture")
def view_last_capture():
    last_filename = os.path.basename(glob(app.config['UPLOAD_FOLDER'] + '/*')[0])
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               last_filename)


#### Fileupload secured with basic auth
# set env variables UPLOAD_USER and UPLOAD_PASSWORD
# curl -u <user>:<pass> -v -F name=test -F upload=@image.jpg http://localhost:5000/upload
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == get_env('UPLOAD_USER') and password == get_env('UPLOAD_PASSWORD')

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/upload", methods=['POST'])
@requires_auth
def view_upload():
    file = request.files['upload']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print('Received file ' + filename)
        files = glob(app.config['UPLOAD_FOLDER'] + '/*')
        print('Removing old images ' + str(files)) 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File %s uploaded!" % filename
    
if __name__ == "__main__":
    app.run(debug=True)
