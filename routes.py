from flask import Flask, render_template, request
from markupsafe import string
#from NLP_Twitter import getRating
app = Flask(__name__)


def getRating(s):
    return 5
# two decorators, same function


@app.route('/')
def welcome():
    return render_template('results.html')


@app.route('/display', methods=['POST', 'GET'])
def result():
    coin = request.form.get("coin")
    score = getRating(coin)
    return render_template('results.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
