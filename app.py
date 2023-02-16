from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = '张三'
    return '%s,你好' % name


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
