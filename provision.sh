#!/bin/sh

# INSTALL APACHE, TOOLS
sudo apt update -y
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    apache2

# DOWNLOAD AND INSTALL MINICONDA
echo "------------------------------------"
echo "Downloading and installing Miniconda"
echo "------------------------------------"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
echo "____"
echo "DONE"
echo "____"

conda init

# CREATE RASAENV AND INSTALL RASA
echo "---------------------------------------"
echo "Creating virtuale environement for Rasa"
echo "---------------------------------------"
conda create -n rasaenv python=3.9
conda activate rasaenv
echo "----"
echo "DONE"
echo "----"

echo " "

echo "---------------"
echo "Installing Rasa"
echo "---------------"
pip install rasa --no-cache-dir
echo "----"
echo "DONE"
echo "----"