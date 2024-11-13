"""Helper functions for image processing and OpenAI API interactions."""

import base64
import os
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


def encode_image(image_file) -> str:
    """Encode uploaded image to base64."""
    try:
        return base64.b64encode(image_file.getvalue()).decode("utf-8")
    except Exception as e:
        raise Exception(f"Error encoding image: {str(e)}")


def process_image_with_openai(image_file, prompt: str) -> str:
    """Process image using OpenAI's Vision API to generate Mermaid diagram code."""
    try:
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


def apply_style_to_mermaid(draft_code: str, prompt: str, guide: str) -> str:
    """Apply styling to Mermaid code using OpenAI."""
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Prepare messages with style guide as system message and draft code in prompt
        messages = [
            {"role": "system", "content": guide},
            {"role": "user", "content": prompt.format(mermaid_code=draft_code)},
        ]

        # Make API call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1000,
            temperature=0,  # Strict responses
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"Error styling Mermaid code: {str(e)}")
