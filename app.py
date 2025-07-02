from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = weight / (height * height)

    if bmi < 18.5:
        result = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        result = 'Normal weight'
    elif 25 <= bmi < 29.9:
        result = 'Overweight'
    else:
        result = 'Obesity'

    return render_template('result.html', bmi=round(bmi, 2), result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)