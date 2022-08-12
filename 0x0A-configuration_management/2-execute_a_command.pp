#kills process killmenow
exec{'kill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
