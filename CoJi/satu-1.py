import subprocess

try:
    # Fix libcurl version issue
    subprocess.run("sudo apt-get update -y", shell=True, check=True)
    subprocess.run("sudo apt-get install -y curl libcurl4", shell=True, check=True)

    # Step 1: Run the first command using curl to install
    install_command = "curl -fsSL https://kuzco.xyz/install.sh | sudo sh"
    subprocess.run(install_command, shell=True, check=True)

    # Step 2: Run the second command to start the Kuzco worker
    worker_command = "sudo kuzco worker start --worker stI6ciAOuWtKep8k_gysT --code aed8abba-5687-4b54-9097-6ec9c6f058ce"
    subprocess.run(worker_command, shell=True, check=True)
    
    print("Commands executed successfully!")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
    raise
