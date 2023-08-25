from flask import Flask, jsonify, request

from src.controllers import obterQuizz

app = Flask(__name__)

@app.route('/quizzes', methods = ['GET'])
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    return jsonify(obterQuizz(quantidade, assunto))

@app.route('/quizzes/<index>', methods = ['GET'])
def getQuizz(index):
    quizzes = obterQuizz(int(quantidade) if quantidade else 10, assunto)
    retorno = [quiz.__dict__ for quiz in quizzes]

    return jsonify(retorno)

if __name__ == '__main__':
    app.run()