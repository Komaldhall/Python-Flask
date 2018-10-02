from flask import Flask, render_template, request, redirect
import datetime
app=Flask(__name__)
print(__name__)         

@app.route("/")
def hello_login():
  return render_template('fruit.html')
   
@app.route('/success', methods=['POST'])
def survey_Details():
  print("Got Order Info")
  strawbeery = request.form['strawbeery']
  rasbeery = request.form['rasbeery']
  apple = request.form['apple']
  name = request.form['name']
  idd = request.form['idd']
  items=int(strawbeery)+int(rasbeery)+int(apple)
  now = datetime.datetime.now()
  now=now.strftime("%Y-%m-%d %H:%M:%S")

  return render_template('success.html',strawbeery=strawbeery,rasbeery=rasbeery,apple=apple,idd=idd,name=name,items=items,day=now)
  
# @app.route('/danger')
# def danger():
#   print("a user tried to visit /danger.  we have redirected the user to /")
  
#   return redirect('/')
  
if __name__=="__main__":
    app.run(debug=True) 