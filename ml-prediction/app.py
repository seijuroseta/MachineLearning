from flask import Flask, make_response, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from prediction import predict
from constants import parameter_error, limit_error, main_page

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['200 per day', '50 per hour'],
    storage_uri="memory://"
)

def get_main_summary():
    return main_page

@app.route("/")
def main():
    response = make_response(main_page, 200)    
    response.mimetype = "text/plain"
    return response

def prediction_error(text):
    response = dict.fromkeys(['success', 'data'])
    response['success'] = False
    response['data'] = { "error": text }
    return jsonify(response)

@app.route("/prediction")
@limiter.limit("1/second", override_defaults=False)
def prediction():
    review = request.args.get('review')

    if review is None:
        return prediction_error(parameter_error)

    response = dict.fromkeys(['success', 'data'])
    response['success'] = True
    response['data'] = { "score": predict(review) }
    return jsonify(response)

@app.errorhandler(429)
def ratelimit_handler(_):
    return prediction_error(limit_error)
