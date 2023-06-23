# this manifest installs flask

exec {'flask':
  command => 'usr/bin/pip3 install flask -v 2.1.0',
}
