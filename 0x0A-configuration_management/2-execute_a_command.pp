# File: 0x0A-configuration_management/2-execute_a_command.pp
# Description: Kill a process named "killmenow" using pkill

exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
