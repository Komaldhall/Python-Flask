from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
print(__name__)         

@app.route("/")
def hello_login():
  return render_template('index.html')
   
@app.route('/users', methods=['POST'])
def create_user():
  print("Got Post Info")
  session['name'] = request.form['name']
  session['email'] = request.form['email']
  # return redirect('/')
  return render_template('success.html')


if __name__=="__main__":
    app.run(debug=True) 