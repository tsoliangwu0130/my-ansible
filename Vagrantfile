Vagrant.configure("2") do |config|
	# Server: ironman
	config.vm.define :ironman do |ironman_config|
		ironman_config.vm.box = "hashicorp/precise64"
		ironman_config.vm.network "forwarded_port", guest: 8080, host: 9080

		# run Ansible playbook from Vagrant host
		ironman_config.vm.provision "ansible" do |ansible|
			ansible.playbook = "playbook.yml"
		end
	  end

	# Server: ironman_target
	config.vm.define :ironman_target do |ironman_target_config|
		ironman_target_config.vm.box = "hashicorp/precise64"
	  end	
end
