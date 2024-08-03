import unittest
from unittest.mock import patch
from flask import session
from app import app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.login_url = '/login'
        self.login_data = {
            'username': os.getenv('USERNAME'),
            'password': os.getenv('PASSWORD'),
            'plant_id': os.getenv('PLANT_ID')
        }

    def login(self):
        with self.app.session_transaction() as sess:
            sess['token'] = 'mock_token'
            sess['plant_id'] = self.login_data['plant_id']

    @patch('app.get_token')
    @patch('app.requests.post')
    def test_main_page(self, mock_post, mock_get_token):
        mock_get_token.return_value = 'mock_token'
        mock_post.return_value.json.return_value = {
            "status": "0",
            "message": "success",
            "data": {
                "today_eq": "11626.0",
                "month_eq": "0",
                "year_eq": "12759028",
                "total_eq": "18948894",
                "real_power": "8951.8",
                "co2_emission_reduction": "18892047.318",
                "plant_tree": "1032",
                "data_time": "2024-08-03 10:16:22",
                "last_data_time": "2024-08-03 10:16:22",
                "capacitor": "14.8",
                "is_balance": 0,
                "is_reflux": 0,
                "reflux_station_data": None
            },
            "systemNotice": None
        }
        self.login()
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Today's Energy", response.data)

    @patch('app.get_token')
    @patch('app.requests.post')
    def test_plant_details_page(self, mock_post, mock_get_token):
        mock_get_token.return_value = 'mock_token'
        mock_post.return_value.json.return_value = {
            "status": "0",
            "message": "success",
            "data": {
                "name": "Charissa Garcia",
                "address": "35885 Saddle Palm Wy, Zephyrhills, FL 33541, USA",
                "capacitor": "14.8",
                "electricity_price": 7.92,
                "timezone": {
                    "dis_name": "(UTC-05:00) Central Daylight Time (CDT)"
                }
            }
        }
        self.login()
        response = self.app.get('/plant')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Charissa Garcia", response.data)

    @patch('app.get_token')
    @patch('app.requests.post')
    def test_device_list_page(self, mock_post, mock_get_token):
        mock_get_token.return_value = 'mock_token'
        mock_post.return_value.json.return_value = {
            "status": "0",
            "message": "success",
            "data": [{
                "children": [
                    {"id": 1, "sn": "12345", "model_no": "HM-1200N"},
                    {"id": 2, "sn": "67890", "model_no": "HM-600N"}
                ]
            }]
        }
        self.login()
        response = self.app.get('/devices')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"12345", response.data)
        self.assertIn(b"67890", response.data)

    @patch('app.get_token')
    @patch('app.requests.post')
    def test_device_details_page(self, mock_post, mock_get_token):
        mock_get_token.return_value = 'mock_token'
        mock_post.return_value.json.return_value = {
            "status": "0",
            "message": "success",
            "data": [{
                "children": [
                    {"id": 1, "sn": "12345", "model_no": "HM-1200N", "soft_ver": "V01.00.18", "hard_ver": "H00.04.00", "warn_data": {"warn": False, "connect": True}},
                    {"id": 2, "sn": "67890", "model_no": "HM-600N", "soft_ver": "V01.00.10", "hard_ver": "H00.04.10", "warn_data": {"warn": False, "connect": True}}
                ]
            }]
        }
        self.login()
        response = self.app.get('/device/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"12345", response.data)
        self.assertIn(b"HM-1200N", response.data)

        response = self.app.get('/device/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"67890", response.data)
        self.assertIn(b"HM-600N", response.data)

if __name__ == '__main__':
    unittest.main()
