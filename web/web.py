from flask import Flask, render_template, redirect
from script.main import main_script

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/<number>/')
def user_view(number):
    if number.isdigit():
        return render_template('number.html', number=number, number_w=main_script(number))
    else:
        return redirect('/')


@app.route('/api/<value>/')
def api(value):
    if value.isdigit():
        return main_script(value)
    else:
        return "Bad Request", 400


if __name__ == '__main__':
    app.run(debug=True)
