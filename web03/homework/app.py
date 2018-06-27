from flask import *
import mlab
app = Flask(__name__)
from models.service import Service
#1. Create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service= all_service)

@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template("search.html", all_service= all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects().with_id(service_id)
    return render_template('detail.html', service = service)


@app.route('/new-service', methods= ["GET", "POST"])
def create():
    if request.method == "GET":
       return render_template('new_service.html')
    elif request.method == "POST":
       form = request.form
       name = form['name']
       yob = form['yob']
       address = form['address']

       new_service = Service(
            name = name,
            yob = yob,
            address = address,
       )
       new_service.save()
       return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ["GET", "POST"])
def update(service_id):
    service = Service.objects().with_id(service_id)
    if request.method == "GET":
        return render_template('update_service.html', service = service)
    else:
        form = request.form
        service.update(
            set__name = form['name'],
            set__yob = form['yob'],
            set__address = form['address'],
            set__gender = form['gender']
        )
        service.reload()
        return redirect(url_for('admin'))


@app.route('/delete/<service_id>')
def delete(service_id):
    person = Service.objects().with_id(service_id)
    if person is not None:
        person.delete()
        return redirect(url_for('admin'))
    else:
        return "ERR"

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 