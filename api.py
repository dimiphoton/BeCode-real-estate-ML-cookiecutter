from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict():
    # Get form data
    avg_income = request.form.get("Average Income of Area")
    avg_population = request.form.get("Average Area Population")

    # Perform prediction based on form data
    prediction = process_prediction(avg_income, avg_population)

    # Render template with prediction result
    return render_template("index.html", prediction_text=prediction)

def process_prediction(avg_income, avg_population):
    # Perform prediction logic, for example using a machine learning model
    # ...
    prediction = "Prediction result: $" + str(avg_income * avg_population)
    return prediction

if __name__ == "__main__":
    app.run(debug=True)
