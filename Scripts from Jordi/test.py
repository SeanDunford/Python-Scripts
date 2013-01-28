import Image
#import png

r = png.Reader("test.png")
r.read()

l=list(_[2])
l[0]


im = Image.open("test.png")
im.getpixel((0,0))
#r,g,b = im.getpixel((0,0))
#pix = im.load()
#r,g,b = pix[0, 0]

#print "color=" + str(r) + ";" + str(g) + ";" + str(b) + "&submit=1"
