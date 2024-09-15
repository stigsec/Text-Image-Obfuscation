import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import os

#####VARIABLES#####
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
KEY_IMAGE_NAME = "key.png"
DEFAULT_TEXT_IMAGE_FORMAT = "png"
DEFAULT_OUTPUT_IMAGE_FORMAT = "png"

#####ENCRYPTION AND DECRYPTION FUNCTIONS#####
def create_random_image(width, height):
    random_pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return Image.fromarray(random_pixels, 'RGB')

def make_white_background_transparent(image):
    image = image.convert('RGBA')
    pixels = np.array(image)
    white_pixels = (pixels[:, :, 0] == 255) & (pixels[:, :, 1] == 255) & (pixels[:, :, 2] == 255)
    pixels[white_pixels] = (0, 0, 0, 0)
    return Image.fromarray(pixels, 'RGBA')

def replace_black_pixels_with_random(image):
    pixels = np.array(image)
    black_pixels = (pixels[:, :, 0] == 0) & (pixels[:, :, 1] == 0) & (pixels[:, :, 2] == 0) & (pixels[:, :, 3] > 0)
    random_colors = np.random.randint(0, 256, (pixels[black_pixels].shape[0], 3), dtype=np.uint8)
    pixels[black_pixels, :3] = random_colors
    return Image.fromarray(pixels, 'RGBA')

def overlay_images(base_image, overlay_image):
    return Image.alpha_composite(base_image.convert("RGBA"), overlay_image)

def encrypt_image(text_image_path, key_image, output_image_path="message.png"):
    text_image = Image.open(text_image_path)
    width, height = text_image.size

    key_image = key_image.resize((width, height))
    
    transparent_text_image = make_white_background_transparent(text_image)
    colored_text_image = replace_black_pixels_with_random(transparent_text_image)
    
    final_image = overlay_images(key_image, colored_text_image)
    final_image.save(output_image_path)

    return output_image_path

def decrypt_image(encrypted_image_path, key_image_path, output_image_path='decrypted.png'):
    encrypted_image = Image.open(encrypted_image_path).convert('RGBA')
    key_image = Image.open(key_image_path).convert('RGBA')

    if encrypted_image.size != key_image.size:
        raise ValueError("The encrypted image and the key image must have the same dimensions.")

    encrypted_pixels = np.array(encrypted_image)
    key_pixels = np.array(key_image)
    
    decrypted_pixels = np.zeros_like(encrypted_pixels)

    differences = (encrypted_pixels != key_pixels).any(axis=-1)

    decrypted_pixels[differences] = [0, 0, 0, 255]
    decrypted_pixels[~differences] = [255, 255, 255, 255]

    decrypted_image = Image.fromarray(decrypted_pixels, 'RGBA')
    decrypted_image.save(output_image_path)
    
    return output_image_path

