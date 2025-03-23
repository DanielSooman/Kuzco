import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker lx6zro5_BkOMApF9H_nTZ --code 5d3d0d94-cd6f-4fe2-8d94-4048b74c3b78"
subprocess.run(worker_command, shell=True, check=True)
