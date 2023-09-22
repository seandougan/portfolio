from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html');

@app.route('/aboutme')
def aboutme():  # put application's code here
    return render_template('aboutme.html');

@app.route('/education')
def education():  # put application's code here
    return render_template('education.html');

@app.route('/workexperience')
def workexperience():  # put application's code here
    return render_template('workexperience.html');

@app.route('/projects')
def projects():  # put application's code here
    return render_template('projects.html');


if __name__ == '__main__':
    app.run()
