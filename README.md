# PRODIGY_CS_02
# Pixel Manipulation for Image Encryption

This is a simple image encryption tool that uses pixel manipulation to encrypt and decrypt images.

## Features

- Encrypt image by adding a key value to each pixel.
- Decrypt image by subtracting the same key value.
- User-friendly GUI using Tkinter.
- Supports PNG, JPG, JPEG formats.

## How to Run

1. Make sure you have Python installed.
2. Install dependencies:
    ```bash
    pip install pillow numpy
    ```
3. Run the application:
    ```bash
    python main.py
    ```

## Usage

- Enter a numerical key (e.g., 50).
- Click "Encrypt Image" to choose and encrypt an image.
- Click "Decrypt Image" to revert the encryption using the same key.
