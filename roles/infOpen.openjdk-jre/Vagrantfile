# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

VMS = {
  :openjdk_jre_trusty => {
    :box => "ubuntu/trusty64"
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  VMS.each_pair do |name, options|

    config.vm.define name do |vm_config|

      # Set proper box
      vm_config.vm.box = options[:box]

      # Use trigger plugin to set environment variable used by Ansible
      # Needed with 2.0 home path change
      vm_config.vm.provision "trigger" do |trigger|
        trigger.fire do
          ENV['ANSIBLE_ROLES_PATH'] = '../'
          ENV['ANSIBLE_ROLE_NAME'] = File.basename(Dir.getwd)
        end
      end

      # Run Ansible provisioning
      vm_config.vm.provision "ansible" do |ansible|
        ansible.playbook  = "tests/test_vagrant.yml"
      end

    end
  end
end
