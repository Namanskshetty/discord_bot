#!/bin/bash
figlet "WELCOME"
echo "starting bash"
echo -e "\e[1;31m Installing new version of pip and Installing requirents \e[0m"
chmod +x script.sh
sh ./script.sh
echo "Wait for 5 seconnds"
sleep 5
python3 main.py

