#### WRITING QR ###########################################
# creating a qr code image with qrcode library more info can 
# more info on the qrcode library 
# can be found here https://github.com/lincolnloop/python-qrcode
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=5,
    border=4,
)
qr.add_data('https://github.com/hoffstadt/DearPyGui')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("dpg-qr.png")


#### READING QR #######################################
# more info on the pyzbar library can be 
# found here https://github.com/NaturalHistoryMuseum/pyzbar
# we will read directly into dpg however you could utilize open cv 
# from the last example and grab the image from every camera 
# capture and use pyzbar to decode it

# reading the qr code .png into dpg and showing it
import dearpygui.dearpygui as dpg
from pyzbar.pyzbar import decode
import numpy
import webbrowser
dpg.create_context()

def process_qr_image():
    width, height, channels, data = dpg.load_image("dpg-qr.png")

    # after loading with dpg we will read 
    # into a numpy array to do some data minuplation
    # pyzbar wants data in a a 255 shaped format of 8 bits
    # but will also accept a numpy array and do the 
    # conversion from 32 to 8 bit for us
    nparray = numpy.frombuffer(data, 'f')
    nparrayscalar = numpy.multiply(nparray, 255.0)
    npreshaped = numpy.reshape(nparrayscalar,(width, height, channels))

    # various helpful stuff to know about the array
    print("Array is of type: ", type(npreshaped))
    print("No. of dimensions: ", npreshaped.ndim)
    print("Shape of array: ", npreshaped.shape)
    print("Size of array: ", npreshaped.size)
    print("Array stores elements of type: ", npreshaped.dtype)

    # reading the image for QR 
    qr_class = decode(npreshaped)[0]

    # various helpful stuff to know about the qr code class
    print(type(qr_class))
    print(qr_class)

    # reading for data
    qr_data = qr_class.data.decode()

    # because the data in teh qr code is a link we will open it
    webbrowser.open(qr_data)

    # we can also pull the rect or poly infor from the 
    # qr code class and draw squares, 
    # referenceing the open cv example also you could draw 
    # live rectangles overtop of the images using dpg every frame

width, height, channels, data = dpg.load_image("dpg-qr.png")
with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.window(label="Tutorial", tag="MainWin", width=800, height=600):
    dpg.add_image("texture_tag")
    dpg.add_button(label="Process QR code", callback=process_qr_image)
    dpg.add_text("", tag="QR Data")



dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
