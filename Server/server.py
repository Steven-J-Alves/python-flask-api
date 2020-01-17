from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

#


class Estudante(Resource):
    def get(self, nome):
        return {'estudante': nome}


# http://127.0.0.1:5000/estudante/steven
api.add_resource(Estudante, '/estudante/<string:nome>')

app.run(port=5000)
