from pyvmax import timer_counter
from pyvmax.vmaxapi import VmaxApi


class VmaxApi81(VmaxApi):
    """API definition class that implements one method for each REST API call
    Attributes:
        version (str): descripter of the API version
        api_counter (int): number of API calls made during this python interpreter session
        api_timer (int): sum of ms response time of all API calls made during this python interpreter session
        api_last_resp_time (int): ms response time of last API call made during this python interpreter session
    Args:
        Restful (:obj:`Restful`): connection object to the API server
        base_url (str):  the ip and port # of api server
    """
    def __init__(self, Restful, base_url):
        super(VmaxApi81, self).__init__(Restful, base_url)
        self.version = "v81"

    ######################################
    # PERFORMANCE Resource group
    ######################################
    @timer_counter
    def get_perf_host_keys(self, params_dict):
        target_uri = "%s/81/performance/Host/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_host_metrics(self, params_dict):
        target_uri = "%s/81/performance/Host/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_initiator_keys(self, params_dict):
        target_uri = "%s/81/performance/Initiator/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_initiator_metrics(self, params_dict):
        target_uri = "%s/81/performance/Initiator/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_initiatorbyport_keys(self, params_dict):
        target_uri = "%s/81/performance/InitiatorByPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_initiatorbyport_metrics(self, params_dict):
        target_uri = "%s/81/performance/InitiatorByPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_iscsiclient_keys(self, params_dict):
        target_uri = "%s/81/performance/ISCSIClient/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_scsiclient_metrics(self, params_dict):
        target_uri = "%s/81/performance/ISCSIClient/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_iscsitarget_keys(self, params_dict):
        target_uri = "%s/81/performance/ISCSITarget/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_scsitarget_metrics(self, params_dict):
        target_uri = "%s/81/performance/ISCSITarget/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    ######################################
    # REPLICATION Resource group
    ######################################
    @timer_counter
    def get_replica_devicegroup(self, group_id):
        target_uri = "%s/81/replication/devicegroup/%s" % (self.rest.url, group_id)
        return self.rest.get(target_uri)

    ######################################
    # VVOL Resource group
    ######################################
    @timer_counter
    def get_vvol_arrays(self):
        target_uri = "%s/81/vvol/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    @timer_counter
    def get_vvol_array(self, array_id):
        target_uri = "%s/81/vvol/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_vvol_array_protocolendpoints(self, array_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def create_vvol_array_maskingview(self, array_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_vvol_array_protocolendpoint(self, array_id, proto_id):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint/%s" % (self.rest.url, array_id, proto_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_vvol_array_storagecontainers(self, array_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def create_vvol_array_storagecontainer(self, array_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_vvol_array_storagecontainer(self, array_id, storcont_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_vvol_array_storagecontainer(self, array_id, storcont_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def delete_vvol_array_storagecontainer(self, array_id, storcont_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.delete(target_uri)

    @timer_counter
    def get_vvol_array_storagecontainer_storageresources(self, array_id, storcont_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s/storageresource" % (self.rest.url, array_id, storcont_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def get_vvol_array_storagecontainer_storageresource(self, array_id, storcont_id, storresource_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%sstorageresource/%s" % (self.rest.url, array_id, storcont_id, storresource_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_vvol_array_storagecontainer_storageresource(self, array_id, storcont_id, storresource_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%sstorageresource/%s" % (self.rest.url, array_id, storcont_id, storresource_id)
        return self.rest.put(target_uri, params_dict)
