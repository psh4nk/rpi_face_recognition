#!/bin/bash

# This script installs and enables XRDP and XFCE4 on Raspberry Pi 4 B+ running the 32-bit version of Raspbian.

# Directions:
# Download file: wget https://gist.github.com/psh4nk/523dabd67a95ae2dc0cf8e37d7afc8d0
# Set file permissions to allow execution: chmod u+x ./xrdp.sh
# Run file: ./xrdp.sh

sudo apt-get install -y xrdp xfce4
echo xfce4-session > ~/.xsession
sudo sed -i '/\/dev\/dri\/renderD128/c\Option "DRMDevice\" \"\"' /etc/X11/xrdp/xorg.conf
sudo systemctl restart xrdp
