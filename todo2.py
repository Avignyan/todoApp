from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app)
ns = api.namespace('Todo get and post ')
ASSETTYPE_DAO = ns.model(name="ASSETTYPE_MODEL_NAME", model={
    "F_ASSET TYPENAME": fields.String(required=True),
    "F_VIDEOCASSETTE": fields.String(required=True)
})
@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'HelloWorld!'}

    @ns.expect('ASSETTYPE_DAO')
    def post(self):
        return {'message': 'HelloWorld!'}

if __name__ == '__main__':
    app.run(debug=True)