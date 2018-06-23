from flask import Flask, render_template
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
    all_service = Service.objects(gender = gender, yob__lte=1998, address__exact="Hà Nội")
    return render_template("search.html", all_service= all_service)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 