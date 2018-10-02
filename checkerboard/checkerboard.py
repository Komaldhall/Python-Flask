from flask import Flask, render_template
app=Flask(__name__)
print(__name__)         

@app.route("/")
def hello_world():
  row=8
  column=8
  return render_template('index.html', rows=row, columns=column )
   

@app.route("/<x>/<y>")
def playmul(x,y):
  row=int(x)
  column=int(y)
  if row==column:
    return render_template('index.html', rows=row, columns=column )
  
  return "Oh... its broken, Please enter matching matrix!!"
  
if __name__=="__main__":
    app.run(debug=True)  