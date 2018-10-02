from flask import Flask, flash, session, render_template, request, redirect

app=Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

print(__name__)         

@app.route("/")
def hello_login():
  return render_template('dojo.html')
   
@app.route('/success', methods=['POST'])
def survey_Details():
  print("Got Survey Info")
  if len(request.form['name'])<1:
    flash("Please enter Name")
  else:  
    name = request.form['name']
    
  location = request.form['location']
  language = request.form['language']
  if len(request.form['message'])<1:
    flash("Please provide Comment")
  elif len(request.form['message'])>120: 
    flash("Comment can't exceed 120 characters!")
  else:
    message = request.form['message']
  
  if '_flashes' in session.keys():
    return redirect("/")
  else:
    return render_template('success.html',name=name,location=location,language=language,message=message)
  
  
@app.route('/danger')
def danger():
  print("a user tried to visit /danger.  we have redirected the user to /")
  
  return redirect('/')
  
if __name__=="__main__":
    app.run(debug=True) 