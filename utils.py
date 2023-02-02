import pickle
import json
import config
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class BostonDataPrice():

    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT) :
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD=RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT
 
       
    def __load_model(self): # Private Method
        # Load Model File
        with open(r"artifacts/regression_model.pkl", "rb") as f:
            self.model = pickle.load(f)
            print('self.model >>',self.model)

        # scaling model
        with open(r"artifacts/normal_scaler_model.pkl","rb") as f:
            self.scaler_model=pickle.load(f)
            print('scaler_model',self.scaler_model)

    def get_predicted_price(self):
        self.__load_model()
        test_array = np.array([self.CRIM,self.ZN,self.INDUS,self.CHAS,self.NOX,self.RM,self.AGE,self.DIS,self.RAD,self.TAX,self.PTRATIO,self.B,self.LSTAT],ndmin=2)
    
        print("Test Array is :",test_array)
        scaled_array = self.scaler_model.transform(test_array)
    
        predicted_price = self.model.predict(scaled_array)[0]
        print("Predicted Price :", predicted_price)
        return predicted_price

if __name__ == '__main__':
    pred = BostonDataPrice(0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98).get_predicted_price()
    print(pred)