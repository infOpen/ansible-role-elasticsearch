# elasticsearch

[![Build Status](https://travis-ci.org/infOpen/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-elasticsearch)

Install elasticsearch package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Package variables
#------------------
elasticsearch_apt_cache_valid_time: 3600
elasticsearch_packages: "{{ _elasticsearch_packages }}"
elasticsearch_system_dependencies: "{{ _elasticsearch_system_dependencies }}"
elasticsearch_repositories: "{{ _elasticsearch_repositories }}"

# Service variables
#------------------
elasticsearch_service_name: "{{ _elasticsearch_service_name }}"
elasticsearch_service_state: 'started'
elasticsearch_service_enabled: True

# Elasticsearch default version
elasticsearch_version: '5.x'

# Paths management
elasticsearch_config_files_mode: '0400'

elasticsearch_data_dir_path: "{{ _elasticsearch_data_dir_path }}"
elasticsearch_etc_dir_path: "{{ _elasticsearch_etc_dir_path }}"
elasticsearch_home_dir_path: "{{ _elasticsearch_home_dir_path }}"
elasticsearch_limits_dir_path: "{{ _elasticsearch_limits_dir_path }}"
elasticsearch_log_dir_path: "{{ _elasticsearch_log_dir_path }}"
elasticsearch_logrotate_dir_path: "{{ _elasticsearch_logrotate_dir_path }}"
elasticsearch_pid_dir_path: "{{ _elasticsearch_pid_dir_path }}"

elasticsearch_dirs_paths:
  - path: "{{ _elasticsearch_data_dir_path }}"
    mode: '0700'
    state: 'directory'
  - path: "{{ _elasticsearch_etc_dir_path }}"
    mode: '0500'
    state: 'directory'
  - path: "{{ _elasticsearch_home_dir_path }}"
    mode: '0700'
    state: 'directory'
  - path: "{{ _elasticsearch_log_dir_path }}"
    mode: '0700'
    state: 'directory'


# User and group management
elasticsearch_user_name: 'elasticsearch'
elasticsearch_group_name: 'elasticsearch'


# Sysctl virtual memory setting
elasticsearch_sysctl_rules:
  - name: 'vm.max_map_count'
    value: 262144
    state: 'present'


# Security limits rules
elasticsearch_limits_rules:
  - 'elasticsearch soft memlock unlimited'
  - 'elasticsearch hard memlock unlimited'


# Default configuration file
#---------------------------
elasticsearch_java_home: ''
elasticsearch_java_opts: []
elasticsearch_limit_nproc: 2048
elasticsearch_max_open_files: 65536
elasticsearch_max_locked_memory: 'unlimited'
elasticsearch_max_map_count: 262144
elasticsearch_restart_on_upgrade: 'true'
elasticsearch_startup_sleep_time: 5


# Main configuration file
#------------------------

elasticsearch_config_base: "{{ _elasticsearch_config_base }}"
elasticsearch_config_xpack: "{{ _elasticsearch_config_xpack }}"
elasticsearch_manage_xpack: False

_elasticsearch_config_base:
  cluster:
    name: 'es-cluster01'
  http:
    port: 9200
  network:
    host: '127.0.0.1'
  node:
    max_local_storage_nodes: 1
    name: "{{ ansible_hostname }}"
  path:
    conf: "{{ elasticsearch_etc_dir_path }}"
    data: "{{ elasticsearch_data_dir_path }}"
    logs: "{{ elasticsearch_log_dir_path }}"
_elasticsearch_config_xpack:
  xpack:
    monitoring:
      enabled: False
    security:
      enabled: False
    watcher:
      enabled: False


# Logrotate settings
#-------------------
elasticsearch_logrotate_rules:
  - 'daily'
  - 'dateext'
  - 'dateformat _%Y-%m-%d'
  - 'rotate 31'
  - 'copytruncate'
  - 'compress'
  - 'delaycompress'
  - 'missingok'
  - "create 644 {{ elasticsearch_user_name }} {{ elasticsearch_group_name }}"
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.elasticsearch }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
