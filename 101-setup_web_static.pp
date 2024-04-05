# File: /etc/puppet/manifests/site.pp

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><body>Fake HTML content for testing</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Update Nginx configuration
class { 'nginx':
  alias => '/data/web_static/current',
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
  require => Class['nginx'],
}
