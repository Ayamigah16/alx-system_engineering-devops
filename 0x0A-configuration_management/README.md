# 0x0A. Configuration management

## Puppet Configuration Management Project

### Description
This project involves setting up and configuring Puppet on Ubuntu 20.04 LTS using Puppet manifests. The goal is to complete various tasks related to configuration management.

### Requirements
- Ubuntu 20.04 LTS
- Puppet 5.5 preinstalled
- Puppet manifests following specified guidelines
- Puppet-lint version 2.1.1

### Tasks Completed

#### Task 0: Create a File
Create a file in /tmp with specific permissions, owner, group, and content.

- File path: /tmp/school
- File permission: 0744
- File owner: www-data
- File group: www-data
- File content: I love Puppet

```bash
$ puppet apply 0x0A-configuration_management/0-create_a_file.pp

#### Task 1: Install a Package
Install Flask version 2.1.0 using pip3.

- Install **flask**
- Version must be **2.1.0**

```bash
$ puppet apply 0x0A-configuration_management/1-install_a_package.pp

#### Task 2: Execute a command
Kill a process named "killmenow" using the exec Puppet resource and pkill.

- Must use the **exec** Puppet resource
- Must use **pkill**

```bash
$ puppet apply 0x0A-configuration_management/2-execute_a_command.pp

### Versioning
This project uses Puppet 5.5, as specified in the requirements

### Running the Manifests
To apply the Puppet manifests, use the following command:
```bash
$ puppet apply <manifest_file.pp>

Make sure to adapt the file paths, package names, and versions according to your needs.

### Puppet-Lint Checks
Run puppet-lint on your manifests to ensure they pass without any errors.

```bash
$ puppet-lint 0x0A-configuration_management/