# Using strace, find out why Apache is returning a 500 error


$file_to_edit = '/var/www/html/wp-settings.php'

#replace line 

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
