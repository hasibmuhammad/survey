from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/survey'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Survey(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True)
    issue = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, issue, rating, comments):
        self.user = user
        self.issue = issue
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        issue = request.form['issues']
        rating = request.form['rating']
        comment = request.form['comments']
        # print(user, issue, rating, comment)
        if user == '' or issue == '':
            return render_template('index.html', message="Please enter all required fields!")

        if db.session.query(Survey).filter(Survey.user == user).count() == 0:
            data = Survey(user, issue, rating, comment)
            db.session.add(data)
            db.session.commit()

            # After Inserting the data to the database -> sending an email with information
            send_mail(user, issue, rating, comment)

            return render_template('success.html')
        else:
            return render_template('index.html', message="You have already responded to the survey!")


if __name__ == '__main__':
    app.run()
