from flask import Flask, jsonify
from error_handler import *
from resources import resources

app = Flask(__name__)
app.register_blueprint(resources.companyBP)
app.register_blueprint(resources.companyFavouritesBP)



@app.route('/')
def hello_world():
    return 'Hello World from API!'


if __name__ == '__main__':
    app.run(Debug=False)


# def RegisterErrorHandlers(app):
#     @app.errorhandler(Exception)
#     def handle_exception_error(e):
#         return jsonify({'msg': 'Internal Server Error'}), 500
#
#     @app.errorhandler(405)
#     def handle_405_error(e):
#         return jsonify({'msg': 'Method not allowed'}), 405
#
#     @app.errorhandler(403)
#     def handle_403_error(e):
#         return jsonify({'msg': 'Forbidden error'}), 403
#
#     @app.errorhandler(404)
#     def handle_403_error(e):
#         return jsonify({'msg': 'Not Found error'}), 404
#
#     @app.errorhandler(ObjectNotFound)
#     def handle_object_not_found_error(e):
#         print("Error: ", e)
#         return jsonify({'msg': str(e)}), 404
#
#     @app.errorhandler(RequestBodyEmpty)
#     def handle_request_body_empty_error(e):
#         return jsonify({'msg': str(e)}), 400
#
#     @app.errorhandler(ObjectAlreadyExists)
#     def handle_request_object_already_exists_error(e):
#         return jsonify({'msg': str(e)}), 400
#
#
# RegisterErrorHandlers(app)
