import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter text or URL:")
        self.label.pack()
        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()
        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.pack()

        self.qr_code_label = tk.Label(master)
        self.qr_code_label.pack()

        self.qr_code = None

    def generate_qr_code(self):
        data = self.entry.get()
        if data:
            self.qr_code = qrcode.make(data)
            qr_code_image = ImageTk.PhotoImage(self.qr_code)
            self.qr_code_label.config(image=qr_code_image)
            self.qr_code_label.image = qr_code_image
            self.save_button.config(state=tk.NORMAL)
        else:
            self.qr_code = None
            self.qr_code_label.config(image=None)
            self.save_button.config(state=tk.DISABLED)

    def save_qr_code(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            self.qr_code.save(file_path)

root = tk.Tk()
qrcode_generator = QRCodeGenerator(root)
root.mainloop()
