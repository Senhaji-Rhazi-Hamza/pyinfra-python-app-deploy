from pyinfra.operations import apt

apt.packages(
    name='Ensure nginx is installed',
    packages=['nginx'],
    sudo=True,
    update=True,
)


