from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def parse_request():
    data = flask.request.data() # but data will be empty unless the request has the proper content-type header...
    if not data:
        data = request.form.keys()[0]

if __name__ == '__main__':
    app.run(debug=True)
