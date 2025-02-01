import pytest
from src.services.budget_service import analyze_budget

@pytest.fixture
def sample_transactions():
    return [
        {'date': '2023-01-01', 'amount': 100, 'category': 'Food'},
        {'date': '2023-01-02', 'amount': -50, 'category': 'Income'},
        {'date': '2023-01-03', 'amount': 200, 'category': 'Rent'},
    ]

def test_analyze_budget(sample_transactions):
    income = 2000  # Example monthly income
    result = analyze_budget(sample_transactions, income)
    
    assert isinstance(result, dict)
    assert 'analysis' in result
    assert 'categories' in result