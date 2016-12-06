Vagrant.configure("2") do |config|
	config.vm.box = "hashicorp/precise64"
	config.vm.define "ironman"

	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.verbose  = ""
	end
end
