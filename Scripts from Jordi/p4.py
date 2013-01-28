#import png
import Image

#r = png.Reader("test.png")
#r.read()	

#l=list(_[2])
#l[0]

string = 0
im = Image.open("test.png")
y = 0
for x in range(0, 40):
	string = string + im.getpixel((y,0))
	y = y + 1

print str(string)

#r,g,b = im.getpixel((0,0))
#pix = im.load()
#r,g,b = pix[0, 0]

#print "color=" + str(r) + ";" + str(g) + ";" + str(b) + "&submit=1"
