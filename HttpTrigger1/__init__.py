import logging

import azure.functions as func
from .cnki2bib import getBibFileContentString

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('cnki')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('cnki')

    if name:
        bib = getBibFileContentString(name)
        logging.info(bib)
        return func.HttpResponse(bib)
    else:
        return func.HttpResponse(
             "No cnki field found. Pass a cnki in the query string or in the request body for a personalized response.",
             status_code=200
        )
