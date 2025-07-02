from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ocr():
    return jsonify({"message": "Hello from OCR"})

def handler(environ, start_response):
    from werkzeug.wrappers import Request, Response
    request = Request(environ)
    response = app.full_dispatch_request()
    return response(environ, start_response)
