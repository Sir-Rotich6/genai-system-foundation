import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(command)}\nError: {e}")
        sys.exit(1)

# Uninstall the 'openai' package
print("Uninstalling 'openai'...")
run_command([sys.executable, "-m", "pip", "uninstall", "-y", "openai"])

# Install the specific version of 'openai'
print("Installing 'openai' version 1.57.1...")
run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "openai==1.57.1"])

# Verify the installation
try:
    import openai
    print(f"'openai' version {openai.__version__} is installed.")
except ImportError:
    print("Failed to import the 'openai' library after installation.")
    sys.exit(1)
