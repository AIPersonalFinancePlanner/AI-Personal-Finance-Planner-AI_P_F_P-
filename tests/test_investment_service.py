import pytest
from src.services.investment_service import suggest_investments

@pytest.mark.parametrize("risk_profile, expected", [
    ('high', ['Cryptocurrencies', 'High-risk stocks', 'Venture capital']),
    ('medium', ['Balanced mutual funds', 'Real estate', 'Index funds']),
    ('low', ['Bonds', 'Dividend stocks', 'Fixed deposits']),
])
def test_suggest_investments(risk_profile, expected):
    result = suggest_investments(risk_profile)
    assert result['recommendations'] == expected