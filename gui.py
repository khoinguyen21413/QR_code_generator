import tkinter as tk
import qrcode
from tkinter import messagebox
from PIL import Image, ImageTk
import io

class QRCodeGeneration:
    def __init__(self, root):
        self.bg_color = "#4AFFB7"
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("650x400")
        self.root.configure(bg= self.bg_color)

        self.create_widgets()
        self.update_input_fields()
    
    def create_widgets(self):
        # Frame1 (bên trái)
        self.frame1 = tk.Frame(self.root, bg="lightblue", width=550, height=500)
        self.frame1.pack(side="left", fill="both", expand=True)

        # Frame2 (bên phải)
        self.frame2 = tk.Frame(self.root, bg="lightgreen", width=350)
        self.frame2.pack(side="right", fill="both")

        # Frame 1A (bên trên)
        self.frame1a = tk.Frame(self.frame1, bg= "lightcyan", height= 75)
        self.frame1a.pack(side="top", fill="x", expand=True)  
        self.frame1a.pack_propagate(False)


        # Frame 1B (bên dưới)
        self.frame1b = tk.Frame(self.frame1, bg= "thistle", height= 425)
        self.frame1b.pack(side="top", fill="x", expand=True)
        self.frame1b.pack_propagate(False)

        radio_frame = tk.Frame(self.frame1a, bg="lightcyan")
        radio_frame.pack(anchor="center", padx=10)
        self.qr_type_var = tk.StringVar(value="text")
        radio_text = tk.Radiobutton(radio_frame, text="Text", variable=self.qr_type_var, command=self.update_input_fields, value="text", bg="lightcyan")
        radio_link = tk.Radiobutton(radio_frame, text="Link", variable=self.qr_type_var, command=self.update_input_fields, value="link", bg="lightcyan")
        radio_wifi = tk.Radiobutton(radio_frame, text="Wifi", variable=self.qr_type_var, command=self.update_input_fields, value="wifi", bg="lightcyan")

        radio_text.pack(side="left", padx=10)
        radio_link.pack(side="left", padx=10)
        radio_wifi.pack(side="left", padx=10)

        # Nhap lieu 
        # Text
        self.label_text = tk.Label(self.frame1b, text="Nhập văn bản: ")
        self.entry_text = tk.Entry(self.frame1b, width=40)

        # Link
        self.label_link = tk.Label(self.frame1b, text="Nhập đường dẫn: ")
        self.entry_link = tk.Entry(self.frame1b, width=40)

        # Wifi
        self.label_ssid = tk.Label(self.frame1b, text="Nhập tên wifi: ")
        self.entry_ssid = tk.Entry(self.frame1b, width=40)
        
        self.label_password = tk.Label(self.frame1b, text="Nhập mật khẩu wifi: ")
        self.entry_pasword = tk.Entry(self.frame1b, width=40)
        
        self.label_type_wifi = tk.Label(self.frame1b, text="Loại bảo mật")
        self.security_var = tk.StringVar(value="WPA")
        self.security_menu = tk.OptionMenu(self.frame1b, self.security_var, "WPA", "WEP", "Nopass")

        
    def update_input_fields(self):
        qr_type = self.qr_type_var.get()

        # An cac widget tren frame1b
        for widget in self.frame1b.winfo_children():
            widget.pack_forget()
        
        if qr_type == "text":
            self.label_text.pack(anchor="w", pady=(5,0), padx=10)
            self.entry_text.pack(anchor="w", pady=(0,5), padx=10)
        elif qr_type == "link":
            self.label_link.pack(anchor="w", pady=(5,0), padx=10)
            self.entry_link.pack(anchor="w", pady=(0,5), padx=10)
        elif qr_type == "wifi":
            self.label_ssid.pack(anchor="w", pady=(5,0), padx=10)
            self.entry_ssid.pack(anchor="w", pady=(0,5), padx=10)

            self.label_password.pack(anchor="w", pady=(5,0), padx=10)
            self.entry_pasword.pack(anchor="w", pady=(0,5), padx=10)

            self.label_type_wifi.pack(anchor="w", pady=(5,0), padx=10)
            self.security_menu.pack(anchor="w", pady=(0,5), padx=10)