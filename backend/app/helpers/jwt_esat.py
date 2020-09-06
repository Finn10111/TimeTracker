'''
this is a custom module to extend flask-jwt-extended to work with ember-simple-auth-token
refresh tokens.  by default flask-jwt-extended wants the refresh tokens in the header, but
esat sends it in the payload.  This is meant to decorate the refresh route like this:
@app.route('/token-refresh', methods=['POST'])
@jwt_esat_refresh_token_required
def do_refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user),
        'refresh_token': create_refresh_token(identity=current_user)
    }
    return jsonify(ret), 200
'''

from flask import request
from functools import wraps
from flask_jwt_extended.exceptions import NoAuthorizationError, WrongTokenError
from flask_jwt_extended.config import *
from flask_jwt_extended.tokens import decode_jwt
from flask_jwt_extended.view_decorators import _load_user
#from flask_jwt_extended.blacklist import check_if_token_revoked
try:
    from flask import _app_ctx_stack as ctx_stack
except ImportError:  # pragma: no cover
    from flask import _request_ctx_stack as ctx_stack


def jwt_esat_refresh_token_required(fn):
    """
      modified decorator from jwt's jwt_refresh_token_required function
      looks for the refresh token in the payload instead of header
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_token = request.json.get('refresh_token', None)
        if not jwt_token:
            raise NoAuthorizationError("Missing refresh token")

        decoded_token = decode_jwt(
            jwt_token, config.decode_key, config.algorithm, csrf=False)

        # Make sure the type of token we received matches the request type we expect
        if decoded_token['type'] != 'refresh':
            raise WrongTokenError('Only refresh tokens can access this endpoint')

        # If blacklisting is enabled, see if this token has been revoked
        #if config.blacklist_enabled:
            #check_if_token_revoked(decoded_token)

        ctx_stack.top.jwt = decoded_token
        _load_user(decoded_token['identity'])
        return fn(*args, **kwargs)
    return wrapper
