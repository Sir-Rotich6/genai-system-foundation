# If `download` is in core_modules/downloader.py, import it:
import sys
sys.path.append('../core_modules')  # Adapt path as needed
from downloader import download

# Use the function to download a file:
download('core_modules', 'downloader.py')
