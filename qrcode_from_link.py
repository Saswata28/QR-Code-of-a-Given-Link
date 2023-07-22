# Do 'pip install qrcode Image' in your terminal first.
import qrcode


def generate_qr(link, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)
    image_of_qr = qr.make_image(fill_color="black", back_color="white")
    image_of_qr.save(f"{file_name}.png")


user_input_link = input("Enter the Link you want to get the QR code of: ")
user_input_qr_file_name = input(
    "Enter the name of the file you want to save as qr code image(Don't name it same as other existing files in the folder where this code is): ")
generate_qr(user_input_link, user_input_qr_file_name)
directory = os.getcwd()
print(
    f"QR code Image of your link has been downloaded in \"{directory}\" as \"{user_input_qr_file_name}.png\".")
