import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker vBeNhW2MTYZwWbJRx94Ho --code 568dd654-cf57-4a92-a768-1ba4b892b9e7"
subprocess.run(worker_command, shell=True, check=True)
