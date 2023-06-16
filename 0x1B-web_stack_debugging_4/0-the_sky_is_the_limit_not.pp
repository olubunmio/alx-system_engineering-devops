# Increase the ULIMIT of the nginx default config file
exec { 'increase-nginx-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
# Restart Nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
