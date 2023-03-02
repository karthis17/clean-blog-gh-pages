from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


def post_json():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_content = response.json()
    return blog_content


@app.route('/')
def main_page():

    return render_template('index.html', posts=post_json(), date=date)


@app.route('/<name>')
def navigate_page_load(name):
    return render_template(name, date=date)


@app.route('/<id_no>?<post_page>')
def post_content(post_page, id_no):
    return render_template(post_page, posts=post_json(), id_no=int(id_no), date=date)


if __name__ == '__main__':
    date = datetime.now()
    app.run(debug=True)
