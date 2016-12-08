Vagrant.configure("2") do |config|
	config.vm.box = "hashicorp/precise64"
	config.vm.define "ironman"

	# run Ansible playbook from Vagrant host
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "playbook.yml"
	end
end
