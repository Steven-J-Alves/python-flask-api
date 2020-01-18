from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('preco',
                        type=float,
                        required=True,
                        help="Nao pode ficar em branco"
                        )

    def get(self, nome):
        for item in items:
            if item['nome'] == nome:
                return item
        return {'item': None}, 404

    def post(self, nome):

        data = Item.parser.parse_args()

        item = {'nome': nome, 'preco': data['preco']}
        items.append(item)
        return item, 201


# http://127.0.0.1:5000/estudante/steven
api.add_resource(Item, '/item/<string:nome>')

app.run(port=5000)
