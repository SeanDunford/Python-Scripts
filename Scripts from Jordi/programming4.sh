#!/bin/bash

curl -s -b "enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518740199%3Bi%3A3%3Bi%3A2%3B%7D;PHPSESSID=e7640fdbfc994ba58c655c5c8e51de2c" http://www.enigmagroup.org/missions/programming/4/image.php > test.png

python p4.py | curl -s -b 'enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518740199%3Bi%3A3%3Bi%3A2%3B%7D;PHPSESSID=e7640fdbfc994ba58c655c5c8e51de2c' --data @- -e 'http://www.enigmagroup.org/missions/programming/4/image.php' http://www.enigmagroup.org/missions/programming/4/image.php


