# Puppet manifest to install and configure Nginx web server on Ubuntu

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    
    error_page 404 /404.html
    location = /404.html {
      root /usr/share/nginx/html;
      internal;
    }
}
",
}

# Restart Nginx (without using systemctl)
exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,
}

# Create a default HTML page with the content "Hello World!"
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Notify the Nginx restart when the HTML page is modified
File['/var/www/html/index.html'] -> Exec['nginx-restart']
