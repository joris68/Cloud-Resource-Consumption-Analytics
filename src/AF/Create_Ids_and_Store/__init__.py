import logging
import traceback
from common_MS_API import get_secret_client, create_query_on_server_return_id, create_report_on_server_return_id
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    try:

        # get the vault_url to retrive a new 
        vault_url = os.environ['vault_url']
        secret_client = get_secret_client(vault_url)


        # create query ID and store it into the key Vault

        query_id = create_query_on_server_return_id(secret_client)
        secret_client.set_secret('queryID', query_id)
        logging.info("QueryID was stored in Key Vault")


        # create report ID and store it into the key Vault

        report_id = create_report_on_server_return_id(query_id, secret_client)
        secret_client.set_secret('reportID', report_id)
        logging.info("ReportID was stored in Key Vault")

        func.HttpResponse("Creating the Query ID and the Report ID  was successful and now stored in Key Vault", status_code=200)


    except Exception as e:

        error_traceback = traceback.format_exc()

        return func.HttpResponse( str(e) + " --------" + error_traceback ,status_code=400)


