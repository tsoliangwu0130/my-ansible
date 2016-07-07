Vagrant.configure(2) do |config|
  config.vm.box = "brightmarch/debian-8.4-amd64"
  config.vm.define "vagrant-server"
  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "forwarded_port", guest: 8080, host: 8082
  config.vm.network "forwarded_port", guest: 8090, host: 8092

  config.vm.provider "virtualbox" do |v|
    v.memory = 8192
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook/index.yml"
  end
end
