import requests
import pytest
import responses

BASE_URL = "http://dummy-url.com"

@responses.activate
def test_generate_image_4k():
    input_text = "Narendra Modi"
    responses.add(
        responses.POST,
        f"{BASE_URL}/generate_image",
        json={"image_url": "/generated_image_4k.png"},
        status=200
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/generated_image_4k.png",
        body=open("test_images/generated_image_4k.png", "rb").read(),
        status=200,
        content_type="image/png"
    )

    response = requests.post(f"{BASE_URL}/generate_image", json={"input_text": input_text})
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

@responses.activate
def test_generate_image_2k():
    input_text = "Narendra Modi"
    responses.add(
        responses.POST,
        f"{BASE_URL}/generate_image",
        json={"image_url": "/generated_image_2k.png"},
        status=200
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/generated_image_2k.png",
        body=open("test_images/generated_image_2k.png", "rb").read(),
        status=200,
        content_type="image/png"
    )

    response = requests.post(f"{BASE_URL}/generate_image", json={"input_text": input_text})
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
