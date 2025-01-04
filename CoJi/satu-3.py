import subprocess

subprocess.run("apt-get update -y", shell=True, check=True)
subprocess.run("apt-get install -y curl libcurl4", shell=True, check=True)

install_command = "curl -fsSL https://kuzco.xyz/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker lx6zro5_BkOMApF9H_nTZ --code 5d3d0d94-cd6f-4fe2-8d94-4048b74c3b78"
subprocess.run(worker_command, shell=True, check=True)
