import qrcode

# Data you want to convert into QR code
data = "https://www.linkedin.com/in/m-arman-mahmud"

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,  # size of each box in pixels
    border=4      # thickness of the border
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="white", back_color="black")

# Save the image
img.save("qrcode.png")

print("QR Code generated successfully!")
