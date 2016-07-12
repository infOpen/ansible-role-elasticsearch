# openjdk-jre

[![Build Status](https://travis-ci.org/infOpen/ansible-role-openjdk-jre.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-openjdk-jre)

Install openjdk-jre package.

## Requirements

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role has two test methods :

- localy with Vagrant or Docker:
- automaticaly by Travis using docker

Tests should pass before Github push :)

Role tests are done with Docker, Tox and testinfra in temporaly container
- install [Docker](https://www.docker.com/)
- install [Tox](https://pypi.python.org/pypi/tox) into a virtualenv

### Running tests

#### Run playbook with Vagrant

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

#### Run playbook and tests with Docker

> **Warning**
> You must have an SSH keys into common location (~/.ssh/id_rsa) or set path in
>  environment variables. They will used to connect to container by SSH for
> Ansible deployment

- make test-all (for test over all Ansible version)
- or for only one version: TOXENV=py27-ansible20 make test-env

## Role Variables

Follow the possible variables with their default values

    # Package variables
    #------------------
    openjdk_jre_package_state  : present

    openjdk_jre_version : 7


Specific OS family vars :

    # Debian
    openjdk_jre_packages :
      - "openjdk-{{ openjdk_jre_version }}-jre"

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.openjdk-jre }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
