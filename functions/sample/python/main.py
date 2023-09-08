"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests


def main():
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        authenticator = IAMAuthenticator(
            'apikey')
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(
            "url")
        response = service.post_all_docs(
            db='reviews',
            include_docs=True,
        ).get_result()

        print(f"Databases: {response}")
    except ApiException as ae:
        print("unable to connect")
        return {"error": ae.message}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"body": response}


