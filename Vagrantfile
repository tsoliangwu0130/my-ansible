Vagrant.configure("2") do |config|
	# Server: jenksin_server
	config.vm.define :jenksin_server do |jenkins_config|
		jenkins_config.vm.box = "hashicorp/precise64"
		jenkins_config.vm.network "forwarded_port", guest: 8080, host: 9080

		# run Ansible playbook from Vagrant host
		jenkins_config.vm.provision "ansible" do |ansible|
			ansible.playbook = "playbook.yml"
		end
	  end

	# Server: jenkins_target
	config.vm.define :jenkins_target do |jenkins_target_config|
		ironman_target_config.vm.box = "hashicorp/precise64"
	  end	
end
