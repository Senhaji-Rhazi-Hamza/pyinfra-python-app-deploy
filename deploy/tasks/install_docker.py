from pyinfra import host
from pyinfra.operations import apt
from pyinfra.operations import server
from pyinfra.facts.server import Arch




def get_arch_name():
    arch = host.get_fact(Arch)
    if arch == 'aarch64' or arch == 'arm64':
        return 'arm64'
    else:
        return 'amd64'



server.shell(
    name='Install docker',
    commands=[
        "sudo dpkg  --remove docker docker-engine docker.io containerd runc",
        "apt-get update -y",
         "apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg > gpgkey",
        "cat gpgkey | sudo gpg  --batch --yes --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg ",
        # you should choose the right arch for your target machine : https://docs.docker.com/engine/install/ubuntu/
        f'echo "deb [arch={get_arch_name()} signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null',
        "apt-get update -y",
        "apt-get install docker-ce docker-ce-cli containerd.io -y"
    ],
    get_pty=True,
    sudo=True
)
