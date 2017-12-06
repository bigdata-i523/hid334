from PIL import Image
# import os
# parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# image = Image.open(os.path.join(parentDirectory, 'WeatherIcons', 'Code32.PNG'))

image = Image.open('./images/testimage.png')
image.show()
