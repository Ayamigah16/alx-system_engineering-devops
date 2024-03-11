#!/usr/bin/env puppet

# Automating SSH client configuration using Puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
