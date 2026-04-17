

import qrcode

# The data you want to encode (URL, text, etc.)
data = "https://google.com"

# Generate the QR code
img = qrcode.make(data)

# Save the image to a file
img.save("basic_qr.png")
