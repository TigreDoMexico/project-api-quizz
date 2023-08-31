from marshmallow import Schema, fields


class AnswerSchema(Schema):
    resposta = fields.String(required=True)
    correta = fields.Boolean(required=True)

class QuizzSchema(Schema):
    pergunta = fields.String(required=True)
    assunto = fields.String()
    respostas = fields.List(fields.Nested(AnswerSchema))
