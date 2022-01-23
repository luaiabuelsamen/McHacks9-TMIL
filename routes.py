from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function


@app.route('/')
def base():
    return render_template('base.html', the_title='risko homepage')


if __name__ == '__main__':
    app.run(debug=True)
