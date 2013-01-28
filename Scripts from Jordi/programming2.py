#!/usr/bin/python

print "hello world!"

import urllib2
import ImageFile
from cStringIO import StringIO
import Image


image_url = "http://www.enigmagroup.org/missions/programming/3/image.php"
opener1 = urllib2.build_opener()
page1=opener1.open(image_url)

data = StringIO(page1.read())
img = Image.open(data)

print img
#p = ImageFile.Parser()

#while 1:
#    s = page1.read(1024)
#    if not s:
#        break
#    p.feed(s)

#im = p.close()
#r,g,b = im.getpixel((0,0))

#fout = open('images/tony'+image[s]+"%d%_d%_d"%(r,g,b), "wb")
#fout.write(my_picture)
#fout.close()

