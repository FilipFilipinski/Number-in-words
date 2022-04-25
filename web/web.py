from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('number.html')


@app.route('/<name>/')
def user_view(name):
    return name


if __name__ == '__main__':
    app.run(debug=True)
