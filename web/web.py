from flask import Flask, render_template, redirect
from script.main import main_script

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('number.html')


@app.route('/<name>/')
def user_view(name):
    if name.isdigit():
        return main_script(name)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
