# Configure client using ssh
file_line { 'Turnoff Passwd Auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '#   PasswordAuthentication no'
}

file_line { 'Declare Identity File':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '#   IdentityFile ~/.ssh/school',
}
