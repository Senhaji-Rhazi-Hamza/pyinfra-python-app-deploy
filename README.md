# pyinfra-python-app-deploy
This project aims to show how you can deploy production ready a python app using the wonderful library pyinfra

## Usage

### 1. Setup your VM
```bash
# Assuming you have virtualbox already installed, using the vagrant file at the root directory run the command at the root directory

vagrant up
```

### 2. deploy your app 


```bash
# Assuming you have installed pyinfra (pip install pyinfra) & you have replaced variables in deploy/group_data/app_servers.py with yours.

# Execute the command :

pyinfra inventories/staging.py setup_server.py
```

### More refs : 
<br>

You can find a complete explanation in this [medium article](https://hamza-senhajirhazi.medium.com/deploy-your-python-app-on-remote-server-with-pyinfra-42753ada37ca) 

You can also find a complete demo in this [youtube video](https://www.youtube.com/watch?v=cCXHx7j6yeU)