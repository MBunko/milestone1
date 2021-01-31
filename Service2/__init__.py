import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    l1='1234567890'
    a=""
    for i in range (0,5):
        b=random.choice(l1)
        a+=b
    return func.HttpResponse(
             a,
             status_code=200
        )
