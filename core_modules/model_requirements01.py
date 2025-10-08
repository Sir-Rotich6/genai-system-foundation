import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(command)}\nError: {e}")
        sys.exit(1)

# Uninstall the 'claude' package
print("Uninstalling 'claude'...")
run_command([sys.executable, "-m", "pip", "uninstall", "-y", "claude"])

# Install the specific version of 'claude'
print("Installing 'claude' version 1.57.1...")
run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "claude==1.57.1"])

# Verify the installation
try:
    import claude
    print(f"'claude' version {claude.__version__} is installed.")
except ImportError:
    print("Failed to import the 'claude' library after installation.")
    sys.exit(1)
