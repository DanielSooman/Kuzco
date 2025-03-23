import subprocess

install_command = "curl -fsSL https://inference.supply/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

worker_command = "kuzco worker start --worker lc7k3CXN7j7PGdkS0O61A --code f2aa4e50-65da-4cc4-be0e-7098268595b9"
subprocess.run(worker_command, shell=True, check=True)
