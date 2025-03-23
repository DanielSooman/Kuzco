import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker J5nbT8KHPCchGthS0HnP8 --code 4e71c20a-7e98-44a0-a3e9-4823b3661786"
subprocess.run(worker_command, shell=True, check=True)
