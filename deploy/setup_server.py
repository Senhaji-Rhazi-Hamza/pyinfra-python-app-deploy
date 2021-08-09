
from pyinfra import host
from pyinfra.operations import server

status, stdout, stderr = host.run_shell_command('ls')

#print(stdout)
