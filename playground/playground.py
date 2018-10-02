from flask import Flask, render_template
app=Flask(__name__)
print(__name__)         

@app.route("/")
def hello_world():
  return "Hello World"
   
@app.route("/play")
def play():
  times=3
  return render_template('index.html',num=times)  

@app.route("/play/<num>")
def playmul(num):
  num=int(num)
  return render_template('index.html',num=num)

@app.route("/play/<num>/<color>")
def playcolor(num,color):
  num=int(num)
  color=color
  return render_template('index.html',num=num,color=color)

if __name__=="__main__":
    app.run(debug=True)  