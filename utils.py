import pickle
import json
import config
import numpy as np
import pymongo
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
            #print('self.model >>',self.model)

        # scaling model
        with open(r"artifacts/normal_scaler_model.pkl","rb") as f:
            self.scaler_model=pickle.load(f)
            #print('scaler_model',self.scaler_model)

    def get_predicted_price(self):
        self.__load_model()
        test_array = np.array([self.CRIM,self.ZN,self.INDUS,self.CHAS,self.NOX,self.RM,self.AGE,self.DIS,self.RAD,self.TAX,self.PTRATIO,self.B,self.LSTAT],ndmin=2)
    
        #print("Test Array is :",test_array)
        scaled_array = self.scaler_model.transform(test_array)
    
        predicted_price = self.model.predict(scaled_array)[0]
        #print("Predicted Price :", predicted_price)
        self.predicted_price=predicted_price
        return self.predicted_price

    def database_fun(self):
        self.get_predicted_price()
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
        # database_name = 'boston_db'
        self.db = self.mongo_client['boston_db']
        self.collection_user = self.db['user_input']
        # self. __database_init()
        self.query ={
        "CRIM"  :self.CRIM,
        
        "ZN"    :self.ZN,
        "INDUS" :self.INDUS, 
        "CHAS"  :self.CHAS,  
        "NOX"   :self.NOX,  
        "RM"    :self.RM, 
        "AGE"   :self.AGE,
        "DIS"   :self.DIS,
        "RAD"   :self.RAD,
        "TAX"   :self.TAX,
        "PTRATIO":self.PTRATIO,
        "B"      :self.B,
        "LSTAT"  :self.LSTAT,
        "predicted price":self.predicted_price
        }

        self.data=self.collection_user.insert_one(self.query)
        return self.data
        


if __name__ == '__main__':
    #pred = BostonDataPrice(0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98).get_predicted_price()
    cls = BostonDataPrice(0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98)
    pred=cls.get_predicted_price()
    users_inputs=cls.database_fun()
    print(pred)
    print(users_inputs)