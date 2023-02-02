from flask import Flask,render_template,request,jsonify
import config
from utils import BostonDataPrice
import traceback


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('test.html')

@app.route('/predictprice', methods = ['GET','POST'])
def predicted_price():
    try:
        if request.method == 'POST':
            data = request.form.get

            print("User Data is :",data)
            CRIM =int(data('CRIM'))
            ZN = int(data('ZN'))
            INDUS = int(data('INDUS'))
            CHAS = int(data('CHAS'))
            NOX = int(data('NOX'))
            RM = int(data('RM'))
            AGE=int(data('AGE'))
            DIS=int(data('DIS'))
            RAD=int(data('RAD'))
            TAX=int(data('TAX'))
            PTRATIO=int(data('PTRATIO'))
            B=int(data('B'))
            LSTAT=int(data('LSTAT'))
            

            price = BostonDataPrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
            charges = price.get_predicted_price()
            return  render_template('test.html',prediction = charges)
        else:
            data = request.args.get

            print("User Data is :",data)
            CRIM =eval(data('CRIM'))
            ZN = eval(data('ZN'))
            INDUS = eval(data('INDUS'))
            CHAS = eval(data('CHAS'))
            NOX = eval(data('NOX'))
            RM = eval(data('RM'))
            AGE=eval(data('AGE'))
            DIS=eval(data('DIS'))
            RAD=eval(data('RAD'))
            TAX=eval(data('TAX'))
            PTRATIO=eval(data('PTRATIO'))
            B=eval(data('B'))
            LSTAT=eval(data('LSTAT'))
            
            price = BostonDataPrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
            charges = price.get_predicted_price()
            return  render_template('test.html',prediction = charges)

            
            
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181, debug=False)

   
        