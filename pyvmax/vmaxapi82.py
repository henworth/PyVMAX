from pyvmax import timer_counter
from pyvmax.vmaxapi81 import VmaxApi81


class VmaxApi82(VmaxApi81):
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
        super(VmaxApi82, self).__init__(Restful, base_url)
        self.version = "v82"

    ######################################
    # PERFORMANCE Resource group
    ######################################
    @timer_counter
    def get_perf_storagecontainer_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageContainer/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_storagecontainer_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageContainer/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_storageresrource_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageResource/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_storageresource_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageResource/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_storageresrourcebypool_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageResourceByPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_perf_storageresourcebypool_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageResourceByPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    ######################################
    # PROVISIONING Resource group
    ######################################
    @timer_counter
    def get_prov_array(self, array_id):
        target_uri = "%s/82/provisioning/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    ######################################
    # REPLICATION Resource group
    ######################################
    @timer_counter
    def get_replica_srdfgroup(self, symm_id, rdfg_num):
        target_uri = "%s/82/replication/symmetrix/%s/rdf_group/%s" % (self.rest.url, symm_id, rdfg_num)
        return self.rest.get(target_uri)

    @timer_counter
    def get_replica_storagegroups(self, symm_id, params_dict=None):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup" % (self.rest.url, symm_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def get_replica_storagegroup(self, symm_id, group_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s" % (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_replica_storagegroup_srdfgroups(self, symm_id, group_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group" % (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    @timer_counter
    def create_replica_storagegroup_srdf(self, symm_id, group_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group" % (self.rest.url, symm_id, group_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.put(target_uri)

    @timer_counter
    def delete_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.delete(target_uri, params_dict)

    @timer_counter
    def create_replica_storagegroup_snapshot(self, symm_id, group_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/snapshot" % (self.rest.url, symm_id, group_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def recreate_replica_storagegroup_snapshot(self, symm_id, group_id, snap_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation" % (self.rest.url, symm_id, group_id, snap_id)
        return self.rest.post(target_uri, params_dict)

    ######################################
    # SLO PROVISIONING Resource group
    ######################################
    @timer_counter
    def get_slo_arrays(self):
        target_uri = "%s/82/sloprovisioning/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array(self, array_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array_splits(self, array_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array_split(self, array_id, split_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s" % (self.rest.url, array_id, split_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array_split_cuimages(self, array_id, split_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage" % (self.rest.url, array_id, split_id)
        return self.rest.get(target_uri)

    @timer_counter
    def create_slo_array_split_cuimages(self, array_id, split_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage" % (self.rest.url, array_id, split_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_slo_array_split_cuimage(self, array_id, split_id, cu_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_slo_array_split_cuimage(self, array_id, split_id, cu_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def get_slo_array_split_cuimage_volumes(self, array_id, split_id, cu_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s/volume" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array_split_cuimage_volume(self, array_id, split_id, cu_id, vol_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s/volume/%s" % (self.rest.url, array_id, split_id, cu_id, vol_id)
        return self.rest.get(target_uri)

    @timer_counter
    def provision_slo_array_split(self, array_id, split_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/storageProvisioningToHost" % (self.rest.url, array_id, split_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_slo_array_srps(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/srp" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def get_slo_array_srp(self, array_id, srp_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp/%s" % (self.rest.url, array_id, srp_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_slo_array_storagegroups(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def create_slo_array_storagegroup(self, array_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_slo_array_storagegroup(self, array_id, sg_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_slo_array_storagegroup(self, array_id, sg_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def delete_slo_array_storagegroup(self, array_id, sg_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.delete(target_uri)

    @timer_counter
    def get_slo_array_volumes(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/volume" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def get_slo_array_volume(self, array_id, volume_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/volume/%s" % (self.rest.url, array_id, volume_id)
        return self.rest.get(target_uri)

    ######################################
    # SYSTEM Resource group
    ######################################
    @timer_counter
    def get_alert_summary(self):
        target_uri = "%s/82/system/alert_summary" % (self.rest.url)
        return self.rest.get(target_uri)

    ######################################
    # VVOL Resource group
    ######################################
    @timer_counter
    def get_vvol_array_vasaprovider(self, array_id):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def create_vvol_array_vasaprovider(self, array_id, params_dict):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def edit_vvol_array_vasaprovider(self, array_id, params_dict):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def delete_vvol_array_vasaprovider(self, array_id):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.delete(target_uri)

    ######################################
    # WORKLOAD Resource group
    ######################################

    @timer_counter
    def get_workload_array(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def edit_workload_array(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def get_workload_array_admissibility(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/admissibility" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_workload_array_sgcompliances(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s/compliance" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def get_workload_array_headroom(self, array_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/headroom" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def get_workload_array_referenceworkloads(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    @timer_counter
    def create_workload_array_referenceworkload(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    @timer_counter
    def get_workload_array_referenceworkload(self, array_id, work_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.get(target_uri, params_dict)

    @timer_counter
    def delete_workload_array_referenceworkload(self, array_id, work_id):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.delete(target_uri)

    @timer_counter
    def edit_workload_array_referenceworkload(self, array_id, work_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.put(target_uri, params_dict)

    @timer_counter
    def get_workload_array_utilization(self, array_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/utilization" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)
