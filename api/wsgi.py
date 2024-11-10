from flask import Flask
from flask_restx import Api

from namespaces.user import api as user_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

api.add_namespace(user_ns)


if __name__ == '__main__':
    app.run(debug=True)