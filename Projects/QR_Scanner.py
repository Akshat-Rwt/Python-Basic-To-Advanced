import qrcode

upi_id = input("Enter the UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app
# You can modify these URLS bsed on the payment apps you want to support


phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR Code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

# Save the QR  code to image file(Optional)
phonepe_qr.save('Phonepe_qr.png')
paytm_qr.save('Paytm_qr.png')
googlepay_qr.save('Googlepay_qr.png')

# Display the QR Code(You may need to install pillow library)
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()