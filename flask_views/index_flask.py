from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello_world():
     student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
     )
     return render_template('index.html',name="komal", times=5, list=[1,2,4,3], student=student_info)


if __name__=="__main__":
    app.run(debug=True)    