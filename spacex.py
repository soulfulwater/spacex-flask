from datetime import datetime
import random

from flask import Flask, render_template, redirect, url_for

from app.dashboard import get_launches
from app.details import get_launch_details

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def dashboard():
    launches = get_launches()
    if launches == 'error':
        return render_template('bs/error.html', error=True)
    else:
        return render_template('bs/dashboard.html', launches=launches)


@app.route('/all-launches/')
def launches():
    launches = get_launches(return_all=True)
    if launches == 'error':
        return render_template('bs/error.html', error=True)
    else:
        return render_template('bs/alllaunches.html', launches=launches)


@app.route('/launch/<int:launch_id>')
def launch(launch_id):
    launch_details = get_launch_details(launch_id)
    if launch == 'error':
        return render_template('bs/error.html', error=True)
    else:
        return render_template('bs/launch_detail.html', launch=launch_details)


@app.route('/random/')
def random_launch():
    launches = get_launches(return_all=True)
    secure_random = random.SystemRandom()
    choice = secure_random.choice(launches)
    return redirect(url_for('launch', launch_id=choice['flight_number']))


@app.template_filter('dt')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

@app.template_filter('detail_dt')
def datetimeformat_detail(value, format='%H:%M / %d-%m-%Y'):
    datetime_object = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    return datetime_object.strftime(format)

@app.template_filter('yt')
def youtubelink(link):
    return link[32:]


if __name__ == '__main__':
    app.run()
