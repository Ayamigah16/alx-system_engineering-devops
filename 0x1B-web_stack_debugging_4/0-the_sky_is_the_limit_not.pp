# fixes number of open files
exec { 'fix--for-nginx':
  command => "/bin/sed -i 's/15/3000/g' /etc/default/nginx "
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix--for-nginx']
}
