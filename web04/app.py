from flask import *
import mlab
from youtube_dl import YoutubeDL
from models.video import Video

app = Flask(__name__)
app.secret_key = "..."
mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
   return render_template("detail.html", youtube_id= youtube_id)

@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("admin"))
        else:
            return "Login Fail"

@app.route('/logout')
def logout():
   del session['logged']
   return redirect(url_for("index"))

@app.route("/admin", methods =["GET", "POST"])
def admin():
    if "loggedin" in session:
        if request.method == "GET":
            videos = Video.objects()
            return render_template("admin.html", videos = videos)
        elif request.method == "POST":
            form = request.form
            link = form["link"]
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)
            title = data["title"]
            thumbnail = data["thumbnail"]
            views = data["view_count"]
            youtube_id = data["id"]

            new_video = Video(
                title = title,    
                thumbnail = thumbnail,
                views = views,
                link = link,
                youtube_id = youtube_id
            )
            new_video.save()

            return redirect(url_for("admin"))
    else:
        return "Yêu cầu đăng nhập"

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)