from flask import Flask  
app = Flask(__name__)    
                        
print(__name__)         

#1)localhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")
@app.route('/')          
def hello_world():
    return 'Hello World!'  
#2)localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>') 
def say(name):
    #3)localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request.
    if name=="flask":
        return "Hi Flask"
    #4)localhost:5000/say/michael - have it say "Hi Michael" (have the same function say() handle this routing request)    
    elif name=="michael":
        return "Hi Michael"
    #5)localhost:5000/say/john - have it say "Hi John!" (have the same function say() handle this routing request)    
    elif name=="john":
        return "Hi John!" 

#6)localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 35.  
# To do this use int().  For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, 
# it should say "hello" 80 times.
#7)localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)
@app.route('/users/<num>/<name>') 
def repeat(num,name):
    num=int(num)
    return num*name


if __name__=="__main__":                           
    app.run(debug=True)   