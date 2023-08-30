from flask import Flask, jsonify, request
from marshmallow import ValidationError

from src.controllers import QuizzController
from src.controllers.schemas import QuizzSchema

app = Flask(__name__)

controller = QuizzController()

@app.route('/quizzes', methods = ['GET'])
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    return jsonify(controller.ObterQuizzes(quantidade, assunto)), 200

@app.route('/quizz', methods = ['POST'])
def postQuizz():
    request_data = request.json
    schema = QuizzSchema()

    try:
        result = schema.load(request_data)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    print(result)
    return 'OK', 200

if __name__ == '__main__':
    app.run()