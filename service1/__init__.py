import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint="removed for github""
key="removed for github"

client = CosmosClient(endpoint, key)

database= client.create_database_if_not_exists(id="users")
comtainer_name= "userid"
container= database.create_container_if_not_exists(
    id="userid",
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    input1=requests.get('https://bunkozip.azurewebsites.net/api/Service2?code=/4RPOwpMBcwQUonuWnRPPwXujqLeAxPTxqU0C8VWfdQicPgQ43vBDg==')
    input2=requests.get("https://bunkozip.azurewebsites.net/api/Service3?code=TAiOH3JoLpB8XpGLKIwt5FKXLoed9wGwtvkiin53Uuof0bFUaJdzcA==")
    a1=input1.text
    b1=input2.text
    c = [i + j for i, j in zip(a1, b1)]
    space=""
    d=space.join(c)

    container.create_item(body={"username": d, "id":"1"})

    return func.HttpResponse(
            d,
            status_code=200
        )
