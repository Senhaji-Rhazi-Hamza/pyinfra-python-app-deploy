import os

ssh_port = 2000
ssh_user = 'senhaj'
ssh_key = os.path.join(os.path.expanduser('~'), '.ssh/id_rsa')

# if you are using VM with virtual box and vagrant, once you created your VM with Vagrantfile use this assignation of ssh_key
# ssh_key=os.path.join(
#   os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#   ,'.vagrant/machines/default/virtualbox/private_key'
#   )
