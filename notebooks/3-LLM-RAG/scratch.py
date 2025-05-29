import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"

api_key = os.getenv("NVIDIA_API_KEY")
if not api_key or not api_key.startswith("nvapi-"):
    raise ValueError("NVIDIA_API_KEY not found or invalid in .env file.")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json",
}

payload = {
    "text_prompts": [
        {
            "text": "underwater world, plants, shells, creatures, high detail, sharp focus, 4k",
            "weight": 1
        },
        {
            "text": "",
            "weight": -1
        }
    ],
    "cfg_scale": 5,
    "sampler": "K_DPM_2_ANCESTRAL",
    "seed": 0,
    "steps": 25
}

response = requests.post(invoke_url, headers=headers, json=payload)
response.raise_for_status()
response_body = response.json()

# Extract and decode the base64 image
image_base64 = response_body['artifacts'][0]['base64']

# Save to file
with open("underwater_scene.png", "wb") as f:
    f.write(base64.b64decode(image_base64))

print("Image saved as 'underwater_scene.png'")