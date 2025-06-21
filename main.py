from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Store key for decryption
key_array = None

# Generate a reproducible random key for XOR
def generate_key_array(shape, seed):
    np.random.seed(seed)
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

# Encrypt using XOR operation
def encrypt_image(image_path, seed):
    global key_array
    img = Image.open(image_path).convert("RGB")  # Ensure 3 channels
    arr = np.array(img, dtype=np.uint8)
    key_array = generate_key_array(arr.shape, seed)
    encrypted = np.bitwise_xor(arr, key_array)
    encrypted_img = Image.fromarray(encrypted)
    save_path = os.path.splitext(image_path)[0] + "_encrypted.png"
    encrypted_img.save(save_path)
    return save_path

# Decrypt using XOR operation with the same key
def decrypt_image(image_path, seed):
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    if key_array is None:
        raise ValueError("Encryption key not found. Encrypt an image first.")
    key = generate_key_array(arr.shape, seed)
    decrypted = np.bitwise_xor(arr, key)
    decrypted_img = Image.fromarray(decrypted)
    save_path = os.path.splitext(image_path)[0] + "_decrypted.png"
    decrypted_img.save(save_path)
    return save_path

# GUI Application
class ImageEncryptorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption Tool")
        master.geometry("450x230")

        self.label = tk.Label(master, text="Enter a numeric seed key (e.g., 1234):")
        self.label.pack(pady=10)

        self.key_entry = tk.Entry(master)
        self.key_entry.pack(pady=5)
        self.key_entry.insert(0, "1234")

        self.encrypt_btn = tk.Button(master, text="Encrypt Image", command=self.encrypt)
        self.encrypt_btn.pack(pady=5)

        self.decrypt_btn = tk.Button(master, text="Decrypt Image", command=self.decrypt)
        self.decrypt_btn.pack(pady=5)

        self.note = tk.Label(master, text="* Use same seed for decryption\n* Decrypt only works after encrypt", fg="gray")
        self.note.pack(pady=10)

    def encrypt(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if filepath:
            try:
                seed = int(self.key_entry.get())
                output = encrypt_image(filepath, seed)
                messagebox.showinfo("Success", f"Image Encrypted and saved as\n{output}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def decrypt(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if filepath:
            try:
                seed = int(self.key_entry.get())
                output = decrypt_image(filepath, seed)
                messagebox.showinfo("Success", f"Image Decrypted and saved as\n{output}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
