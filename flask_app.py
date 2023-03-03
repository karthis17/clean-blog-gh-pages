from flask import Flask, render_template, request
from datetime import datetime
import requests
import smtplib

app = Flask(__name__)


def post_json():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_content = response.json()
    return blog_content


def form_mail(name, email, phone, message):
    email_me = YOUR_MAIL_DI
    password_me = YOUR_MAIL_DI_PASSWORD
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email_me, password_me)
        connection.sendmail(from_addr=email_me, to_addrs="karthiscar602@gmail.com", msg=email_message)


@app.route('/')
def main_page():
    return render_template('index.html', posts=post_json(), date=date)


@app.route('/<name>')
def navigate_page_load(name):
    return render_template(name + ".html", date=date)


@app.route('/<int:id_no>?<post_page>')
def post_content(post_page, id_no):
    return render_template(post_page, posts=post_json(), id_no=id_no, date=date)


@app.route('/contact', methods=["POST", "GET"])
def contact_form():
    if request.method == 'POST':
        received_name = request.form['name']
        received_email = request.form['email']
        received_phone_no = request.form['phone_no']
        received_message = request.form['message']
        form_mail(received_name, received_email, received_phone_no, received_message)
        return render_template("contact.html", date=date, is_msg=True)
    return render_template('contact.html', date=date, is_msg=False)


if __name__ == '__main__':
    date = datetime.now()
    app.run(debug=True)
