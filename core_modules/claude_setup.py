# Import libraries
import claude
import os
from google.colab import userdata

# Function to initialize the Claude API key
def initialize_claude_api():
    # Access the secret by its name
    API_KEY = userdata.get('API_KEY')
    
    if not API_KEY:
        raise ValueError("API_KEY is not set in userdata!")
    
    # Set the API key in the environment and Claude
    os.environ['CLAUDE_API_KEY'] = API_KEY
    claude.api_key = os.getenv("CLAUDE_API_KEY")
    print("Claude API key initialized successfully.")
