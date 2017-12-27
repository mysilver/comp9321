from flask import Flask, request
from flask_restful import Resource, Api


class Headers(Resource):
    def get(self):
        # Print the KEY-VALUES in the request header
        print(request.headers)

        # Find & return the header key-values
        headers = {}
        for h in request.headers.environ:
            header_key = h.replace("HTTP_", "")
            header_value = request.headers.get(header_key)
            if header_value is not None:
                headers[header_key] = header_value

        return headers, 200, {"Content-Type": "text/plain"}


app = Flask(__name__)
api = Api(app)
api.add_resource(Headers, '/')

if __name__ == '__main__':
    app.run(debug=True)
