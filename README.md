# My Ansible [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Ansible roles / playbooks to setup some tools like [Docker](https://www.docker.com/), [Jenkins](https://jenkins.io/), and etc. on Linux machine. Currently only support [Ubuntu 14.04](http://releases.ubuntu.com/14.04/).

## Table of content

#### Vagrantfile

* [Vagrantfile](Vagrantfile)

#### Ansible Roles

* [pip](roles/pip)
* [docker](roles/docker)
* [docker-jenkins](roles/docker-jenkins)
* [jenkins-ansible-lint](roles/jenkins-ansible-lint)

#### Ansible Playbooks

* [playbooks_example](playbook_example.yml)
* [docker-jenkins](docker-jenkins.yml)
* [jenkins-ansible-lint](jenkins-ansible-lint.yml)

## Usage - Locally

### ansible-playbook

1. Install [Vagrant](https://www.vagrantup.com/) and [Ansible](https://www.ansible.com/) on your local machine

2. Copy your SSH public key (if you don't have one, follow this [guideline](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) and create one)

    ```shell
    $ cat ~/.ssh/id_rsa.pub | pbcopy
    ```

3. Run and log in the VM via SSH

    ```shell
    $ vagrant up
    $ vagrant ssh
    ```

4. Add your SSH key to `~/.ssh/authorized_keys`

5. Log out the VM and run any Ansible playbook you like (feel free to modify [inventory](inventory) file as needed)

    ```shell
    $ ansible-playbook docker-jenkins.yml -i inventory
    ```

### vagrant provision

Since the ansible-playbook is also defined in [Vagrantfile](Vagrantfile) provision block, we can run the ansible-playbook when the VM first starts:

```shell
$ vagrant up
```

or do provision whenever you want run the playbook via vagrant:

```shell
$ vagrant provision
```
