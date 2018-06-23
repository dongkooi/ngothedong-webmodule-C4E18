from flask import Flask, render_template
import mlab
app = Flask(__name__)
from models.customer import Customer

mlab.connect()

@app.route('/')
def index():
    all_customer = Customer.objects(contacted = False, gender= 1)
    if len(all_customer) < 10:
        all_customer = all_customer
    else:
        for i in range(10):
            all_customer = all_customer
    return render_template('index.html', all_customer= all_customer )
    
@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template("customer.html", all_customer= all_customer)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 