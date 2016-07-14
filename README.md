elasticsearch
=============

[![Build Status](https://travis-ci.org/infOpen/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-elasticsearch)

Install ntp package.

Requirements
------------

This role requires Ansible 2.1 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Defaults variables for elasticsearch

    # Package variables
    #------------------
    elasticsearch_package_state   : present

    # Service variables
    #------------------
    elasticsearch_service_state   : started
    elasticsearch_service_enabled : True

    ################################### Cluster ###################################
    elasticsearch_cluster_name : 'elasticsearch'


    #################################### Node #####################################
    elasticsearch_node_master : True
    elasticsearch_node_data   : True
    elasticsearch_custom_var  : {}
    elasticsearch_node_max_local_storage_nodes : 1


    #################################### Index ####################################
    elasticsearch_index_number_of_shards   : 5
    elasticsearch_index_number_of_replicas : 1


    #################################### Paths ####################################
    elasticsearch_path_conf     : /etc/elasticsearch
    elasticsearch_path_work     : /tmp/elasticsearch
    elasticsearch_path_logs     : /var/log/elasticsearch
    elasticsearch_path_plugins  : /usr/share/elasticsearch/plugins
    elasticsearch_path_data     :
      - /var/lib/elasticsearch


    #################################### Plugin ###################################
    elasticsearch_plugin_mandatory : []


    ################################### Memory ####################################
    elasticsearch_bootstrap_mlockall : False


    ############################## Network And HTTP ###############################
    elasticsearch_network_bind_host       : 127.0.0.1
    elasticsearch_network_publish_host    : 127.0.0.1
    elasticsearch_network_host            : 127.0.0.1
    elasticsearch_transport_tcp_port      : 9300
    elasticsearch_transport_tcp_compress  : False
    elasticsearch_http_port               : 9200
    elasticsearch_http_max_content_length : 100mb
    elasticsearch_http_enabled            : True


    ################################### Gateway ###################################
    elasticsearch_gateway_type                : local
    elasticsearch_gateway_recover_after_nodes : 1
    elasticsearch_gateway_recover_after_time  : 5m
    elasticsearch_gateway_expected_nodes      : 2


    ############################# Recovery Throttling #############################
    elasticsearch_cluster_routing_allocation_node_initial_primaries_recoveries : 4
    elasticsearch_cluster_routing_allocation_node_concurrent_recoveries        : 2
    elasticsearch_indices_recovery_max_bytes_per_sec  : 20mb
    elasticsearch_indices_recovery_concurrent_streams : 5


    ################################## Discovery ##################################
    elasticsearch_discovery_zen_minimum_master_nodes   : 1
    elasticsearch_discovery_zen_ping_timeout           : 3s
    elasticsearch_discovery_zen_ping_multicast_enabled : True
    elasticsearch_discovery_zen_ping_unicast_hosts     : []


    ################################## Slow Log ##################################
    elasticsearch_index_search_slowlog_threshold_query_warn    : 10s
    elasticsearch_index_search_slowlog_threshold_query_info    : 5s
    elasticsearch_index_search_slowlog_threshold_query_debug   : 2s
    elasticsearch_index_search_slowlog_threshold_query_trace   : 500ms

    elasticsearch_index_search_slowlog_threshold_fetch_warn    : 1s
    elasticsearch_index_search_slowlog_threshold_fetch_info    : 800ms
    elasticsearch_index_search_slowlog_threshold_fetch_debug   : 500ms
    elasticsearch_index_search_slowlog_threshold_fetch_trace   : 200ms

    elasticsearch_index_indexing_slowlog_threshold_index_warn  : 10s
    elasticsearch_index_indexing_slowlog_threshold_index_info  : 5s
    elasticsearch_index_indexing_slowlog_threshold_index_debug : 2s
    elasticsearch_index_indexing_slowlog_threshold_index_trace : 500ms


    ################################## GC Logging ################################
    elasticsearch_monitor_jvm_gc_young_warn  : 1000ms
    elasticsearch_monitor_jvm_gc_young_info  : 700ms
    elasticsearch_monitor_jvm_gc_young_debug : 400ms

    elasticsearch_monitor_jvm_gc_old_warn    : 10s
    elasticsearch_monitor_jvm_gc_old_info    : 5s
    elasticsearch_monitor_jvm_gc_old_debug   : 2s


    ################################## Security ################################
    elasticsearch_http_jsonp_enable: False


Specific OS family vars :

    # Debian
    elasticsearch_packages :
      - elasticsearch
    elasticsearch_service_name: elasticsearch

Dependencies
------------

- infOpen.openjdk-jre

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: infOpen.elasticsearch }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
