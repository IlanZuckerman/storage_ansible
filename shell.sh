#!/bin/bash
# execution example:
# $ ./shell.sh --ge_yamls_path /home/ilan/git/rhevm-jenkins/qe/GE-yamls --pattern storage-ge*.yaml --vault_pass XXX

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -g|--ge_yamls_path) ge_yamls_path="$2"; shift ;;
        -p|--pattern) pattern="$2"; shift;;
        -v|--vault_pass) vault_pass="$2"; shift;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

echo "ge yaml path: $ge_yamls_path"
echo "pattern: $pattern"

echo "$vault_pass" > vault_pass.txt

{ # try block
  ansible-playbook tasks/make_inventory.yml -e "ge_yamls_path=$ge_yamls_path, pattern=$pattern"
  ansible-playbook -i inventory.yml tasks/setup_keys.yml -e="ansible_password=$vault_pass"
  ansible-playbook -i inventory.yml tasks/get_env_info.yml --vault-password-file vault_pass.txt
  python3 html_output.py
} || { # catch block
  echo "Something nasty happened"
}

  rm -rf vault_pass.txt # finally block
