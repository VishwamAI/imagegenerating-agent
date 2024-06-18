import requests
import pytest

BASE_URL = "https://783e-2600-1f14-db0-ba00-bdaa-76cd-8c2f-8339.ngrok-free.app"

def test_generate_image_4k():
    description = "Narendra Modi"
    response = requests.post(f"{BASE_URL}/generate", json={"description": description})
    print(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    image_url = response.json().get("image_url")
    print(f"Image URL: {image_url}")
    assert image_url is not None

    # Verify the image resolution
    image_response = requests.get(f"{BASE_URL}{image_url}")
    print(f"Image response status code: {image_response.status_code}")
    assert image_response.status_code == 200
    with open("generated_image_4k.png", "wb") as f:
        f.write(image_response.content)
    from PIL import Image
    image = Image.open("generated_image_4k.png")
    print(f"Image size: {image.size}")
    assert image.size == (3840, 2160)

def test_generate_image_2k():
    description = "Narendra Modi"
    response = requests.post(f"{BASE_URL}/generate", json={"description": description})
    print(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    image_url = response.json().get("image_url")
    print(f"Image URL: {image_url}")
    assert image_url is not None

    # Verify the image resolution
    image_response = requests.get(f"{BASE_URL}{image_url}")
    print(f"Image response status code: {image_response.status_code}")
    assert image_response.status_code == 200
    with open("generated_image_2k.png", "wb") as f:
        f.write(image_response.content)
    from PIL import Image
    image = Image.open("generated_image_2k.png")
    print(f"Image size: {image.size}")
    assert image.size == (2560, 1440)
