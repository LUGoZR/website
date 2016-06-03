# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |django_config|
  django_config.vm.box = "djangolug"
  django_config.vm.box_url = "https://lugozr.org/dl/djangolug.box"

  # setting up machine specifications
  django_config.vm.provider :virtualbox do |p|
    p.customize ["modifyvm", :id, "--memory", 1024]
    p.customize ["modifyvm", :id, "--cpus", 1]
    p.customize ["modifyvm", :id, "--cpuexecutioncap", 50]
  end

  # setting up folders
  django_config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", :mount_options => ["dmode=777","fmode=777"]

  # setting up hostname
  django_config.vm.hostname = "django.lug"
  django_config.hostmanager.enabled = true
  django_config.hostmanager.manage_host

  # setting up network
  django_config.vm.network :private_network, ip: '192.168.150.150'
  django_config.vm.network "forwarded_port", guest: 80, host: 8080
  django_config.vm.network "forwarded_port", guest: 8000, host: 8000

  # provisioning
  django_config.vm.provision :shell, path: "vagrant_bootstrap.sh"

end

