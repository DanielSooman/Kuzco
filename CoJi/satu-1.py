import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker stI6ciAOuWtKep8k_gysT --code aed8abba-5687-4b54-9097-6ec9c6f058ce"
subprocess.run(worker_command, shell=True, check=True)
