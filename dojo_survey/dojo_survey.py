from flask import Flask, render_template, request, redirect
app=Flask(__name__)
print(__name__)         

@app.route("/")
def hello_login():
  return render_template('dojo.html')
   
@app.route('/success', methods=['POST'])
def survey_Details():
  print("Got Survey Info")
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  message = request.form['message']
  return render_template('success.html',name=name,location=location,language=language,message=message)
  
@app.route('/danger')
def danger():
  print("a user tried to visit /danger.  we have redirected the user to /")
  
  return redirect('/')
  
if __name__=="__main__":
    app.run(debug=True) 