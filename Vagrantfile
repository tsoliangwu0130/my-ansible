Vagrant.configure("2") do |config|
	config.vm.box = "hashicorp/precise64"
	config.vm.define "ironman"
	config.vm.network "forwarded_port", guest: 8080, host: 9080

	# run Ansible playbook from Vagrant host
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "playbook.yml"
	end
end
