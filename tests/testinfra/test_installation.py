"""
Role tests
"""
import pytest


# pytestmark = pytest.mark.docker_images(
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_packages(SystemInfo, Package):
    """
    Tests about packages installed on all systems
    """

    packages = ['python-apt-common', 'python-apt', 'elasticsearch']

    for package in packages:
        assert Package(package).is_installed is True

    if SystemInfo.codename == 'trusty':
        assert Package('openjdk-7-jre').is_installed is True
    elif SystemInfo.codename == 'xenial':
        assert Package('openjdk-8-jre').is_installed is True


def test_os_type(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_group(Group):
    """
    Test about elasticsearch group
    """

    assert Group('elasticsearch').exists


def test_user(User):
    """
    Test about elasticsearch user
    """

    user = User('elasticsearch')

    assert user.exists
    assert user.group == 'elasticsearch'
    assert user.shell == '/bin/false'
    assert user.home == '/home/elasticsearch'


def test_data_folder(File):
    """
    Test about elasticsearch folders
    """

    folder = File('/var/lib/elasticsearch')

    assert folder.exists
    assert folder.is_directory
    assert folder.user == 'elasticsearch'
    assert folder.group == 'elasticsearch'


def test_config_files(File):
    """
    Test about all configuration files
    """

    files = [
        '/etc/elasticsearch/elasticsearch.yml',
        '/etc/elasticsearch/logging.yml',
        '/etc/default/elasticsearch',
    ]

    for cur_file in files:
        cfg_file = File(cur_file)
        assert cfg_file.exists
        assert cfg_file.is_file
        assert cfg_file.user == 'elasticsearch'
        assert cfg_file.group == 'elasticsearch'

    logrotate_file = File('/etc/logrotate.d/elasticsearch')
    assert logrotate_file.exists
    assert logrotate_file.is_file
    assert logrotate_file.user == 'root'
    assert logrotate_file.group == 'root'


def test_process(Process):
    """
    Test about elasticsearch processus
    """

    assert len(Process.filter(user='elastic+')) == 1


def test_service(Command, Service, Socket):
    """
    Test about elasticsearch service
    """

    assert Service('elasticsearch').is_enabled
    assert Service('elasticsearch').is_running
    assert Socket("tcp://127.0.0.1:9200").is_listening
    assert Socket("tcp://127.0.0.1:9300").is_listening
