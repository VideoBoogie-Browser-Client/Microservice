from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/upload')
def upload_video():
    return render_template('upload_video.html')


if __name__ == '__main__':
    app.run(debug=True)