import os

from pyinfra import host
from pyinfra.operations import server, init
from pyinfra.operations import apt
from pyinfra import local

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Package the app excluding deployment folder

local.shell(
    f"tar -cvf  {ROOT_PATH}/deploy/files/app.tar.gz"
    f"--exclude {ROOT_PATH}/deploy {ROOT_PATH}/*"
)

# local.include('tasks/install_docker.py')


server.shell(
    name='Install docker',
    commands=[
        "apt-get update -y",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
        'sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"',
        "apt-get update -y",
        "apt-get install docker-ce docker-ce-cli containerd.io -y"
    ],
    sudo=True
)

# apt.packages(
#     name='Ensure docker is installed',
#     packages=['docker-ce', 'docker-ce-cli', 'containerd.io'],
#     sudo=True,
#     update=True,
# )

local.include('tasks/install_nginx.py')


server.shell(
    name='reload nginx to ensure it has started',
    commands=['nginx -s reload'],
    sudo=True,
)

status, stdout, stderr = host.run_shell_command('ls')
