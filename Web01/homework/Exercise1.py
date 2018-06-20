from flask import Flask, render_template
app = Flask(__name__)


@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    new_height = height / 100
    bmi = weight / new_height**2
    if bmi < 16:
        status = "severely"
    elif bmi <=30:
        if bmi <= 18.5:
            status = "underweight"
        elif bmi <= 25:
            status = "normal"
        else:
            status = "overweight"
    else:
        status = "obese"
    # return "BMI = {0}, so you 're {1}".format(bmi,status)
    return render_template('bmi.html',bmi= bmi, status= status)

if __name__ == '__main__':
  app.run(debug=True)
 