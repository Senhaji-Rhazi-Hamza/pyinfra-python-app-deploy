import os
ssh_port = 2222
ssh_user = 'vagrant'
ssh_key=os.path.join(
  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  ,'.vagrant/machines/default/virtualbox/private_key'
  )
