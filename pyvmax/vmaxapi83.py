from pyvmax import timer_counter
from pyvmax.vmaxapi82 import VmaxApi82


class VmaxApi83(VmaxApi82):
    """API definition class that implements one method for each REST API call
    Attributes:
        version (str): descripter of the API version
        api_counter (int): number of API calls made during this python interpreter session
        api_timer (int): sum of ms response time of all API calls made during this python interpreter session
        api_last_resp_time (int): ms response time of last API call made during this python interpreter session
    Args:
        restful (:obj:`Restful`): connection object to the API server
        base_url (str):  the ip and port # of api server
    """
    def __init__(self, restful, base_url):
        super(VmaxApi83, self).__init__(restful, base_url)
        self.version = "v83"

    ######################################
    # VVOL Resource group
    ######################################
    @timer_counter
    def get_vvol_array_storagecontainers(self, array_id, params=None):
        target_uri = "{}/83/vvol/symmetrix/{}/storagecontainer".format(self.rest.url, array_id)
        return self.rest.get(target_uri, params)
