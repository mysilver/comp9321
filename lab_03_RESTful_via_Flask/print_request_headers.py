from flask import Flask, request, jsonify
import dicttoxml

app = Flask(__name__)


@app.route("/")
def print_headers():
    # Print the KEY-VALUES in the request header
    print(request.headers)

    # Find & return the header key-values
    headers = {}
    for h in request.headers.environ:
        header_key = h.replace("HTTP_", "")
        header_value = request.headers.get(header_key)
        if header_value is not None:
            headers[header_key] = header_value

    client_accepted_response_format = headers.get('ACCEPT')
    if client_accepted_response_format == "text/xml":
        return dicttoxml.dicttoxml(headers), 200, {"Content-Type": "text/xml"}

    return jsonify(headers)


if __name__ == '__main__':
    app.run(debug=True)
