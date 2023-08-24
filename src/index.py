from flask import Flask, jsonify

from controllers.quizzController import obterQuizz

app = Flask(__name__)

@app.route('/quizzes')
def getQuizz():
    returno = obterQuizz()
    return jsonify(returno.__dict__)

if __name__ == '__main__':
    app.run()