from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Function to log user sign-ins
def log_sign_in(username):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign_in_data = pd.DataFrame({'Username': [username], 'Sign-in Time': [current_time]})
    
    try:
        log_df = pd.read_excel('user_sign_ins.xlsx')
    except FileNotFoundError:
        log_df = pd.DataFrame(columns=['Username', 'Sign-in Time'])

    log_df = log_df.append(sign_in_data, ignore_index=True)
    log_df.to_excel('user_sign_ins.xlsx', index=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle the user login form submission
    username = request.form['username']
    password = request.form['password']

    # Add your authentication logic here, and if successful, log the sign-in:
    if username == 'valid_user' and password == 'valid_password':
        log_sign_in(username)
        return redirect(url_for('home'))
    else:
        return "Login failed. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
