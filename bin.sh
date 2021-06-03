#!/bin/bash
echo "
 _  _  ____  __     ___  __   _  _  ____ 
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)
"
echo "starting bash"
echo -e "\e[1;31m Installing new version of pip \e[0m"
pip install --upgrade pip
echo -e "\e[1;31m Installing requirents \e[0m"
pip install -r requirements.txt
echo "Wait for 5 seconnds"
sleep 5
python3 main.py

