import requests

API_KEY = 'dd385e640879d2a13d6f4da32b20febb'

def check_api_key(api_key):
    url = 'https://2captcha.com/res.php'
    params = {
        'key': api_key,
        'action': 'getbalance'
    }
    
    response = requests.get(url, params=params)
    return response.json()

result = check_api_key(API_KEY)
print(result)