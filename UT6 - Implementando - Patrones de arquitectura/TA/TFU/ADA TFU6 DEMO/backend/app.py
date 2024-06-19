from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    if request.headers.get('X-Kong-Proxy-ID'):
        return 'Hello from Kong!'
    elif request.headers.get('X-Forwarded-For'):
        return 'Hello from Nginx Reverse Proxy!'
    else:
        return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)