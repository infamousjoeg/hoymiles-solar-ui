from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    token = session.get('token')
    plant_id = session.get('plant_id')
    if not token or not plant_id:
        return redirect(url_for('auth.login'))
    
    API_BASE_URL = current_app.config['API_BASE_URL']
    url = f'{API_BASE_URL}/pvm-data/data_count_station_real_data'
    payload = {
        "body": {"sid": plant_id},
        "WAITING_PROMISE": True
    }
    headers = {
        'Cookie': f'hm_token={token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        data = response.json()['data']
    except ValueError:
        print("Error: Response is not in JSON format")
        print("Response Text:", response.text)
        return "Error fetching data", 500
    except KeyError:
        print("Error: Unexpected response structure")
        print("Response JSON:", response.json())
        return "Error fetching data", 500
    
    return render_template('index.html', data=data)

@main_bp.route('/plant')
def plant_details():
    token = session.get('token')
    plant_id = session.get('plant_id')
    if not token or not plant_id:
        return redirect(url_for('auth.login'))
    
    API_BASE_URL = current_app.config['API_BASE_URL']
    url = f'{API_BASE_URL}/pvm/station_find'
    payload = {
        "body": {"id": plant_id},
        "WAITING_PROMISE": True
    }
    headers = {
        'Cookie': f'hm_token={token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        details = response.json()['data']
    except ValueError:
        print("Error: Response is not in JSON format")
        print("Response Text:", response.text)
        return "Error fetching data", 500
    except KeyError:
        print("Error: Unexpected response structure")
        print("Response JSON:", response.json())
        return "Error fetching data", 500
    
    return render_template('plant_details.html', details=details)

@main_bp.route('/devices')
def device_list():
    token = session.get('token')
    plant_id = session.get('plant_id')
    if not token or not plant_id:
        return redirect(url_for('auth.login'))
    
    API_BASE_URL = current_app.config['API_BASE_URL']
    url = f'{API_BASE_URL}/pvm/station_select_device_of_tree'
    payload = {
        "body": {"id": plant_id},
        "WAITING_PROMISE": True
    }
    headers = {
        'Cookie': f'hm_token={token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        devices = response.json()['data'][0]['children']
    except ValueError:
        print("Error: Response is not in JSON format")
        print("Response Text:", response.text)
        return "Error fetching data", 500
    except KeyError:
        print("Error: Unexpected response structure")
        print("Response JSON:", response.json())
        return "Error fetching data", 500
    
    return render_template('device_list.html', devices=devices)

@main_bp.route('/device/<int:device_id>')
def device_details(device_id):
    token = session.get('token')
    plant_id = session.get('plant_id')
    if not token or not plant_id:
        return redirect(url_for('auth.login'))
    
    API_BASE_URL = current_app.config['API_BASE_URL']
    url = f'{API_BASE_URL}/pvm/station_select_device_of_tree'
    payload = {
        "body": {"id": plant_id},
        "WAITING_PROMISE": True
    }
    headers = {
        'Cookie': f'hm_token={token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        devices = response.json()['data'][0]['children']
        device = next((device for device in devices if device["id"] == device_id), None)
    except ValueError:
        print("Error: Response is not in JSON format")
        print("Response Text:", response.text)
        return "Error fetching data", 500
    except KeyError:
        print("Error: Unexpected response structure")
        print("Response JSON:", response.json())
        return "Error fetching data", 500
    
    if device:
        return render_template('device_details.html', device=device)
    else:
        return "Device not found", 404

@main_bp.route('/toggle_dark_mode', methods=['POST'])
def toggle_dark_mode():
    if 'dark_mode' in session:
        session.pop('dark_mode')
    else:
        session['dark_mode'] = True
    return ('', 204)