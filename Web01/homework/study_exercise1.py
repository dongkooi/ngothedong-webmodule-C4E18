from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    return render_template('about-me.html')

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)
