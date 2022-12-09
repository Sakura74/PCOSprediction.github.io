from flask import Flask, render_template, redirect, request
#render_template is used to create html templates
import sklearn
import joblib




model=joblib.load("model.pkl")
# __name__==__main__
app = Flask(__name__)


#This is for GET request which is default
@app.route('/')
def hello():
  return render_template("index.html")


@app.route('/',methods=['POST'])
def marks():
  if request.method == 'POST':
    weight=int(request.form['Weight'])
    hair=int(request.form['hair'])
    skin=int(request.form['skin'])
    loss=int(request.form['loss'])
    pimples=int(request.form['pimples'])
    food=int(request.form['food'])
    exercise=int(request.form['exercise'])

    pcos=[weight,hair,skin,loss,pimples,food,exercise]

    if (model.predict([pcos])==1):
      pred="Yes"
    else:
      pred="No"



    return render_template("index.html",yourresult=pred)


   
  
  


if __name__=='__main__':
  #app.debug=True #we dont have to restart the server if we make any changes
  app.run(debug=True)