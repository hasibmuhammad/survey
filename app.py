from ast import main
from email import message
from importlib.metadata import requires
from flask import Flask, render_template, request

app = Flask(__name__)


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
            return render_template('index.html', message="Plese enter all required fields!")
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
