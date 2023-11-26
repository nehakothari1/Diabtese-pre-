from flask import Flask, render_template, request
import pickle 
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) #read mode

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Glucose= int(request.form["Glucose"])
        BloodPressure = int(request.form["BloodPressure"])
        SkinThickness = int(request.form["SkinThickness"])
        Insulin = int(request.form["Insulin"])
        BMI = int(request.form["BMI"])
        DiabetesPedigreeFunction = int(request.form["DiabetesPedigreeFunction"])
        Age = int(request.form["Age"])
        
        
        #get prediction
        input_cols = [[ Glucose, BloodPressure, SkinThickness, Insulin, BMI,
         DiabetesPedigreeFunction, Age]]
        prediction = model.predict(input_cols)
        output = round(prediction[0])
        return render_template("index.html", prediction_text='Diabetes Presdiction = {}'.format(output))
if __name__ == "_main_":
    app.run(debug=True)