#!/bin/bash
eho " _    _  ____  __    ___  _____  __  __  ____ 
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)
 )    (  )__)  )(__( (__  )(_)(  )    (  )__) 
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)"
echo "starting bash"
echo -e "\e[1;31m Installing new version of pip and Installing requirents \e[0m"
chmod +x script.sh
sh ./script.sh
echo "Wait for 5 seconnds"
sleep 5
python3 main.py

