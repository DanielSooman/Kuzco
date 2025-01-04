import subprocess

subprocess.run("apt-get update -y", shell=True, check=True)
subprocess.run("apt-get install -y curl libcurl4", shell=True, check=True)

install_command = "curl -fsSL https://kuzco.xyz/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker khEYwVlxk1UZdHnP3dv-z --code 62f49510-bb67-4ef3-8653-f465d1e0246f"
subprocess.run(worker_command, shell=True, check=True)
