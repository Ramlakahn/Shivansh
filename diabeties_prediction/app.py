import pickle
import pandas as pd
from flask import Flask, request, render_template

with open("random_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Keep the exact training column order
        input_df = pd.DataFrame([[
            float(request.form["Pregnancies"]),
            float(request.form["Glucose"]),
            float(request.form["BloodPressure"]),
            float(request.form["SkinThickness"]),
            float(request.form["Insulin"]),
            float(request.form["BMI"]),
            float(request.form["DiabetesPedigreeFunction"]),
            float(request.form["Age"])
        ]], columns=[
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
        ])

        # Predict
        prediction = model.predict(input_df)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        return render_template("result.html", result=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)

