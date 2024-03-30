import qrcode
import os

#QR_Project
# Environment variables for customization
qr_data = os.getenv('QR_DATA_URL', 'https://github.com/Ash-neon')
qr_code_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
qr_code_filename = os.getenv('QR_CODE_FILENAME', 'myQR.png')
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

# Ensure the QR codes directory exists
os.makedirs(qr_code_dir, exist_ok=True)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img_path = os.path.join(qr_code_dir, qr_code_filename)
img.save(img_path)

print(f"QR Code generated successfully and saved to {img_path}")
