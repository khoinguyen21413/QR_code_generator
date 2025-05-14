import tkinter as tk
import qrcode
from tkinter import messagebox
from PIL import Image, ImageTk
import io

class QRCodeGeneration:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("800x500")
        self.root.configure(bg= "#4AFFB7")

        self.create_widgets()
    
    def create_widgets(self):
        # Frame1 (bên trái)
        frame1 = tk.Frame(self.root, bg="lightblue", width=550, height=500)
        frame1.pack(side="left", fill="both", expand=True)

        # Frame2 (bên phải)
        frame2 = tk.Frame(self.root, bg="lightgreen", width=350)
        frame2.pack(side="right", fill="both")