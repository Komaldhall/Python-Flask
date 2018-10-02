from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
print(__name__)         

@app.route("/")
def hello_login():
  session['num']=random.randrange(0, 101)
  if not 'msg' in session:
    session['msg']=""
  return render_template("index.html")  

@app.route("/again")
def login():
  session['num']=random.randrange(0,2)
  session['msg']=""
  return render_template("index.html") 

@app.route("/count", methods=['POST'])
def count():
  if int(request.form['number'])>int(session['num']):
    session['msg']="TOO HIGH"
    

  elif int(request.form['number'])<int(session['num']):
    session['msg']="TOO LOW"


  elif int(request.form['number'])==int(session['num']): 
    session['msg']="Great!! YOU WON" 
    
  return redirect('/')
  

if __name__=="__main__":
    app.run(debug=True) 