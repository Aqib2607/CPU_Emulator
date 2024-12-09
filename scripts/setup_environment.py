import os
import subprocess
import sys

def install_requirements():
    """Installs required dependencies listed in requirements.txt."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_virtualenv():
    """Sets up a virtual environment for the project."""
    subprocess.check_call([sys.executable, "-m", "venv", "env"])
    print("Virtual environment created successfully.")

if __name__ == "__main__":
    if not os.path.exists("env"):
        setup_virtualenv()
    install_requirements()
    print("Environment setup complete.")
