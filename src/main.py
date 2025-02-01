from flask import Flask, request, jsonify
from services.budget_service import analyze_budget
from services.investment_service import suggest_investments
from api.api_connector import fetch_bank_data
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/analyze_budget', methods=['POST'])
def budget_analysis():
    data = request.json
    analysis = analyze_budget(data['transactions'], data['income'])
    return jsonify(analysis)

@app.route('/investment_advice', methods=['POST'])
def get_investment_advice():
    data = request.json
    advice = suggest_investments(data['risk_profile'])
    return jsonify(advice)

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    user_id = request.args.get('user_id')
    transactions = fetch_bank_data(user_id)
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)