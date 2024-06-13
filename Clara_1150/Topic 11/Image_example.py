"""
Mark Porraz
Image_example.py
All information and logica can be found at this website
https://www.geeksforgeeks.org/python-pillow-a-fork-of-pil/
"""

from PIL import Image

# example 1
img = Image.open(r"test.png")  # the image needs to be beside in same folder as file
print(img.mode)  # showing what mode the file is ()
print(img.size)  # showing the image size ()
print(img.format)  # showing what format the file is in ()
img.show()  # this command actually makes the photo appear from folder it is stored

# example 2
# angle = 40
# img = Image.open(r"test.png")
# r_img = img.rotate(angle)
# img.show()
# this bit of code demonstrates using the rotate() function by an angle


# example 3
# size = (40, 40)
# img = Image.open(r"test.png")
# r_img = img.resize(size)
# r_img.show()

# example 4
# size = (40, 40)
# img = Image.open(r"test.png")
# r_img = img.resize(size, resample=Image.BILINEAR)
#
# # resized_test.png => Destination_path
# r_img.save("resized_test.png")
#
# # Opening the new image
# img = Image.open(r"resized_test.png")
# print(img.size)
