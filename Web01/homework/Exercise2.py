from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
	        "quy": 
            {
			"name" : "Dinh Cong Quy",
			"age" : 20
            },
            "tuananh": 
            {
			"name" : "Huynh Tuan Anh",
			"age" : 22
            }
        }   

    return render_template('user.html', users= users, username= username)

if __name__ == '__main__':
  app.run(debug=True)
 