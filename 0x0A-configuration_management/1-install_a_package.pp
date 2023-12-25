# File: 0x0A-configuration_management/1-install_a_package.pp
# Description: Install Flask version 2.1.0 using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',  # or the version compatible with Flask 2.1.0
  provider => 'pip3',
}
