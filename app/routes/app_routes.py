from flask import Flask, jsonify, request
from flask import current_app as app

@app.route("/", methods=['GET', 'POST'])
def root():
    data = {}
    data['method'] = request.method
    data['data'] = 'Hello World!'
    app.logger.info(f"Response: ${data}")
    return jsonify(data)