import subprocess

subprocess.run("apt-get update -y", shell=True, check=True)
subprocess.run("apt-get install -y curl libcurl4", shell=True, check=True)

install_command = "curl -fsSL https://kuzco.xyz/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker stI6ciAOuWtKep8k_gysT --code aed8abba-5687-4b54-9097-6ec9c6f058ce"
subprocess.run(worker_command, shell=True, check=True)
