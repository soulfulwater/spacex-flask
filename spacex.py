from flask import Flask, render_template

from app.dashboard import get_launches
from app.details import get_launch_details

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def dashboard():
    launches = get_launches()
    if launches == 'error':
        return render_template('error.html', error=True)
    else:
        return render_template('dashboard.html', launches=launches)


@app.route('/launch/<int:launch_id>')
def launch(launch_id):
    launch_details = get_launch_details(launch_id)
    if launch == 'error':
        return render_template('error.html', error=True)
    else:
        return render_template('launch_detail.html', launch=launch_details)


@app.template_filter('dt')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

@app.template_filter('yt')
def youtubelink(link):
    return link[32:]


if __name__ == '__main__':
    app.run()
