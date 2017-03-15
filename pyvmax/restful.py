import json
import logging
import requests
from requests.auth import HTTPBasicAuth

# Disable warnings from untrusted server certificates
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except Exception:
    print("Ignore messages related to insecure SSL certificates")


class Restful:
    """Restful class implements network calls to communicate with REST API server
    Attributes:
        log (:obj:`logging`): logger object
    Args:
        base_url (str):  the ip and port # of api server
        username (str):  credentialed user of unisphere
        password (str):  the user's password
        verify_ssl (bool, optional):  verify SSL security cert or not
    """
    def __init__(self, base_url, username, password, verify_ssl=False):
        self.url = base_url
        self.auth = HTTPBasicAuth(username, password)
        self.verify_ssl = verify_ssl
        self.log = logging.getLogger("pyvmax")
        self.log.debug("Setting up Restful")

    def set_url(self, new_url):
        self.url = new_url

    def json_to_str(self, json_obj):
        """Converts json to string

        Args:
            json_obj(any type convertable to string): esp dict, list string, requests response object
        Returns:
            str
        """
        return str(json.dumps(json_obj, sort_keys=False, indent=2))

    def __request_helper(self, target_url, method="GET", params=None, data=None):
        try:
            request = requests.request(
                method,
                target_url,
                headers={"content-type": "application/json", "accept": "application/json"},
                auth=self.auth,
                verify=self.verify_ssl,
                params=params,
                data=json.dumps(data)
            )
        except requests.exceptions.RequestException:
            self.log.critical("Can't {} to API server URL: {}".format(method, target_url))
            self.log.critical("Exiting {}".format(method))
            exit(1)
        try:
            response = request.json()
        except Exception:
            self.log.warning("API {} did not return JSON response".format(method))
            self.log.warning(response.text)
            response = dict()

        # This is a VMAX API peculiarity, that "message" in the JSON means
        # the server is having issues, and the response can't be well made
        if "message" in response:
            self.log.warning("API call {}: server only responded with:".format(target_url))
            self.log.warning(request.json())
            response = dict()
        return response

    def get(self, target_url, payload=None):
        """Make the REST GET call to the public api

        Args:
            target_url(str): the full REST API URL
            payload(dict, optional): dict representing the json request payload
        Returns:
            dict:  could be empty
        """
        return self.__request_helper(target_url, method="GET", params=payload)

    def post(self, target_url, request_object=None):
        """Make the REST POST call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict:  could be empty
        """
        return self.__request_helper(target_url, method="POST", params=request_object)

    def put(self, target_url, request_object=None):
        """Make the REST PUT call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict:  could be empty
        """
        return self.__request_helper(target_url, method="PUT", params=request_object)

    def delete(self, target_url, request_object=None):
        """Make the REST DELETE call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict:  could be empty
        """
        return self.__request_helper(target_url, method="DELETE", params=request_object)