#####GUI#####
class TIO:
    def __init__(self, root):
        self.root = root
        self.root.title("T.I.O v1 by stigs")
        
        #####DEFALT RESOLUTION#####
        self.output_width = DEFAULT_WIDTH
        self.output_height = DEFAULT_HEIGHT
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Text Image Obfuscation", font=("Arial", 16)).pack(pady=10)

        #####SETTINGS#####
        self.settings_frame = tk.LabelFrame(self.root, text="Settings", padx=10, pady=10)
        self.settings_frame.pack(padx=10, pady=5)

        tk.Label(self.settings_frame, text="Width:").pack(side=tk.LEFT)
        self.width_entry = tk.Entry(self.settings_frame, width=5)
        self.width_entry.pack(side=tk.LEFT)
        self.width_entry.insert(0, str(self.output_width))

        tk.Label(self.settings_frame, text="Height:").pack(side=tk.LEFT, padx=5)
        self.height_entry = tk.Entry(self.settings_frame, width=5)
        self.height_entry.pack(side=tk.LEFT)
        self.height_entry.insert(0, str(self.output_height))

        #####APPLY SETTINGS BUTTON#####
        self.apply_settings_button = tk.Button(self.settings_frame, text="Apply Settings", command=self.apply_settings)
        self.apply_settings_button.pack(side=tk.LEFT, padx=10)

        #####ENCRYPT SECTION#####
        self.encrypt_frame = tk.LabelFrame(self.root, text="Encrypt", padx=10, pady=10)
        self.encrypt_frame.pack(padx=10, pady=5)

        self.btn_select_text_images = tk.Button(self.encrypt_frame, text="Select Images", command=self.load_text_images)
        self.btn_select_text_images.pack(side=tk.LEFT)

        self.btn_encrypt = tk.Button(self.encrypt_frame, text="Encrypt", command=self.encrypt_action, state=tk.DISABLED)
        self.btn_encrypt.pack(side=tk.LEFT, padx=5)

        #####DECRYPT SECTION#####
        self.decrypt_frame = tk.LabelFrame(self.root, text="Decrypt", padx=10, pady=10)
        self.decrypt_frame.pack(padx=10, pady=5)

        self.btn_select_encrypted_images = tk.Button(self.decrypt_frame, text="Select Encrypted Images", command=self.load_encrypted_images)
        self.btn_select_encrypted_images.pack(side=tk.LEFT)

        self.btn_select_key_image = tk.Button(self.decrypt_frame, text="Select Key Image", command=self.load_key_image)
        self.btn_select_key_image.pack(side=tk.LEFT, padx=5)

        self.btn_decrypt = tk.Button(self.decrypt_frame, text="Decrypt", command=self.decrypt_action, state=tk.DISABLED)
        self.btn_decrypt.pack(side=tk.LEFT, padx=5)

    def apply_settings(self):
        try:
            self.output_width = int(self.width_entry.get())
            self.output_height = int(self.height_entry.get())
            messagebox.showinfo("Success", "Resolution updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for width and height.")

    def load_text_images(self):
        self.text_image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.text_image_paths:
            self.btn_encrypt.config(state=tk.NORMAL)

    def load_encrypted_images(self):
        self.encrypted_image_paths = filedialog.askopenfilenames(title="Select Encrypted Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.encrypted_image_paths and hasattr(self, 'key_image_path'):
            self.btn_decrypt.config(state=tk.NORMAL)

    def load_key_image(self):
        self.key_image_path = filedialog.askopenfilename(title="Select Key Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.key_image_path and hasattr(self, 'encrypted_image_paths'):
            self.btn_decrypt.config(state=tk.NORMAL)

    def encrypt_action(self):
        try:
            if not self.text_image_paths:
                messagebox.showerror("Error", "No images selected!")
                return

            first_image = Image.open(self.text_image_paths[0])
            key_image = create_random_image(self.output_width, self.output_height)
            key_image.save(KEY_IMAGE_NAME)  #####SAVING THE KEY#####

            output_paths = []
            for i, text_image_path in enumerate(self.text_image_paths, 1):
                output_image_path = f"message_{i}.{DEFAULT_OUTPUT_IMAGE_FORMAT}"
                encrypt_image(text_image_path, key_image, output_image_path=output_image_path)
                output_paths.append(output_image_path)

            messagebox.showinfo("Success", f"Encryption complete!\nImages: {', '.join(output_paths)}\nKey Image: {KEY_IMAGE_NAME}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_action(self):
        try:
            if not self.encrypted_image_paths:
                messagebox.showerror("Error", "No encrypted images selected!")
                return

            output_paths = []
            for i, encrypted_image_path in enumerate(self.encrypted_image_paths, 1):
                output_image_path = f"decrypted_{i}.{DEFAULT_OUTPUT_IMAGE_FORMAT}"
                decrypt_image(encrypted_image_path, self.key_image_path, output_image_path=output_image_path)
                output_paths.append(output_image_path)

            messagebox.showinfo("Success", f"Decryption complete!\nDecrypted Images: {', '.join(output_paths)}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TIO(root)
    root.mainloop()
