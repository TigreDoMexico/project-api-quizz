FROM python:3.8
WORKDIR /app
RUN pip install flask marshmallow pymongo python-dotenv
COPY . .
EXPOSE 5000
ENV FLASK_APP=src.index.py
CMD ["flask", "run", "--host=0.0.0.0"]
