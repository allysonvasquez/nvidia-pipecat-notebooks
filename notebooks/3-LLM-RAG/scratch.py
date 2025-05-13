import base64
import requests

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"

headers = {
    "Authorization": "Bearer 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",
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