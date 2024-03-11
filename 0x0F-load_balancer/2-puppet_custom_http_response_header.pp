# 2-puppet_custom_http_response_header.pp

# Define a class for configuring the custom HTTP header
class custom_http_response_header {
  
  # Ensure nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Define a custom nginx location block to add the custom header
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
        try_files $uri $uri/ =404;
    }
}
    ",
    notify  => Service['nginx'],
  }

  # Enable and start nginx service
  service { 'nginx':
    ensure  => running,
    enable  => true,
  }

}

# Include the custom class
include custom_http_response_header
