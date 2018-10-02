from flask import Flask, flash, session, render_template, request, redirect
import re
import datetime
app=Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z]).*\d')
print(__name__)         

@app.route("/")
def hello_login():
  return render_template('register.html')
   
@app.route('/success', methods=['POST'])
def survey_Details():
  now = datetime.datetime.today().strftime("%m/%d/%Y")
  
  print(now)
  #first_name
  if len(request.form['fname'])<1:
    flash("Please enter First Name")
  elif not request.form['fname'].isalpha():
    flash("Please enter non-alpha character")
  else:
    session['fname']=request.form['fname']

  #last_name
  if len(request.form['lname'])<1:
    flash("Please enter Last Name")
  elif not request.form['lname'].isalpha():
    flash("Please enter non-alpha character")
  else:
    session['lname']=request.form['lname']
  
  #email  
  if len(request.form['email'])<1:
    flash("Please enter Email")
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid Email Address!")
  else:
    session['email']=request.form['email']

  #birthday
  if len(request.form['bday'])<1:
    flash("Please provide Birth info")
  elif request.form['bday']>now:
    flash("Your birthday refers to a future date. Please check!!")
  else:
    session['bday']=request.form['bday'] 

 
  #password
  if len(request.form['pwd'])<1:
    flash("Please provide Password")
  elif len(request.form['pwd'])<8:
    flash("Password should be atleast 8 charaters!")
  elif not PASSWORD_REGEX.match(request.form['pwd']):
    flash("Password should have atleast 1 uppercase letter and 1 numeric value!")


  #confirm_password
  if len(request.form['cpwd'])<1:
    flash("Please Confirm Password") 
  elif request.form['pwd']!=(request.form['cpwd']):
    flash("Password mismatch. Please check!!")  
   

  return render_template("register.html")
  if '_flashes' in session.keys():
    return redirect("/")
  else:
    return redirect('/done')

@app.route('/done')  
def success():
  session['done']="Thanks for submitting your information."
  return redirect("/")

  
  

  
if __name__=="__main__":
    app.run(debug=True) 