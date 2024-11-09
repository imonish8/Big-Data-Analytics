from flask import Flask, render_template, url_for
from rich.markup import render

app = Flask(__name__)

# Sample data for projects (you can replace it with database data)
projects = [
    {
        'title': 'Data Says',
        'description': 'Description of project 1.',
        'link': '#'
    },
    {
        'title': 'V vocal',
        'description': 'Description of project 2.',
        'link': '#'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)