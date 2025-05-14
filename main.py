import qrcode
import os
import validators

# Function to validate URL
def get_valid_url():
    while True:
        url = input("Enter a valid URL: ")
        if validators.url(url):
            return url
        else:
            print("Invalid URL. Please try again.")

# Create 'output' directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Get a valid URL from the user
url = get_valid_url()

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to the specified path
output_path = os.path.join(output_dir, "qrcode.png")
img.save(output_path)
print(f"QR Code generated and saved at '{output_path}'")
