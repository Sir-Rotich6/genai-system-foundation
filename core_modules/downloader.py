# core_modules/downloader.py

import subprocess
import os

def download(directory, filename, base_url='https://raw.githubusercontent.com/Sir-Rotich6/genai-system-foundation/main/'):
    file_url = f"{base_url}{directory}/{filename}"
    try:
        curl_command = f'curl -o {filename} {file_url}'
        subprocess.run(curl_command, check=True, shell=True)
        print(f"Downloaded '{filename}' successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to download '{filename}'. Check the URL and your internet connection.")
