#!/bin/bash
# execution example:
# ./shell.sh /home/ilan/git/rhevm-jenkins/qe/GE-yamls

if [ $# -eq 0 ]
  then
    echo "No arguments supplied.
You need to pass a full path of where the storage-ge yamls are"
    exit 1
fi

ansible-playbook make_inventory.yml -e "ge_yamls_path=$1"
ansible-playbook -i inventory.yml setup_keys.yml -e="ansible_password=qum5net"
ansible-playbook -i inventory.yml get_env_info.yml