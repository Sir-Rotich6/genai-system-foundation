import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(command)}\nError: {e}")
        sys.exit(1)

# Uninstall the 'anthropic' package (if you want a clean install)
print("Uninstalling 'anthropic'...")
run_command([sys.executable, "-m", "pip", "uninstall", "-y", "anthropic"])

# Install the specific version of 'anthropic'
print("Installing 'anthropic' version 0.19.0...")
run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "anthropic==0.19.0"])

# Verify the installation
try:
    import anthropic
    print(f"'anthropic' version {anthropic.__version__} is installed.")
except ImportError:
    print("Failed to import the 'anthropic' library after installation.")
    sys.exit(1)
