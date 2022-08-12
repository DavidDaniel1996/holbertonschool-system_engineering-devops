#create a file in /tmp
file {'/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data'
}
