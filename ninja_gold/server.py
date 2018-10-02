from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
print(__name__)         

@app.route("/")
def hello_ninja():
  if not 'gold' in session:
    session['gold']=0
  if not 'activities' in session:
    session['activities']=[]
  return render_template("index.html")  

@app.route("/process_money",methods=['POST'])
def process():
  if request.form['building']=='farm':
    num=random.randrange(10,21)
    session['gold']+=num
  elif request.form['building']=='cave':
    num=random.randrange(5,11)
    session['gold']+=num
  elif request.form['building']=='house':
    num=random.randrange(2,6)
    session['gold']+=num
  elif request.form['building']=='casino':
    num=random.randrange(-50,51)
    # session['earn_take']=random.randrange(0,2)
    # if session['earn_take']==0:
    #   session['gold']+=num
    # else:
    #   session['gold']-=num  
    session['gold']+=num
  if session['gold']<0:
    session['gold']=0
  if num>0:
    num_dict={ 
      'message':"Earned {} golds from the {}.".format(num,request.form['building']),
      'type':'success'
    }
    session['activities'].append(num_dict)
  elif num<0:
    num_dict={ 
      'message':"lost {} golds from the {}.".format(-num,request.form['building']),
      'type':'failure'
    }
    session['activities'].append(num_dict)

  # if num>=0:
  #   session['activities']+="Earned {} golds from the {}.".format(num,request.form['building'])
  # else:
  #   session['activities']+="lost {} golds from the {}.".format(-num,request.form['building'])
  return redirect("/")

@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')


  

if __name__=="__main__":
    app.run(debug=True) 