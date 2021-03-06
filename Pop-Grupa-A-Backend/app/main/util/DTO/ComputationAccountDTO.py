from flask_restplus import Namespace, fields


class ComputationAccountDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'role': fields.String(required=True, description='user role'),
        'id': fields.Integer(description='user Identifier')
    })

    user_register= api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'email': fields.String(required=True, description='user email'),
        'role': fields.String(required=True, description='user role'),
    })

    user_login= api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })
