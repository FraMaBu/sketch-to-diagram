# app/utils.py
import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def encode_image(image_file):
    """Encode uploaded image to base64"""
    try:
        return base64.b64encode(image_file.getvalue()).decode("utf-8")
    except Exception as e:
        raise Exception(f"Error encoding image: {str(e)}")


def process_image_with_openai(image_file, prompt):
    """Process image using OpenAI's Vision API"""
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Encode image
        base64_image = encode_image(image_file)

        # Prepare messages with image and prompt
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ]

        # Make API call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1000,
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"Error processing image with OpenAI: {str(e)}")


def apply_style_to_mermaid(draft_code, style_prompt):
    """Apply styling to Mermaid code without sending image again"""
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Prepare messages with draft code and style prompt
        messages = [
            {
                "role": "user",
                "content": f"{style_prompt}\n\nHere's the Mermaid.js code to style:\n{draft_code}",
            }
        ]

        # Make API call using standard GPT-4
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            max_tokens=1000,
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"Error styling Mermaid code: {str(e)}")
