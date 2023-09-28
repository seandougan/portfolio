from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    page='index'
    context = {
        'page': 'index',
        'page_title': 'Home',
        'description': 'This is the Home Page for https://www.seandougan.ca',
        'keywords': 'Software, Developer, Portfolio, Sean, Dougan, Home, Canada, Toronto',
        'yourpageurl': ''
    }
    return render_template('index.html', **context);


@app.route('/aboutme')
def aboutme():
    context = {
        'page': 'aboutme',
        'page_title': 'About Sean',
        'description': 'This is a quick about me for sean',
        'keywords': 'Software, Developer, Portfolio, Sean, About Me, Pharmacy, Pharmaceutical, Logistics, Career, Apple Developer, Android, iOS, C#, Dotnet, Javascript, JS, Python, Flask, Database, Sql, Testing',
        'yourpageurl': 'aboutme'
    }
    return render_template('aboutme.html', **context);


@app.route('/education')
def education():
    context = {
        'page': 'education',
        'page_title': 'Education',
        'description': 'This is the Education Sean has Taken Relevant to his Working Experience',
        'keywords': 'Software, Developer, Portfolio, Sean, Dougan, Home, Canada, Toronto, Education, George Brown College, University of Toronto, Kinesiology',
        'yourpageurl': 'education'
    }
    return render_template('education.html', **context);


@app.route('/workexperience')
def workexperience():
    context = {
        'page': 'workexperience',
        'page_title': 'Work Experience',
        'description': 'This is Seans relevant working experience in the software industry',
        'keywords': 'Software, Developer, Portfolio, Sean, Dougan, Work Experience, Dougan Software Development, Leven Systems, Healthcare, HL7, insurance, Kibii, Canada',
        'yourpageurl': 'workexperience'
    }
    return render_template('workexperience.html', **context);


@app.route('/projects')
def projects():
    context = {
        'page': 'projects',
        'page_title': 'Projects',
        'description': 'This is the Projects Sean is passionate about and works on in his spare time',
        'keywords': 'Software, Developer, Portfolio, Sean, Dougan, Biztraak, DevEmpires, Cloud, Deploy, Code, Projects',
        'yourpageurl': 'projects'
    }
    return render_template('projects.html', **context);


@app.route('/blog')
def blog():
    context = {
        'page': 'blog',
        'page_title': 'Blogs',
        'description': 'This is a collection of markups that try to give you a good picture of what I know',
        'keywords': 'Software, Developer, Portfolio, Sean, Dougan, Blog, OOP, Coding Standards, Languages, Tips, Tricks, Information, Secrets',
        'yourpageurl': 'blog'
    }
    return render_template('blog.html', **context);


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message='Page Not Found'), 404


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate a sitemap.xml for your Flask app."""
    # Add your logic to generate the sitemap URLs dynamically
    urls = [
        {'loc': 'https://www.seandougan.ca/', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': 'https://www.seandougan.ca/aboutme', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': 'https://www.seandougan.ca/workexperience', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': 'https://www.seandougan.ca/projects', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': 'https://www.seandougan.ca/education', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': 'https://www.seandougan.ca/blogs', 'changefreq': 'weekly', 'priority': 0.7},
        # Add more URLs as needed
    ]

    response = make_response(render_template('sitemap.xml', urls=urls))
    response.headers['Content-Type'] = 'application/xml'
    return response


if __name__ == '__main__':
    app.run()
