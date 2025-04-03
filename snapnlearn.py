'''
    Welcome to the snapnlearn.py!
     
       This is a simple Streamlit web app that allows users to submit a photo to be analyzed.
       This tool leverage's OpenAI's Vision capabilities which can receive both text and images as
       prompts. OpenAI's Vision API is accessed with the 'gpt-4o-mini' model here but can also be
       accessed via OpenAI's '01', 'gpt-4o', and 'gpt-4-turbo' models.
       
       Streamlit is an open-source Python library which allows users to quickly and easily
       build Python web applications. While you are running a Streamlit web app locally:
       any changes you make and save to your Python code-base will reflect *live* on your app.

       This tool builds an API request containing a pre-defined text-prompt alongside a user-uploaded
       image to OpenAI's Vision API and receives an analysis of the image as json formatted text.

       TODO Leverage Streamlit's side menu capabilites to allow users to input their own text-prompt
       alonside their image. Include other pre-defined text-prompts that allow users to, for example,
       search online stores for the provided image.

       TODO Incorporate OAUTH 2.0 to allow for granular control over access to the tool. Streamlit
       supports OAUTH 2.0. Youtube guide.
       
    Finally, a "method" in Python is a "function" in most other programming languages. I will
    be referrering to them as functions.

'''

# Import libraries
import streamlit as st         # The streamlit library allows for quick and easy app development
import requests                # The requests library streamlines the creation and handling of API requests
import io                      # This library deals with opening files
import os                      # Allows python to interact with the local file system
from dotenv import load_dotenv # Allows API key to be stored/retrieved from .env file
import base64                  # Allows for encoding base64
from PIL import Image          # Adds the Image class from pillow, which allows Python to handle images

# Initialize OPENAI API key (used to authenticate OpenAI API requests)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API key
if not OPENAI_API_KEY:
    st.error("OpenAI Key is missing. Please provide a valid key.")
    st.stop()   # Stops the rest of the app from running

# A function that analyzes a user-provided image.
# - Leverages OpenAI's Vision API and Python's 'requests' library
# - Requires an image as an argument
# - Returns the response from OpenAI as a string.
def analyze_photo(image):
    
    # Convert image into bytes then encode to base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Prepare the API request by initializing the header with our API key.
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Initialize api_url to OpenAI API endpoint for GPT-4 with Vision.
    api_url = "https://api.openai.com/v1/chat/completions"
    #api_url = "https://api.deepseek.com/v1/chat/completions"

    # Create the payload
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image? Explain with bullet points."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
                ]
            }
        ],
        "max_tokens": 300
    }
    
    # Make the API Request:
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"] # Returns a str from a dict
    except requests.exceptions.HTTPError as e:
        st.error(f"Failed to analyze the image: {e}")
    except Exception as e:
        st.error(f"An unnexpected error occurred: {e}")
    return None

# Main Function
# This function serves to structure and run the Streamlit app.
def main():

    # Title
    st.title("Welcome to SnapNLearn!")

    # Subtitle
    st.write(f'Upload an existing photo by selecting **Browse Files** or upload a \
             new photo by selecting **Take Photo** below')

    # Creates a widget that allows users to upload images.
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

    # Allow user to upload photo from their camera
    camera_file = st.camera_input("Or take a photo")

    # Determine which image to use
    image = None
    try:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
        elif camera_file is not None:
            image = Image.open(camera_file)
    except Exception as e:
        st.error(f"Failed to process image: {e}")
        image = None

    # Display the image if one is uploaded or taken
    if image is not None:
        st.image(image, caption = "Your photo")

        # Analyze the image after user clicks button
        if st.button("Analyze photo"):
            with st.spinner("Analyzing the image..."):
                analysis_result = analyze_photo(image)
                if analysis_result:
                    st.subheader("Analysis Result:")
                    st.success("Analysis complete!")
                    st.write(analysis_result)


# If name is equal to main: run the main function
if __name__ == "__main__":
    main()