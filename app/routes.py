from flask import Blueprint, request, jsonify, send_from_directory
import requests
import os
import app

from sap_session import SAPSessionManager
sap_manager = SAPSessionManager()

main = Blueprint('main', __name__)

from dotenv import load_dotenv
load_dotenv() 

@main.route('/')
def index():
    return send_from_directory('../static', 'index.html')


@main.route('/search_bin', methods=['GET'])
def search_bin():
    bin_location = request.args.get('bin_location')
    if not bin_location:
        return jsonify({"error": "Missing bin location parameter"}), 400

    if os.getenv('USE_DEMO_DATA') == "true":
        # Return demo data
        dummy_data = {
            "value": [
                {"BinLocation": "A1", "ProductCode": "P001", "Batch": "B001", "Quantity": 100},
                {"BinLocation": "A1", "ProductCode": "P002", "Batch": "B002", "Quantity": 150},
                {"BinLocation": "A1", "ProdufctCode": "P003", "Batch": "B003", "Quantity": 200}
            ]
        }
        return jsonify(dummy_data)
    else:
        response = sap_manager.request('GET', f"InventoryLocations?$filter=BinLocation eq '{bin_location}'")
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch data from SAP"}), response.status_code



@main.route('/create_transfer', methods=['POST'])
def create_transfer():
    data = request.json
    response = sap_manager.request('POST', 'StockTransfers', json=data)
    if response.status_code == 201:
        return jsonify({"message": "Stock transfer created successfully"})
    else:
        return jsonify({"error": "Failed to create stock transfer"}), response.status_code