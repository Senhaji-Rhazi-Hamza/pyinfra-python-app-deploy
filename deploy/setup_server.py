import os

from pyinfra import host
from pyinfra.operations import server, files
from pyinfra import local


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


APP_NAME="my_server_app"
DOCKER_IMAGE="my_py_app"
DOCKER_TAG="0.0.0"
ARCHIVE_NAME='app.tar.gz'

# Package your app into an archive excluding deployment folder
local.shell(
    f"tar -cvf  {ROOT_PATH}/deploy/files/{ARCHIVE_NAME} " +
    f"--exclude {ROOT_PATH}/deploy {ROOT_PATH}/* -C {ROOT_PATH} ."
)


# install docker if not installed
local.include('tasks/install_docker.py')

# install nginx if not installed
local.include('tasks/install_nginx.py')

files.put(
    name='Copy src code to remote machine',
    src='files/app.tar.gz',
    dest='/opt/apps/app.tar.gz',
    mode='644',
    sudo=True,
)

server.shell(
    name='Untar the code source in the /opt/apps/{APP_NAME} folder and build the app docker image',
    commands=[
        f'(test ! -d /opt/apps/{APP_NAME} &&  mkdir /opt/apps/{APP_NAME}) || echo "folder already exist"',
        f'tar -xvf /opt/apps/{ARCHIVE_NAME} -C /opt/apps/{APP_NAME}'
        ],
    sudo=True,
)


server.shell(
    name='Build and run docker image ',
    commands=[
        f"cd /opt/apps/{APP_NAME}/ && sudo docker image build --rm -t {DOCKER_IMAGE}:{DOCKER_TAG} -f Dockerfile .",
        f"sudo docker run -p 5000:5000 -d --restart unless-stopped {DOCKER_IMAGE}:{DOCKER_TAG}"
        ],
    get_pty=True,
    sudo=True
)

files.put(
    name='Copy nginx conf',
    src='./templates/nginx.conf',
    dest='/etc/nginx/sites-available/app.conf',
    sudo=True,
)

server.shell(
    name='Run nginx conf',
    commands=[
        "sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/",
        "sudo systemctl restart nginx",
        ],
    sudo=True
)
