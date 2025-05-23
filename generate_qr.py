from PIL import Image, ImageTk
import io
import qrcode

def create_qr_image(qr_type, data):
    if qr_type == "text":
        if not data:
            raise ValueError("Vui lòng nhập văn bản")
        qr_data = data[0]
    elif qr_type == "link":
        if not data:
            raise ValueError("Vui lòng nhập url")
        qr_data = data[0]
    elif qr_type == "wifi":
        ssid = data[0]
        password = data[1]
        security = data[2]

        if not ssid:
            raise ValueError("Vui lòng nhập tên wifi")
        if security != 'nopass' and not password:
            raise ValueError("Vui lòng nhập mật khẩu")
        if len(password) < 8:
            raise ValueError("Vui lòng nhập mật khẩu ít nhất 8 ký tự")
        if security == "nopass":
            qr_data = f"WIFI:T:{security};S:{ssid};;"
        else:
             qr_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    else:
        raise ValueError("Loại mã qr không hợp lệ")  

    # tạo mã QR từ dữ liệu
    qr = qrcode.QRCode(version=1, box_size=6, border=2)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_image(img,path):
    img.save(path)
