# Weatherlapse

Python Flask web application that presents timelapse content and related weather station data. Data is gathered with https://github.com/jasalt/timelapse-intra.

Example project for TIEA207 open data project course. [MIT](LICENSE) licensed.

# Development guide

    ## Setup & activate virtualenv (with help of virtualenvwrapper)

    # Without existing virtualenv (developing on Python 3.4.0):
    mkvirtualenv tiea207-demo -p python3
    pip install -r requirements.txt
    
    # With existing virtualenv:
    workon tiea207-demo

    # Run development server
    ./run-dev.py

Browse to http://localhost:5000

# Heroku deploy guide

With [Heroku Toolbelt](https://toolbelt.heroku.com/) installed and account configured:

1) Clone repository `git clone <repository url>`

2) Create Heroku app `heroku create <application_name>`

3) Push local repository to Heroku `git push heroku master`

4) Access application at `http://<application_name>.herokuapp.com`

# Related projects
https://github.com/dandelany/animate-earth
