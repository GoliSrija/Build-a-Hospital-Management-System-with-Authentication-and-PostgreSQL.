```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from blueprints import bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(bp)

app.route_ruledecorators = {}

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello, World!"})

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found", "status_code": 404}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal Server Error", "status_code": 500}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e), "status_code": 500}), 500

if __name__ == '__main__':
    app.run()
```