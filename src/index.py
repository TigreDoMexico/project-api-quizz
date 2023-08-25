from flask import Flask, jsonify, request

from src.controllers import QuizzController

app = Flask(__name__)

controller = QuizzController()

@app.route('/quizzes', methods = ['GET'])
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    return jsonify(controller.ObterQuizzes(quantidade, assunto))

@app.route('/quizzes/<index>', methods = ['GET'])
def getQuizz(index):
    print(index)
    return jsonify({'retorno': index})

if __name__ == '__main__':
    app.run()