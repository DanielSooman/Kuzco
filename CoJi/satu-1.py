import subprocess

def update_and_install_dependencies():
    try:
        print("Updating package index...")
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)
        print("Installing curl and libcurl4...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "curl", "libcurl4"], check=True)
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during dependency installation: {e}")
        raise

def run_install_script():
    try:
        print("Running Kuzco installation script...")
        subprocess.run(["curl", "-fsSL", "https://kuzco.xyz/install.sh"], check=True)
        subprocess.run(["sudo", "sh"], check=True)
        print("Installation script executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Kuzco installation: {e}")
        raise

def start_kuzco_worker():
    try:
        print("Starting Kuzco worker...")
        worker_command = [
            "sudo", "kuzco", "worker", "start",
            "--worker", "stI6ciAOuWtKep8k_gysT",
            "--code", "aed8abba-5687-4b54-9097-6ec9c6f058ce"
        ]
        result = subprocess.run(worker_command, capture_output=True, text=True, check=True)
        print("Kuzco worker started successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while starting Kuzco worker: {e}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Stderr: {e.stderr}")
        raise

if __name__ == "__main__":
    try:
        update_and_install_dependencies()
        run_install_script()
        start_kuzco_worker()
        print("All steps completed successfully!")
    except Exception as e:
        print(f"Script failed with error: {e}")
