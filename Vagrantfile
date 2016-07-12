# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

VMS = {
  :elasticsearch_trusty => {
    :box => 'ubuntu/trusty64'
  },
  :elasticsearch_xenial => {
    :box => 'ubuntu/xenial64'
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  VMS.each_pair do |name, options|

    config.vm.define name do |vm_config|

      # Set proper box
      vm_config.vm.box = options[:box]


      # Virtualbox vm name management
      vm_config.vm.provider "virtualbox" do |vm|
          vm.name = name.to_s
      end


      # Use trigger plugin to set environment variable used by Ansible
      # Needed with 2.0 home path change
      vm_config.vm.provision 'trigger' do |trigger|
        trigger.fire do
          ENV['ANSIBLE_ROLES_PATH'] = '../'
          ENV['ANSIBLE_ROLE_NAME'] = File.basename(Dir.getwd)
        end
      end


      # Install python 2.7 if not present (On Xenial)
      vm_config.vm.provision 'shell' do |sh|
        sh.inline = '! type -P python2.7 \
                     && (sudo apt-get update \
                     && sudo apt-get install python2.7 -y) || true'
      end


      # Run Ansible provisioning
      vm_config.vm.provision 'ansible' do |ansible|
        ansible.playbook = 'tests/test_vagrant.yml'
        ansible.galaxy_role_file = './requirements.yml'
        ansible.extra_vars = {
          ansible_python_interpreter: '/usr/bin/env python2.7'
        }
        ansible.host_vars = {
          'elasticsearch_xenial' => {'openjdk_jre_version' => 9}
        }
      end

    end
  end
end
