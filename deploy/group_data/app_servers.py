import os

ssh_port = 2000 # for vagrant change port tp 2222
ssh_user = 'senhaj' # for vagrant change user to 'vagrant'
ssh_key = os.path.join(os.path.expanduser('~'), '.ssh/id_rsa')

# if you are using VM with virtual box and vagrant, once you created your VM with Vagrantfile use this assignation of ssh_key
# ssh_key=os.path.join(
#   os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#   ,'.vagrant/machines/default/virtualbox/private_key'
#   )
