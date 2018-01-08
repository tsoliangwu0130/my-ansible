Vagrant.configure("2") do |config|
    # server config
    config.vm.define :server do |server_config|
 	server_config.vm.box = "bento/ubuntu-14.04"
	server_config.vm.network "forwarded_port", guest: 8080, host: 8080
        server_config.vm.network "forwarded_port", guest: 50000, host: 50000

	# run playbook from Vagrant host
	server_config.vm.provision "ansible" do |ansible|
	    ansible.playbook = "jenkins-ansible-lint.yml"
	end
    end

    # target config
    config.vm.define :target do |target_config|
        target_config.vm.box = "bento/ubuntu-14.04"
    end
end
