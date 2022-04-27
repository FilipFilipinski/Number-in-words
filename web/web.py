import requests
from flask import Flask, render_template, redirect, jsonify, request
from script.main import main_script

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect('/' + request.form.get("number"))
    else:
        return render_template('formh.html')


@app.route('/<number>')
def user_view(number):
    if number.isdigit():
        return render_template('number.html', number=number, number_w=main_script(number))
    else:
        return redirect('/')


@app.route('/api/<value>')
def api(value):
    if value.isdigit():
        return jsonify({value: main_script(value)})
    else:
        return jsonify({'message': "Bad Request", 'status': 400}), 400


if __name__ == '__main__':
    app.run(debug=True)
