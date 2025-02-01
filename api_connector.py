import requests
from config import Config

def fetch_bank_data(user_id):
    api_key = Config.BANK_API_KEY
    response = requests.get(f'{Config.BANK_API_ENDPOINT}/data?user_id={user_id}', headers={'Authorization': f'Bearer {api_key}'})
    if response.status_code == 200:
        return response.json()
    return []