import pandas as pd 
from flask import Flask,render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, template_folder ='template')
data= pd.read_csv("D:\Tejas\Data science road map\ML_Projects\Banglore_house_prediction\server\BHP_clean_dataset")
X=pd.read_csv("D:\Tejas\Data science road map\ML_Projects\Banglore_house_prediction\server\col_names")
model = pickle.load(open("D:\\Tejas\Data science road map\ML_Projects\Banglore_house_prediction\server\\banglore_predict_model.pickle" , "rb"))



@app.route('/')
def index():
    locations = sorted(data["location"].unique())
    return render_template('index.html', locations =locations )

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location, bhk, bath, sqft)
    prediction = predict_price(location, sqft, bath, bhk)

    return str(prediction)

def predict_price(location, sqft, bath , bhk):
        loc_index = np.where(X.columns==location)[0]
    
        x= np.zeros(len(X.columns))
        x[0]= sqft
        x[1]=bath
        x[2]=bhk
        try:
            if loc_index >= 0:
                x[loc_index]=1 
        except:
            x[len(X.columns)]=1
        
        return model.predict([x])[0]

if __name__ == "__main__":
    app.run(debug=True)
