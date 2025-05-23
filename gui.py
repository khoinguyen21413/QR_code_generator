import tkinter as tk
import qrcode
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import io
import generate_qr

class QRCodeGeneration:
    def __init__(self, root):
        self.bg_color = "#4AFFB7"
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x350")
        self.root.configure(bg= self.bg_color)
        self.qr_image = None

        self.create_menu()
        self.create_widgets()
        self.update_input_fields()
    
    def create_widgets(self):
        # Frame1 (bên trái)
        self.frame1 = tk.Frame(self.root, bg=self.bg_color, width=550, height=400)
        self.frame1.pack(side="left", fill="both", expand=True)

        # Frame2 (bên phải)
        self.frame2 = tk.Frame(self.root, bg=self.bg_color, width=200)
        self.frame2.pack(side="right", fill="both")
        self.frame2.pack_propagate(False)

        # Frame 1A (bên trên)
        self.frame1a = tk.Frame(self.frame1, bg=self.bg_color, height= 75)
        self.frame1a.pack(side="top", fill="x", expand=True)  
        self.frame1a.pack_propagate(False)


        # Frame 1B (giữa)
        self.frame1b = tk.Frame(self.frame1, bg=self.bg_color, height= 225)
        self.frame1b.pack(side="top", fill="x", expand=True)
        self.frame1b.pack_propagate(False)

        # Frame 1C (bên dưới)
        self.frame1c = tk.Frame(self.frame1, bg=self.bg_color, height= 50)
        self.frame1c.pack(side="top", fill="x", expand=True)
        self.frame1c.pack_propagate(False)

        radio_frame = tk.Frame(self.frame1a, bg=self.bg_color)
        radio_frame.pack(anchor="center", padx=10)
        self.qr_type_var = tk.StringVar(value="text")
        radio_text = tk.Radiobutton(radio_frame, text="Text", variable=self.qr_type_var, command=self.update_input_fields, value="text", bg=self.bg_color)
        radio_link = tk.Radiobutton(radio_frame, text="Link", variable=self.qr_type_var, command=self.update_input_fields, value="link", bg=self.bg_color)
        radio_wifi = tk.Radiobutton(radio_frame, text="Wifi", variable=self.qr_type_var, command=self.update_input_fields, value="wifi", bg=self.bg_color)

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

        btn_generate = tk.Button(self.frame1c, text= "Tạo mã QR", width=40, command=self.generate_qr)
        btn_generate.pack(anchor="w", padx= 10, pady=10)

        # self.qr_display = tk.Label(self.frame2, width=25, height=10, bg="white", relief="solid", borderwidth=1)
        self.qr_display = tk.Label(self.frame2)
        self.qr_display.pack(anchor="w", padx=10, pady=10)

        self.btn_save = tk.Button(self.frame2, text= "Lưu mã QR", width= 40, command=self.save_qr)
        
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

    def generate_qr(self):
        qr_type = self.qr_type_var.get()
        try:
            if qr_type == "text":
                data = [self.entry_text.get()]
            if qr_type == "link":
                data = [self.entry_link.get()]
            if qr_type == "wifi":
                ssid = self.entry_ssid.get()
                password = self.entry_pasword.get()
                security = self.security_var.get()
                data = [ssid, password, security]
                # data = f"WIFI:S:{ssid};T:{type_wifi};P:{password};;"

            img = generate_qr.create_qr_image(qr_type=qr_type, data=data)
            img_resized = img.resize((200,200))
            img_tk = ImageTk.PhotoImage(img_resized)
            self.qr_display.config(image=img_tk)
            self.qr_display.image = img_tk
            self.btn_save.pack(padx= 10, pady= 10)
            self.qr_image = img
        except ValueError as e:
            messagebox.showwarning("Lỗi", str(e))

    def save_qr(self):
        if self.qr_image:
            path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if path:
                generate_qr.save_qr_image(self.qr_image, path)
                messagebox.showinfo("Thành công!", "Đã lưu thành công.")
            else:
                messagebox.showwarning("Lỗi", "Bạn chưa chọn nơi lưu.")
        else:
            messagebox.showwarning("Chưa tạo QR", "Hãy tạo mã QR trước khi lưu")

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Tạo mã QR", command=self.generate_qr)
        file_menu.add_command(label="Lưu mã QR", command= self.save_qr)
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.root.quit)
        menu_bar.add_cascade( label="File", menu=file_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Thông tin")
        help_menu.add_command(label="Cách dùng")
        menu_bar.add_cascade(label="Hỗ trợ", menu=help_menu)

        self.root.config(menu=menu_bar)