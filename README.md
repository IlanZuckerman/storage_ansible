**Intro:**  

The purpose of this script is to gather some of the basic from our ge envs (such as release version and engine state).  
It does it by running Ansible playbooks from a shell script.  
In order to build inventory file on the fly, the script needs to parse ge yamls from rhevm-jenkins project. This is why
 we have the '--pattern' argument.
Ansible will parse only those yamls which name ally with the pattern.

**Prerequisites:**  
- python3-ovirt-engine-sdk4 Installed:  
`$ sudo dnf install python3-ovirt-engine-sdk4`

- Ansible installed  
`$ sudo dnf install python3-ovirt-engine-sdk4`  
- 'shell.sh' script need to have execution permission  
`$ chmod +x <path/to/shell.sh`

**Execution:**  
- Navigate to the folder where 'shell.sh' resides  
- `$ ./shell.sh -ge_yamls_path <full path to a directory where ge yamls are stored> --pattern <pattern for specifying
 which yamls to grab>`   
Example:  
 `$ ./shell.sh --ge_yamls_path /home/ilan/git/rhevm-jenkins/qe/GE-yamls --pattern storage-ge*.yaml
`