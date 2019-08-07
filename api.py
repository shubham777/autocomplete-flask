from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/questions_autocomplete')
def questions_auto():
    return render_template('questions.html')


if __name__ == '__main__':
    app.run(debug=True)
