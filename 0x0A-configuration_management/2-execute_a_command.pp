# kills a process called killmenow

exec {'kill_process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
