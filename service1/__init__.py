import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    input1=requests.get('https://bunkozip.azurewebsites.net/api/Service2?code=/4RPOwpMBcwQUonuWnRPPwXujqLeAxPTxqU0C8VWfdQicPgQ43vBDg==')
    input2=requests.get("https://bunkozip.azurewebsites.net/api/Service3?code=TAiOH3JoLpB8XpGLKIwt5FKXLoed9wGwtvkiin53Uuof0bFUaJdzcA==")
    a1=input1.text
    b1=input2.text
    c = [i + j for i, j in zip(a1, b1)]
    space=""
    d=space.join(c)

    return func.HttpResponse(
            d,
            status_code=200
        )
