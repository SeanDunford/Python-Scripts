#!/bin/bash

if [ -a "./index.php" ]
  then
        rm ./index.php
fi

wget -q --no-cookies --header="Cookie: enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518738714%3Bi%3A3%3Bi%3A2%3B%7D; PHPSESSID=6d0d475c28ed30c6197b37a72ba6edd2" http://www.enigmagroup.org/missions/programming/2/index.php
 

number=`grep "multiply" ./index.php | cut --bytes=53-60`

#echo $number

let "answer=$number * 4"

#echo $answer

hash=`grep "hash" ./index.php | cut --bytes 45-76`

#echo $hash

time=`grep "time" ./index.php | cut --bytes 48-57`

#echo $time

curl -s -b 'enigmafiedV4=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236519%22%3Bi%3A1%3Bs%3A40%3A%22032e642eaa4331ac46c01c6a73c7ac61866681bf%22%3Bi%3A2%3Bi%3A1518738714%3Bi%3A3%3Bi%3A2%3B%7D; PHPSESSID=6d0d475c28ed30c6197b37a72ba6edd2' -d submit=true -d E[number]=$number -d hash=$hash -d E[time]=$time -d answer=$answer http://www.enigmagroup.org/missions/programming/2/index.php >  testing

#grep "time" ./index.php > waddup
