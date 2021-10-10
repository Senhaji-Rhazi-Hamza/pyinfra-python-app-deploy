from pyinfra.operations import apt
from pyinfra.operations import server


apt.packages(
    name='Ensure nginx is installed',
    packages=['nginx'],
    sudo=True,
    update=True,
)


server.shell(
    name='Reload nginx to ensure it has started',
    commands=['nginx -s reload'],
    sudo=True,
)
