'''*****************************************************
*    Author: Steven Alves                              *
*    Universidade: UniMindelo                          *
*    UC: WebServices                                   *
*    Git-Hub: https://github.com/xredocx215sevlanevets *
*    Last-Update: 12/01/2020                           *
*    Servidor: Python com Flask                        *
*****************************************************'''

from setupFlask import *

# Base Dados
items = []


# Classe que Representa todos um item
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


# Classe que Representa todos os items
class ItemsList(Resource):
    def get(self):
        return {'items': items}


# http://127.0.0.1:5000/estudante/steven
api.add_resource(Item, '/item/<string:nome>')
# http://127.0.0.1:5000/items
api.add_resource(ItemsList, '/items')
app.run(port=5000, debug=True)
