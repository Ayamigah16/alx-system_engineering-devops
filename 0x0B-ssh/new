# 100-puppet_ssh_config.pp

# Ensure the SSH client configuration directory exists
file { '/home/root/.ssh':
  ensure => 'directory',
  mode   => '0700',
  owner  => 'root',
  group  => 'root',
}

# Ensure the SSH client configuration file exists
file { '/home/root/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
  content => template('./ssh_config.erb'),
}

# Disable password authentication and set the identity file in the SSH client configuration
file_line { 'Turn off passwd auth':
  path  => '/home/root/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/home/root/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}
