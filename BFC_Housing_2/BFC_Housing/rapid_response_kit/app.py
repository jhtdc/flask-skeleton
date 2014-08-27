import argparse

from flask import Flask, render_template
from rapid_response_kit.utils.registry import Registry
from rapid_response_kit.tools import autorespond
from rapid_response_kit.tools import broadcast
from rapid_response_kit.tools import conference_line
from rapid_response_kit.tools import forward
from rapid_response_kit.tools import ringdown
from rapid_response_kit.tools import simplehelp
from rapid_response_kit.tools import survey
from rapid_response_kit.tools import town_hall
from rapid_response_kit.tools import volunteer_signup
from rapid_response_kit.new_views import login
from rapid_response_kit.new_views import parameters

app = Flask(__name__)
app.config.from_pyfile('utils/config.py')

app.config.apps = Registry()

autorespond.install(app)
broadcast.install(app)
conference_line.install(app)
forward.install(app)
ringdown.install(app)
simplehelp.install(app)
survey.install(app)
town_hall.install(app)
volunteer_signup.install(app)
login.install(app)
parameters.install(app)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5000, action="store",
                        help="The port to run the Twilio Toolkit on")
    parser.add_argument('--debug', default=False, action="store_true",
                        help="Turn on debug mode")
    args = parser.parse_args()
    app.run(debug=args.debug, port=args.port)
