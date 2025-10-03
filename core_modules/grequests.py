import subprocess
import os

def download(directory, filename):
    # The base URL for your repository's raw files
    base_url = 'https://raw.githubusercontent.com/Sir-Rotich6/genai-system-foundation/main/'
    
    # Construct the full URL for the file
    file_url = f"{base_url}{directory}/{filename}"
    
    try:
        # Prepare and execute the curl command
        curl_command = f'curl -o {filename} {file_url}'
        subprocess.run(curl_command, check=True, shell=True)
        print(f"Downloaded '{filename}' successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to download '{filename}'. Check the URL and your internet connection.")

