def safe_jsonify(data):
    # Custom jsonify with error handling
    try:
        return jsonify(data)
    except TypeError:
        return jsonify({"error": "Invalid data type"}), 400