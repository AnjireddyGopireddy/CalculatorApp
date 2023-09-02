from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        #time = float(request.form['time'])  # You may not need this line since you're calculating time_difference
        from_date_str = request.form['from_date']
        to_date_str = request.form['to_date']
        
        from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
        to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

        time_difference = (to_date - from_date).days
        #time_years = time_difference / 365 # Convert days to years
        
        Principal_Amount = principal
        
        Rate_interest=rate
        
        interest = (principal * rate * time_difference) / 100 *1/30.4166666 # Convert days to years
        
        total_amount = principal + interest

        return render_template('index.html', interest=interest, time_difference=time_difference, total_amount=total_amount,Principal_Amount=principal,Rate_interest=rate)
    except (ValueError, KeyError):
        error_message = "Invalid input"
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)