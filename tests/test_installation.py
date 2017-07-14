"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name,codename', [
    ('python-apt-common', None),
    ('python-apt', None),
    ('elasticsearch', None),
    ('openjdk-7-jre', 'trusty'),
    ('openjdk-8-jre', 'xenial'),
])
def test_packages_debian_ubuntu(host, name, codename):
    """
    Tests about packages installed on Debian family
    """

    if host.system_info.distribution not in ('debian', 'ubuntu'):
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    if not codename or host.system_info.codename == codename:
        assert host.package(name).is_installed


def test_group(host):
    """
    Test about elasticsearch group
    """

    assert host.group('elasticsearch').exists


def test_user(host):
    """
    Test about elasticsearch user
    """

    user = host.user('elasticsearch')

    assert user.exists
    assert user.group == 'elasticsearch'
    assert user.shell == '/bin/false'
    assert user.home == '/home/elasticsearch'


def test_data_folder(host):
    """
    Test about elasticsearch folders
    """

    folder = host.file('/var/lib/elasticsearch')

    assert folder.exists
    assert folder.is_directory
    assert folder.user == 'elasticsearch'
    assert folder.group == 'elasticsearch'


@pytest.mark.parametrize('name,user,group', [
    ('/etc/elasticsearch/elasticsearch.yml', 'elasticsearch', 'elasticsearch'),
    ('/etc/elasticsearch/logging.yml', 'elasticsearch', 'elasticsearch'),
    ('/etc/default/elasticsearch', 'elasticsearch', 'elasticsearch'),
    ('/etc/logrotate.d/elasticsearch', 'root', 'root'),
])
def test_config_files(host, name, user, group):
    """
    Test about all configuration files
    """

    cfg_file = host.file(name)
    assert cfg_file.exists
    assert cfg_file.is_file
    assert cfg_file.user == user
    assert cfg_file.group == group


def test_process(host):
    """
    Test about elasticsearch processus
    """

    assert len(host.process.filter(user='elastic+')) == 1


def test_service(host):
    """
    Test about elasticsearch service
    """

    assert host.service('elasticsearch').is_enabled
    assert host.service('elasticsearch').is_running


def test_socket(host):
    """
    Test about elasticsearch socket
    """

    assert host.socket("tcp://127.0.0.1:9200").is_listening
    assert host.socket("tcp://127.0.0.1:9300").is_listening
