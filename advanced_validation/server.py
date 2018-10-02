from flask import Flask, render_template, redirect, flash, request, session
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
  if len(request.form['email'])<1:
    flash("email cannot be empty!")
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid Email Address!")
  else:  
    flash("Success!")
  return redirect('/')

if __name__=="__main__":
    app.run(debug=True)