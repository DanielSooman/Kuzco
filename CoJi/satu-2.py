import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker khEYwVlxk1UZdHnP3dv-z --code 62f49510-bb67-4ef3-8653-f465d1e0246f"
subprocess.run(worker_command, shell=True, check=True)
