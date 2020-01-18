from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, nome):
        for item in items:
            if item['nome'] == nome:
                return item
        return {'item': None}, 404

    def post(self, nome):
        item = {'nome': nome, 'preco': 12.00}
        items.append(item)
        return item, 201


# http://127.0.0.1:5000/estudante/steven
api.add_resource(Item, '/item/<string:nome>')

app.run(port=5000)
