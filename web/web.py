from flask import Flask, render_template, redirect
from script.main import main_script

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/<name>/')
def user_view(name):
    if name.isdigit():
        return render_template('number.html')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
