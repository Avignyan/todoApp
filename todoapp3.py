from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app)
ns = api.namespace('Todo', description='Todo operations')

model1 = ns.model(name="ASSETTYPE_MODEL_NAME", model={
    "Name": fields.String(required=True),
    "ID": fields.String(required=True)
})

asset_types = {}

@ns.route('/<string:ID>')
class AssetTypeResource(Resource):
    def get(self, ID):
        if ID in asset_types:
            return asset_types[ID],200
        return {"message": f"Asset with ID {ID} not found"}, 404

    @ns.expect(model1)
    def post(self, ID):
        if ID in asset_types:
            return {"message": f"Asset with ID {ID} already exists"}, 400
        data = request.json
        asset_types[ID] = data
        return {"message": f"Asset with ID {ID} created"}, 201

    @ns.expect(model1)
    def put(self, ID):
        if ID not in asset_types:
            return {"message": f"Asset with ID {ID} not found"}, 404
        data = request.json
        asset_types[ID] = data
        return {"message": f"Asset with ID {ID} updated"}, 200

    def delete(self, ID):
        if ID in asset_types:
            del asset_types[ID]
            return {"message": f"Asset with ID {ID} deleted"}, 200
        return {"message": f"Asset with ID {ID} not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)
