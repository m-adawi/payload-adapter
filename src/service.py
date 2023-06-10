import requests
from flask import Flask, request
import logging
from waitress import serve
from adapter import PayloadAdapter


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to PayloadAdapter"


@app.route('/json/<mapping>', methods=['POST'])
def json_source(mapping):
    try:
        payload = request.get_json(force=True)
        adapter = PayloadAdapter(mapping)
        result = adapter.convert_payload(payload)
        dest = result["dest"] or request.args.get("dest")
        output = result["output"]
        headers = result["output_headers"]
        if dest is None:
            return output
        response = requests.post(url=dest, headers=headers, json=output)
        return response.text
    except FileNotFoundError as error:
        logging.error(error)
        return str(error), 404
    except Exception as error:
        logging.error(error)
        return repr(error), 500


@app.route("/health")
def health():
    return "OK\n"


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
