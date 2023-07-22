# pip install qrcode Image
import qrcode
import os
import random


def generate_qr(link, file_name):
    # This will generate the QR code from the link.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adding the link inputted by user in the QR.
    qr.add_data(link)
    qr.make(fit=True)
    image_of_qr = qr.make_image(fill_color="black", back_color="white")
    image_of_qr.save(f"{file_name}.png")

    # finding whether same name file exists in the diectory or not.
    # user_input = input('What is the name of your directory')
    # current_directory = os.getcwd()
    # directory = current_directory.split("\\")[-1]
    # print(directory)
    # while_loop_continue = False
    # while_loop_break = False
    # while True:
    #     random_number = random.randint(0, 1000)

    #     searchstring = f"QR_Code{random_number}.png"
    #     # print(searchstring)

    #     for fname in directory:
    #         if os.path.isfile(directory + os.sep + fname):
    #             print("yes")
    #             # We use user_input + os.sep + fname to get full path.os.listdir gives files and directories names, so we use os.path.isfile to check for files.
    #             # Full path
    #             # if os.path.isfile(directory):
    #             f = open(directory + os.sep + fname, 'r')
    #             # f = open(directory, 'r')

    #             if searchstring in f.read():
    #                 print('found string in file %s' % fname)
    #                 while_loop_continue = True
    #             else:
    #                 print('string not found')
    #                 image_of_qr.save(f"QR_Code{random_number}.png")
    #                 while_loop_break = True
    #             f.close()
    #     if while_loop_break == True:
    #         break
    #     elif while_loop_continue == True:
    #         continue
    # image_of_qr.save(f"{link}.png")
    # save the image as a PNG file with the use of Image package.Save the image in the same folder in which this code is.


user_input_link = input("Enter the Link you want to get the QR code of: ")
user_input_qr_file_name = input(
    "Enter the name of the file you want to save as qr code image(Don't name it same as other existing files in the folder where this code is): ")
generate_qr(user_input_link, user_input_qr_file_name)
directory = os.getcwd()
print(
    f"QR code Image of your link has been downloaded in \"{directory}\" as \"{user_input_qr_file_name}.png\".")
