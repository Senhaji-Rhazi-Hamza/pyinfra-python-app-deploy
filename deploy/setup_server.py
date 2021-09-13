import os

from pyinfra import host
from pyinfra.operations import server, init, files
from pyinfra.operations import apt
from pyinfra import local


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Package the app excluding deployment folder
APP_NAME="my_server_app"
DOCKER_IMAGE="my_py_app"
DOCKER_TAG="0.0.0"
ARCHIVE_NAME='app.tar.gz'

local.shell(
    f"tar -cvf  {ROOT_PATH}/deploy/files/{ARCHIVE_NAME} " +
    f"--exclude {ROOT_PATH}/deploy {ROOT_PATH}/* -C {ROOT_PATH} ."
)



local.include('tasks/install_docker.py')
local.include('tasks/install_nginx.py')

files.put(
    name='copy src code',
    src='files/app.tar.gz',
    dest='/opt/apps/app.tar.gz',
    mode='644',
    sudo=True,
)

server.shell(
    name='Untar the code source in the /opt/apps/{APP_NAME} folder and build the app docker image',
    commands=[f'tar -xvf /opt/apps/{ARCHIVE_NAME} -C /opt/apps/{APP_NAME}'],
    sudo=True,
)

server.shell(
    name=f'Untar the code source in the /opt/apps/{APP_NAME} folder',
    commands=[f'(test ! -d /opt/apps/{APP_NAME} &&  mkdir /opt/apps/{APP_NAME}) || echo "folder already exist"'],
    sudo=True,
)

server.shell(
    name='build and run docker image ',
    commands=[
       # "cd /opt/apps/my_server_app/ && docker image build --rm -t py_app:0.0.0 -f Dockerfile ."
        f"cd /opt/apps/{APP_NAME}/ && docker image build --rm -t {DOCKER_IMAGE}:{DOCKER_TAG} -f Dockerfile ."
        ],
    get_pty=True,
    sudo=True
)
status, stdout, stderr = host.run_shell_command('ls')
