import openai
import requests
from io import BytesIO
from PIL import Image


openai.api_key = "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"

# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url'] # type: ignore


def avatar(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256'
    )

    # Convert the image data to a Pillow image object

    img_data = requests.get(response['data'][0]['url']).content
    return response
    
# avatar("2D monkey avatar with goggles,jewellery, cap and hoodie")