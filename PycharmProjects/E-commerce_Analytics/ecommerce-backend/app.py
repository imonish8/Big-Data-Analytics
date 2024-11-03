from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample posts (later, load from JSON or a database)
posts = [
    {"id": 1, "title": "First Post", "content": "This is my first blog post."},
    {"id": 2, "title": "Another Post", "content": "More thoughts here."}
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        new_id = len(posts) + 1
        new_post = {
            "id": new_id,
            "title": request.form['title'],
            "content": request.form['content']
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)