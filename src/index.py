from flask import Flask, jsonify, request

from src.controllers import obterQuizz

app = Flask(__name__)

@app.route('/quizzes')
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    quizzes = obterQuizz(int(quantidade) if quantidade else 10, assunto)
    retorno = [quiz.__dict__ for quiz in quizzes]

    return jsonify(retorno)

if __name__ == '__main__':
    app.run()