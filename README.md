T.I.O. v1 - Text Image Obfuscation by Stigs
Overview
T.I.O. (Text Image Obfuscation) is a Python-based application that allows users to encrypt and decrypt images using a form of steganography. The application leverages random pixel generation to create an encryption key image, and overlays an obfuscated text image on top of it. The application also provides an easy-to-use graphical user interface (GUI) for managing encryption and decryption workflows. The encrypted image can then be decrypted using the same key image to reveal the obfuscated text.

This tool is useful for hiding messages or sensitive information inside images in a visually non-obvious manner.

Features
Encrypt Images: Select any image containing text, and encrypt it with a randomly generated key image.
Decrypt Images: Use the previously generated key image to reveal the hidden message.
GUI: The application comes with a simple and intuitive GUI created with tkinter.
Randomized Encryption: Each encryption generates a unique key, ensuring that the output is distinct even when the same text image is used multiple times.
Customizable Resolution: Users can set custom width and height for the output image resolution.
How it Works
Encryption:
You provide a text image (or images), and the app generates a random key image.
The white background of the text image is made transparent, and the black pixels are replaced with random colors.
The key image is then used as the base to overlay the modified text image, producing an encrypted image.
The key image is saved as key.png and the encrypted images are saved in the current directory.
Decryption:
To decrypt an image, the encrypted image and the corresponding key image must have the same dimensions.
The app compares the encrypted image with the key image, revealing the hidden text by displaying it as black pixels on a white background.
The decrypted image is saved in the current directory.
Dependencies
Python 3.x
numpy
Pillow
tkinter (included in the standard Python library)
To install the necessary dependencies, you can use the following command:

bash
Copy code
pip install numpy pillow
Usage Instructions
Running the Application
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/tio-obfuscation.git
cd tio-obfuscation
Run the TIO.py script:

bash
Copy code
python TIO.py
Application Workflow
Encryption
Open the app.
Under the "Settings" section, set the desired output resolution (width and height). Click "Apply Settings" to save changes.
In the "Encrypt" section, click "Select Images" to choose one or more text images for encryption.
After selecting the text images, click "Encrypt" to begin the encryption process.
The app will generate a key.png file and save the encrypted images as message_1.png, message_2.png, etc.
A message box will inform you of the success of the operation and provide details on the output files.
Decryption
Open the app.
In the "Decrypt" section, click "Select Encrypted Images" to choose one or more previously encrypted images.
Click "Select Key Image" to choose the key.png file generated during encryption.
Once the encrypted images and key are selected, click "Decrypt" to reveal the hidden text.
The decrypted images will be saved as decrypted_1.png, decrypted_2.png, etc.
Project Structure
TIO.py: Main script containing the encryption, decryption logic, and the GUI implementation.
key.png: The generated key image file (after encryption).
message_1.png, message_2.png, etc.: The encrypted images (output).
decrypted_1.png, decrypted_2.png, etc.: The decrypted images (output).
Customization
You can modify the following default settings within the script:

DEFAULT_WIDTH: Default output image width (set to 1280).
DEFAULT_HEIGHT: Default output image height (set to 720).
KEY_IMAGE_NAME: Name of the key image file (default is key.png).
DEFAULT_TEXT_IMAGE_FORMAT: Format of the text image (set to png).
DEFAULT_OUTPUT_IMAGE_FORMAT: Format of the encrypted and decrypted output images (set to png).
Error Handling
The application ensures that the encrypted image and the key image must have the same dimensions for successful decryption.
If the wrong image files are selected, an error message will be displayed.
It provides feedback in case of incorrect width/height inputs or missing files during encryption and decryption processes.
Future Improvements
Allow selection of different output formats (e.g., JPEG, BMP).
Add batch processing for multiple images.
Improve encryption robustness by adding additional layers of encryption.
Option to save settings or load previously used resolutions.
License
This project is licensed under the MIT License.

Author: Stigs
Version: 1.0
Date: September 2024