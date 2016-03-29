#!/bin/bash
#ver 0.0.1
#maintained by tyr.chen
#use oui.txt to lookup vendors.
#Usage: ./lookup-oui.sh mac.txt

#Attention: make sure this script and oui.txt in the same dir.
#Get ou.txt : wget http://standards-oui.ieee.org/oui/oui.txt
#In the file mac.txt,mac adress seprated by ':' or '-' as:
#00:f7:6f:c0:90:b3
#18:4f:32:0e:dc:2f
#or
#18-4f-32-0e-dc-2f
#1c-cb-99-e8-54-d0

seq=0
while read line;do
  let seq=seq+1
  mac=`echo $line | tr -d ':-' | cut -c 1-6 | tr [a-z] [A-Z]`
  echo -ne $seq '\t' $line '\t'
  if value=`grep $mac oui.txt` ;then
    echo $value | sed  -e 's/.*16)[[:blank:]]*//g' -e 's/.*hex)[[:blank:]]*//g'
  else
    echo '[NOT FOUND]'
  fi
done < $1
