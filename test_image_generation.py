import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def test_generate_image_4k():
    description = "Narendra Modi"
    response = requests.post(f"{BASE_URL}/generate", json={"description": description})
    assert response.status_code == 200
    image_url = response.json().get("image_url")
    assert image_url is not None

    # Verify the image resolution
    image_response = requests.get(image_url)
    assert image_response.status_code == 200
    with open("generated_image_4k.png", "wb") as f:
        f.write(image_response.content)
    from PIL import Image
    image = Image.open("generated_image_4k.png")
    assert image.size == (3840, 2160)

def test_generate_image_2k():
    description = "Narendra Modi"
    response = requests.post(f"{BASE_URL}/generate", json={"description": description})
    assert response.status_code == 200
    image_url = response.json().get("image_url")
    assert image_url is not None

    # Verify the image resolution
    image_response = requests.get(image_url)
    assert image_response.status_code == 200
    with open("generated_image_2k.png", "wb") as f:
        f.write(image_response.content)
    from PIL import Image
    image = Image.open("generated_image_2k.png")
    assert image.size == (2560, 1440)
