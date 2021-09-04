from pyinfra.operations import apt

apt.packages(
    name='Ensure docker is installed',
    packages=['docker'],
    sudo=True,
    update=True,
)
