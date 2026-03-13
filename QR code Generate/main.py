'''QR Generator'''

import qrcode

def generate_qr_code():
    url = input("Enter the website URL: ").strip()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  #Size of each box in the QR code grid
        border=4,  #Thickness of the border (minimum is 4)
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    file_name = "myportfolio.png"
    img.save(file_name)

    print(f"QR code generated and saved as {file_name}.")

generate_qr_code()
