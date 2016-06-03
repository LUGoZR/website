#!/bin/bash

echo 'Installing git, Python 3, and pip...'
sudo apt-get -qq install git python3 python3-dev libjpeg-dev libtiff5-dev zlib1g-dev > /dev/null 2>&1
curl -s https://bootstrap.pypa.io/get-pip.py | python3.4 > /dev/null 2>&1

echo 'Installing and configuring virtualenv and virtualenvwrapper...'
pip install --quiet virtualenvwrapper==4.7.0 Pygments==2.1.1
mkdir ~vagrant/virtualenvs
chown vagrant:vagrant ~vagrant/virtualenvs
printf "\n\n# Virtualenv settings\n" >> ~vagrant/.bashrc
printf "export PYTHONPATH=/usr/lib/python3.4" >> ~vagrant/.bashrc
printf "export WORKON_HOME=~vagrant/virtualenvs\n" >> ~vagrant/.bashrc
printf "export PROJECT_HOME=/vagrant\n" >> ~vagrant/.bashrc
printf "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.4\n" >> ~vagrant/.bashrc
printf "source /usr/local/bin/virtualenvwrapper.sh\n" >> ~vagrant/.bashrc

# Some useful aliases for getting started, MotD
echo 'Setting up message of the day, and some aliases...'
printf "alias runserver='python manage.py runserver 0.0.0.0:8000'\n" >> ~vagrant/.bashrc

echo ""
echo "Vagrant install complete."
echo "Now try logging in:"
echo "    $ vagrant ssh"

