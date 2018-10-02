from flask import Flask, render_template
app=Flask(__name__)
print(__name__)         

@app.route("/")
def hello_world():
  users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
  )
  student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    )
  return render_template('index.html', users_info=users, students=student_info)
     
if __name__=="__main__":
    app.run(debug=True)  