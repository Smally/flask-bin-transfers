import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
USE_DEMO_DATA = os.getenv('USE_DEMO_DATA', 'true').lower() == 'true'


# Access environment variables
SAP_B1_ENDPOINT = os.getenv('SAP_B1_ENDPOINT')
SAP_B1_USERNAME = os.getenv('SAP_B1_USERNAME')
SAP_B1_PASSWORD = os.getenv('SAP_B1_PASSWORD')


from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import main
    app.register_blueprint(main)
    return app
