from simpleimage import SimpleImage
img=SimpleImage("flower.png")
img.show()
x=0
y=0
pixel=img.get_pixel(x,y)
average=(pixel.red + pixel.blue + pixel.green)//3

def gray_scale(x):
    average=(x.red + x.blue + x.green)//3
    x.red=average
    x.green=average



for pixel in img:
    if pixel.red>average*1.6947353:
        pixel.red=255
        pixel.blue=0
        pixel.green=0
    else:
        gray_scale(pixel)

img.show()