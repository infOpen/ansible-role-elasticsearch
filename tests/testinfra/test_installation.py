"""
Role tests
"""
import pytest

pytestmark = pytest.mark.destructive


@pytest.mark.docker_images('infopen/ubuntu-trusty-ssh:0.1.0')
def test_trusty_packages(Package):
    """
    Tests about packages installed on Trusty
    """

    packages = ['python-apt-common', 'python-apt', 'openjdk-7-jre']

    for package in packages:
        assert Package(package).is_installed is True


@pytest.mark.docker_images('infopen/ubuntu-xenial-ssh-py27:0.1.0')
def test_xenial_packages(Package):
    """
    Tests about packages installed on Xenial
    """

    packages = ['python-apt-common', 'python-apt', 'openjdk-9-jre']

    for package in packages:
        assert Package(package).is_installed is True
