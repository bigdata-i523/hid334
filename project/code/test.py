from PIL import Image
import os
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
image = Image.open(os.path.join(parentDirectory, 'WeatherIcons'))
image.show()