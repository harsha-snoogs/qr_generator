import qrcode
import qrcode.image.svg

def generate_qr_code(url, file_name='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage:
generate_qr_code('https://naming-ceremony-ac3e8.web.app/', 'naming_ceremony.png')


def generate_svg_qr_code(url, file_name='qr_code.svg', line_color='black', background_color='white'):
    factory = qrcode.image.svg.SvgImage
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        image_factory=factory,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=line_color, back_color=background_color)
    img.save(file_name)
    print(f"SVG QR code saved as {file_name}")

# Example usage:
generate_svg_qr_code(
    'https://naming-ceremony-ac3e8.web.app/',
    file_name='naming_ceremony.svg',
)