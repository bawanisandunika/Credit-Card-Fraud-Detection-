from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # Get the form data
        amount = float(request.form['amount'])
        time = float(request.form['time'])
        
        # Dummy prediction logic (replace with your actual model prediction)
        if amount > 1000:  # Example logic
            prediction = "Fraudulent"
        else:
            prediction = "Not Fraudulent"

    # Render the HTML template with the prediction result
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
