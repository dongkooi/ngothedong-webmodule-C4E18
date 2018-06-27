from flask import *
import mlab
app = Flask(__name__)
from models.service import Service
#1. Create connection
mlab.connect()

# new_service = Service(
#     name="H",
#     yob= "1995",
#     gender= 1,
#     height= 158,
#     phone= "0123456789",
#     address= "TB",
#     status= True
# )
# new_service.save()
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender)
    return render_template("search.html", all_service= all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service= all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    person = Service.objects().with_id(service_id)
    if person is not None:
        person.delete()
        return redirect(url_for('admin'))
    else:
        return "ERR"

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


if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 