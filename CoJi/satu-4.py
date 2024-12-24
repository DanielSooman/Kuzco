import subprocess

# Fix libcurl version issue
subprocess.run("apt-get update -y", shell=True, check=True)
subprocess.run("apt-get install -y curl libcurl4", shell=True, check=True)

# Step 1: Run the first command using curl to install
install_command = "curl -fsSL https://kuzco.xyz/install.sh | sh"
subprocess.run(install_command, shell=True, check=True)

# Step 2: Run the second command to start the Kuzco worker
worker_command = "kuzco worker start --worker lc7k3CXN7j7PGdkS0O61A --code f2aa4e50-65da-4cc4-be0e-7098268595b9"
subprocess.run(worker_command, shell=True, check=True)
