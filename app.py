from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html');


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html');


@app.route('/education')
def education():
    return render_template('education.html');


@app.route('/workexperience')
def workexperience():
    return render_template('workexperience.html');


@app.route('/projects')
def projects():
    return render_template('projects.html');


@app.route('/blog')
def blog():
    return render_template('blog.html');


if __name__ == '__main__':
    app.run()
