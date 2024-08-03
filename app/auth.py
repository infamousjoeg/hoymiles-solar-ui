from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
import hashlib
import requests

auth_bp = Blueprint('auth', __name__)

def get_token(username, password_md5):
    API_BASE_URL = current_app.config['API_BASE_URL']
    url = f'{API_BASE_URL}/iam/auth_login'
    payload = {
        "ERROR_BACK": True,
        "LOAD": {"loading": True},
        "body": {"password": password_md5, "user_name": username},
        "WAITING_PROMISE": True
    }
    response = requests.post(url, json=payload)
    
    try:
        response_data = response.json()
    except ValueError:
        print("Error: Response is not in JSON format")
        print("Response Text:", response.text)
        return None

    if 'data' in response_data and 'token' in response_data['data']:
        return response_data['data']['token']
    else:
        print("Error: Unexpected response structure")
        print("Response JSON:", response_data)
        return None

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        plant_id = request.form['plant_id']
        password_md5 = hashlib.md5(password.encode()).hexdigest()

        token = get_token(username, password_md5)
        if token:
            session.permanent = True
            session['token'] = token
            session['plant_id'] = plant_id
            return redirect(url_for('main.index'))
        else:
            return "Login Failed", 401
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
