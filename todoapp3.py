from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Initialize Flask-RESTX
api = Api(app)
ns = api.namespace('Todo', description='Todo operations')

# Model definition
ASSETTYPE_DAO = ns.model(name="ASSETTYPE_MODEL_NAME", model={
    "F_ASSET_TYPENAME": fields.String(required=True),
    "F_VIDEOCASSETTE": fields.String(required=True)
})

# In-memory data storage (this is just a placeholder for demonstration purposes)
asset_types = {}

@ns.route('/<string:asset_id>')
class AssetTypeResource(Resource):
    def get(self, asset_id):
        if asset_id in asset_types:
            return asset_types[asset_id], 200
        return {"message": f"Asset with ID {asset_id} not found"}, 404

    @ns.expect(ASSETTYPE_DAO)
    def post(self, asset_id):
        """Create a new asset type"""
        if asset_id in asset_types:
            return {"message": f"Asset with ID {asset_id} already exists"}, 400
        data = request.json
        asset_types[asset_id] = data
        return {"message": f"Asset with ID {asset_id} created"}, 201

    @ns.expect(ASSETTYPE_DAO)
    def put(self, asset_id):
        """Update an existing asset type"""
        if asset_id not in asset_types:
            return {"message": f"Asset with ID {asset_id} not found"}, 404
        data = request.json
        asset_types[asset_id] = data
        return {"message": f"Asset with ID {asset_id} updated"}, 200

    def delete(self, asset_id):
        """Delete an asset type by ID"""
        if asset_id in asset_types:
            del asset_types[asset_id]
            return {"message": f"Asset with ID {asset_id} deleted"}, 200
        return {"message": f"Asset with ID {asset_id} not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
