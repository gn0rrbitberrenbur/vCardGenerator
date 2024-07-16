#This script generates a .vcf file storing entered contact data. If you don't want to enter certain data just leave the form empty

import qrcode
import os

#getting the users input with his contact details
first_name=input('Your first name: ')
last_name=input('Your last name: ')
emailadress=input('Your E-mail adress: ')
phonenumber=input('Your mobile phone number: ')

#getting the filepath to store the output
filepathOutput=input('Enter the filepath where the QR-Code should be safed to: ')

#storing the vcard in a f-string
vCard=f"""BEGIN:VCARD
VERSION:3.0
FN:{first_name} {last_name}
TEL;type=CELL:{phonenumber}
EMAIL;type=HOME,INTERNET:{emailadress}
END:VCARD"""

#create the qr code and save it to the filepath that the user entered
def QRcodeCreation ():
        qr_code=qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
)
        qr_code.add_data(vCard)
        qr_code.make(fit=True)

        img=qr_code.make_image(fill_color="black", back_color="white").convert("RGBA")
        img.save(f"{filepathOutput}/{first_name}{last_name}vCard.png")

#checks wether the provided filepath is valid or not and throws an exception if not
filepathValidation=os.path.exists(f'{filepathOutput}')

if filepathValidation==True:
    QRcodeCreation()
else:
    print("Please enter a valid filepath.")