FROM amazon/dynamodb-local:latest

COPY script.json /home/dynamodblocal/data/

CMD ["-jar", "DynamoDBLocal.jar", "-sharedDb", "-dbPath", "/home/dynamodblocal/data"]
