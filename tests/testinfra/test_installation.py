"""
Role tests
"""
import pytest


# pytestmark = pytest.mark.docker_images(
pytestmark = pytest.mark.docker_images('infopen/ubuntu-xenial-ssh-py27:0.1.0')


def test_packages(Package):
    """
    Tests about packages installed on all systems
    """

    packages = [
        'python-apt-common', 'python-apt', 'elasticsearch', 'openjdk-9-jre'
    ]

    for package in packages:
        assert Package(package).is_installed is True


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
    assert user.home == '/var/lib/elasticsearch'


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
        '/etc/logrotate.d/elastic-search'
    ]

    for cur_file in files:
        cfg_file = File(cur_file)
        assert cfg_file.exists
        assert cfg_file.is_file
        assert cfg_file.user == 'root'
        assert cfg_file.group == 'root'


def test_process(Process):
    """
    Test about elasticsearch processus
    """

    assert len(Process.filter(user='elasticsearch')) == 1
