import pytest
from unittest.mock import patch
from src.api.api_connector import fetch_bank_data
from src.config import Config

@pytest.fixture
def mock_config():
    with patch('src.config.Config') as MockConfig:
        MockConfig.BANK_API_KEY = 'test_key'
        MockConfig.BANK_API_ENDPOINT = 'test_endpoint'
        yield MockConfig

@patch('requests.get')
def test_fetch_bank_data_success(mock_get, mock_config):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "transaction_data"}
    
    result = fetch_bank_data('test_user_id')
    
    mock_get.assert_called_once_with('test_endpoint/data?user_id=test_user_id', headers={'Authorization': 'Bearer test_key'})
    assert result == {"data": "transaction_data"}

@patch('requests.get')
def test_fetch_bank_data_failure(mock_get, mock_config):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    
    result = fetch_bank_data('test_user_id')
    
    mock_get.assert_called_once_with('test_endpoint/data?user_id=test_user_id', headers={'Authorization': 'Bearer test_key'})
    assert result == []