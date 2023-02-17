from flask import Flask, render_template

# 显式声明 static 文件夹和 templates 文件夹在哪
app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/hello')
def hello():
    name = '张三'
    return '%s,你好' % name


@app.route('/')
def index():
    return render_template('index-1.html')


if __name__ == '__main__':
    app.run()
