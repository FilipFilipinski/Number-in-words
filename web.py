from flask import Flask

app = Flask(__name__)


@app.route('/<value>')
def render_result(value: str):
    return f'{value}'


@app.route('/')
def render_form(value: str):
    return f'{value}'


if __name__ == '__main__':
    app.run(debug=True)
