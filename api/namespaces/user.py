from flask_restx import Namespace, Resource, fields
import dao.userDao as userDao

dao = userDao.UserDAO()

api = Namespace('users', description='User related operations')

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='The user email address'),
    'password': fields.String(required=True, description='The user password'),
})


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        """List all users"""
        return dao.get_all()
