#!/usr/bin/env bash

echo 'export LC_ALL="en_US.UTF-8"' >> /home/vagrant/.bashrc
sed -i '/AcceptEnv/s/^#*/#/' /etc/ssh/sshd_Config

sudo apt-get update
sudo apt install -y build-essential
sudo apt install -y zlib1g-dev
sudo apt-get install libssl-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev
sudo apt-get install lsb-release
sudo apt-get install libssl-dev

#Installing Python
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar xzf Python-3.6.5.tgz
cd Python-3.6.5
./configure
make
sudo make install

#Vytvorenie odkazu v usr/bin
sudo ln -s /usr/local/bin/python3.6 /usr/bin/python3.6

#Alternativy pre python3
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
sudo update-alternatives --set python 2

sudo apt-get install -y git python-dev

#Installing pip
wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
/usr/local/bin/python3.6 get-pip.py
sudo ln -s /usr/local/bin/pip3.6 /usr/bin/pip

pip install virtualenv