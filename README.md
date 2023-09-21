# QuizzApi
API para gerar quizzes randômicos de vários assuntos

## Dependências
`pip install flask marshmallow pymongo python-dotenv`

## Docker
Criar imagem
`docker build -t quizz-api .`

Criar Docker Compose
`docker-compose up -d`

## Rodar
`python -m src.index`

## Testar
`python -m unittest discover -s test`