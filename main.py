import qrcode
import image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data('https://www.jehangirkhan.me')
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(), color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(255, 19, 32)))
img.save("QR_Code.png")
print("QR Code Generated.")
