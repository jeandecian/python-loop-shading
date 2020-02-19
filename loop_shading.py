from PIL import Image

img = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):

        # values can be: 0-255, x, y
        r = 255
        g = x
        b = y
        
        img.putpixel((x,y),(r,g,b))

output = "output"

img.save(output + ".png")
