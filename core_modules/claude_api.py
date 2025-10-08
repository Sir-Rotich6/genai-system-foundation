import anthropic
import base64
import os

# Initialize the Claude client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def make_claude_api_call(input, mrole, mcontent, user_role):
    # Define parameters
    cmodel = "claude-3-5-sonnet-latest"  # Example model, update as needed

    # Create the messages object
    messages_obj = [
        {
            "role": mrole,
            "content": mcontent
        },
        {
            "role": user_role,
            "content": input
        }
    ]

    # Define all parameters in a dictionary
    params = {
        "max_tokens": 1024,
        "temperature": 0,
        "top_p": 1,
        # Claude does not use frequency_penalty or presence_penalty
    }

    # Make the API call
    response = client.messages.create(
        model=cmodel,
        messages=messages_obj,
        **params
    )

    # Return the response
    return response.content

def image_analysis(image_path_or_url, query_text, model="claude-3-5-sonnet-latest"):
    """
    Analyze an image using Claude's vision-capable model.

    Args:
        image_path_or_url (str): Path to a local image file or URL of the image.
        query_text (str): The query related to the image.
        model (str): The Claude model to use. Defaults to "claude-3-5-sonnet-latest".

    Returns:
        str: The analysis result from the model.
    """
    # Initialize the content list with the query text
    content = [{"type": "text", "text": query_text}]

    if image_path_or_url.startswith(("http://", "https://")):
        # It's a URL; add it to the content
        content.append({"type": "image_url", "image_url": {"url": image_path_or_url}})
    else:
        # It's a local file; read and encode the image data
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        # Create a data URL for the image
        data_url = f"data:image/png;base64,{image_data}"
        content.append({"type": "image_url", "image_url": {"url": data_url}})

    # Create the message object
    messages = [{"role": "user", "content": content}]

    # Define the parameters
    params = {
        "max_tokens": 300,
        "temperature": 0,
        "top_p": 1,
    }

    # Make the API call
    response = client.messages.create(
        model=model,
        messages=messages,
        **params
    )

    # Return the response content
    return response.content

def generate_image(prompt, model="claude-3-5-sonnet-latest", size="1024x1024", quality="standard", n=1):
    """
    Function to generate an image using Claude's image generation API.

    Args:
        prompt (str): The prompt describing the image to generate.
        model (str): The Claude model to use for image generation.
        size (str): The size of the generated image.
        quality (str): The quality of the generated image.
        n (int): The number of images to generate.

    Returns:
        str: The URL of the generated image.
    """
    # Claude's API for image generation may differ; this is a placeholder
    # If Claude supports image generation, use the correct endpoint and parameters
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=n,
    )

    # Extract and return the image URL from the response
    return response.data[0].url
