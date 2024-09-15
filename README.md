# T.I.O. v1 - Text Image Obfuscation by Stigs

## Overview
**T.I.O. (Text Image Obfuscation)** is a Python-based application that allows users to encrypt and decrypt images using a form of steganography. The application leverages random pixel generation to create an encryption key image and overlays an obfuscated text image on top of it. The encrypted image can then be decrypted using the same key image to reveal the hidden text. The application also provides an easy-to-use graphical user interface (GUI) for managing encryption and decryption workflows.

This tool is useful for hiding messages or sensitive information inside images in a visually non-obvious manner. But be aware that this **might not be entirely safe**.

## Features
- **Encrypt Images:** Select any image containing text and encrypt it with a randomly generated key image.
- **Decrypt Images:** Use the previously generated key image to reveal the hidden message.
- **GUI:** A simple and intuitive GUI created with `tkinter`.
- **Randomized Encryption:** Each encryption generates a unique key, ensuring the output is distinct even when the same text image is used multiple times.
- **Customizable Resolution:** Users can set custom width and height for the output image resolution.

## How it Works

### Encryption:
1. You provide a text image (or images), and the app generates a random key image.
2. The white background of the text image is made transparent, and the black pixels are replaced with random colors.
3. The key image is then used as the base to overlay the modified text image, producing an encrypted image.
4. The key image is saved as `key.png`, and the encrypted images are saved in the current directory.

### Decryption:
1. To decrypt an image, the encrypted image and the corresponding key image must have the same dimensions.
2. The app compares the encrypted image with the key image, revealing the hidden text by displaying it as black pixels on a white background.
3. The decrypted image is saved in the current directory.

## Dependencies
- **Python 3.x**
- **numpy**
- **Pillow**
- **tkinter** (included in the standard Python library)

To install the necessary dependencies, run the following command:

```bash
pip install numpy pillow
```
## Usage
```bash
git clone https://github.com/stigsec/Text-Image-Obfuscation.git
cd Text-Image-Obfuscation
```
Run the TIO.py script
```bash
python TIO.py
```
### Encryption
1. Run the script
2. Under the "Settings" section, set the desired output resolution (width and height). Click **Apply Settings** to save changes.
3. In the "Encrypt" section, click **Select Images** to choose one or more text images for encryption.
4. After selecting the text images, click **Encrypt** to begin the encryption process.
5. The app will generate a `key.png` file and save the encrypted images as `message_1.png`, `message_2.png`, etc.
6. A message box will confirm the success of the operation and provide details on the output files.

### Decryption
1. Run the script
2. In the "Decrypt" section, click **Select Encrypted Images** to choose one or more previously encrypted images.
3. Click **Select Key Image** to choose the `key.png` file generated during encryption.
4. Once the encrypted images and key are selected, click **Decrypt** to reveal the hidden text.
5. The decrypted images will be saved as `decrypted_1.png`, `decrypted_2.png`, etc.

## Customization
You can modify the following default settings within the script:
- `DEFAULT_WIDTH`: Default output image width (set to 1280).
- `DEFAULT_HEIGHT`: Default output image height (set to 720).
- `KEY_IMAGE_NAME`: Name of the key image file (default is key.png).
- `DEFAULT_TEXT_IMAGE_FORMAT`: Format of the text image (set to png).
- `DEFAULT_OUTPUT_IMAGE_FORMAT`: Format of the encrypted and decrypted output images (set to png).

## Error Handling
- The application ensures that the encrypted image and the key image must have the same dimensions for successful decryption.
- If the wrong image files are selected, an error message will be displayed.
- It provides feedback in case of incorrect width/height inputs or missing files during encryption and decryption processes.

## License
T.I.O (Text Image Obfuscation) is released uunder the MIT license. See [LICENSE](LICENSE)
