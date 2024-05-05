from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def list_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    items.append(data)
    return jsonify(data), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item.get('id') == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    for item in items:
        if item.get('id') == item_id:
            item.update(data)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for index, item in enumerate(items):
        if item.get('id') == item_id:
            del items[index]
            return '', 204
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
