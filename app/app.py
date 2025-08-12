from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    env_name = os.getenv('APP_ENV', 'Unknown')
    return f"Hello from Flask App - CI/CD Automated! ({env_name} Environment)"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
