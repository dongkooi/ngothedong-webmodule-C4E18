from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') #Trang con
def index():
    posts = [
        {
        "title": "DSK",
        "content": "Lớn rồi",
        "author": "Đông",
        "gender":1
        },
        {
        "title": "Bích Phương",
        "content": "Bùa yêu",
        "gender":0,
        "author": "..."
        },
        {
        "title": "M-TP",
        "content": "Chạy ngay đi",
        "author": "M-tp",
        "gender":1
        }
    ]
    return render_template("index.html", post= posts)

@app.route("/hello")
def say_hello():
    return "hello c4e18"

@app.route("/hi/<name>/<age>")
def say_hi(name, age):
    return "hi {0}, you're {1} years old".format(name, age)

@app.route("/sum/<int:so_x>/<int:so_y>")
def sum_xy(so_x, so_y):
    return "tổng 2 số là {}".format(so_x + so_y)
if __name__ == '__main__': #file chạy trực tiếp
  app.run(debug=True) #debug = true : sever cập nhật...
 