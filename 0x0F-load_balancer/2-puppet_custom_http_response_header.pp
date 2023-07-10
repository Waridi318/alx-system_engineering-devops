# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx custom HTTP header response
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By $::fqdn;",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}
