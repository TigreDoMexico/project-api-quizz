from flask import Flask, jsonify, request

from controllers.quizzController import obterQuizz

app = Flask(__name__)

@app.route('/quizzes')
def getQuizz():
    quantidade = request.args.get('quantidade')
    assunto = request.args.get('assunto')

    returno = obterQuizz(int(quantidade) if quantidade else 10, assunto)
    return jsonify(returno.__dict__)

if __name__ == '__main__':
    app.run()