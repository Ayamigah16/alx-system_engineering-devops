# File: 0x0A-configuration_management/0-create_a_file.pp
# Description: Create a file in /tmp with specific permissions, owner, group, and content

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
