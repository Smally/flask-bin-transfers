from flask import Blueprint, request, jsonify, send_from_directory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_from_directory('../static', 'index.html')


@main.route('/search_bin', methods=['GET'])
def search_bin():
    bin_location = request.args.get('bin_location')
    if not bin_location:
        return jsonify({"error": "Missing bin location parameter"}), 400

    # Dummy data for testing
    dummy_data = {
        "value": [
            {"BinLocation": "A1", "ProductCode": "P001", "Batch": "B001", "Quantity": 100},
            {"BinLocation": "A1", "ProductCode": "P002", "Batch": "B002", "Quantity": 150},
            {"BinLocation": "A1", "ProductCode": "P003", "Batch": "B003", "Quantity": 200}
        ]
    }

    # Filter data based on bin_location for a more realistic simulation
    filtered_data = {
        "value": [item for item in dummy_data["value"] if item["BinLocation"] == bin_location]
    }

    return jsonify(filtered_data)


@main.route('/create_transfer', methods=['POST'])
def create_transfer():
    data = request.json
    # Here you would add the code to interact with SAP B1 service layer
    return jsonify(status="success", data=data)
