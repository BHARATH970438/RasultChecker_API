from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/report/<float:marks>')
def report(marks):
    if marks >= 35 :
        return render_template('pass.html',result = marks)
    else:
        return render_template('fail.html',result = marks)

@app.route('/submit',methods=['POST'])
def result():
    if request.method == 'POST':
        maths = float(request.form['maths'])
        physics = float(request.form['physics'])
        chemistry = float(request.form['chemistry'])
        biology = float(request.form['biology'])
        english = float(request.form['english'])
        average = (maths + physics + chemistry + biology + english)/5
        return redirect(url_for('report',marks = average))


if __name__ == "__main__":
    app.run(debug=True)