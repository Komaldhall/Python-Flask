from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
print(__name__)         

@app.route("/")
def hello_login():
  if not 'count' in session:
    session['count']=1
   
  return render_template("index.html")  


@app.route("/count", methods=['POST'])
def count():
  if request.form['number']=='2':
    session['count']+=2
  elif request.form['number']=='0':
    session['count']=1
  
  return redirect('/')

@app.route("/destroy_session")
def destroy():
  session.clear()
  return redirect('/')  


if __name__=="__main__":
    app.run(debug=True) 