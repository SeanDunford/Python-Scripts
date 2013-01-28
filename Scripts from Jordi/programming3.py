import Image
import os

os.system('curl -b "enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518740199%3Bi%3A3%3Bi%3A2%3B%7D; PHPSESSID=e7640fdbfc994ba58c655c5c8e51de2c;" -o test.jpg http://www.enigmagroup.org/missions/programming/3/image.php')

im = Image.open("test.jpg")

r,g,b = im.getpixel((0,0))

string = '"color=' + str(r) + ";" + str(g) + ";" + str(b) + '"'

c = "curl -s -b 'enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518738714%3Bi%3A3%3Bi%3A2%3B%7D; PHPSESSID=e7640fdbfc994ba58c655c5c8e51de2c' -d "+string+" -d submit=1 --referer http://www.enigmagroup.org/missions/programming/3/image.php http://www.enigmagroup.org/missions/programming/3/image.php"

print r,g,b
print string

os.system(c)
