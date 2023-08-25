import json
from flask import Flask, Response, request

from controllers.quizzController import obterQuizz

app = Flask(__name__)

@app.route('/quizzes')
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    returno = obterQuizz(int(quantidade) if quantidade else 10, assunto)

    return Response(json.dumps({'quizzes': returno}),  mimetype='application/json')

if __name__ == '__main__':
    app.run()