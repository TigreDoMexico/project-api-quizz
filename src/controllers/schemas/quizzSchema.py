from marshmallow import Schema, fields

class QuizzSchema(Schema):
    pergunta = fields.String(required=True)
    assunto = fields.String(required=True)
