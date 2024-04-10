from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_request():
    print("Headers:")
    print(request.headers)
    print("Body:")
    print(request.data.decode("utf-8"))

    return '{"quantity":2,"id":{"0":123,"1":234},"url":{"0":"http://94.103.92.242:8090/","1":"http://94.103.92.242:8090/"},"parameters":{"0":{"0":"negr.com","1":"negr2.com"},"1":{"0":"negr.com","1":"negr2.com"}},"headers":{"0":{"0":"negr.com","1":"negr2.com"},"1":{"0":"negr.com","1":"negr2.com"}},"body":{"0":"aaaaaaaaa","1":"bbbbbbbbb"}}'

@app.route("/ret", methods=["GET", "POST"])
def handle_request1():
    print("Headers:")
    print(request.headers)
    print("Body:")
    print(request.data.decode("utf-8"))

    return 'OK'

@app.route("/au", methods=["GET", "POST"])
def handle_request2():
    print("Headers:")
    print(request.headers)
    print("Body:")
    print(request.data.decode("utf-8"))

    return 'token-aaa'

@app.route("/ul", methods=["GET", "POST"])
def handle_request2():
    print("Headers:")
    print(request.headers)
    print("Body:")
    print(request.data.decode("utf-8"))

    return '["u1","u2","u3"]'


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8090)
