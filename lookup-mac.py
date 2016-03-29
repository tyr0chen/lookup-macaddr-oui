#-*-coding:utf-8-*-
#ver 0.0.1
#maintained by tyr.chen
#use api.macvendors.com to lookup vendors.
# 使用方法：python lookup-mac.py <mac-file>
# <mac-file>中mac地址以':'或者'-'分割，如
#00:f7:6f:c0:90:b3
#18:4f:32:0e:dc:2f
#或者
#18-4f-32-0e-dc-2f
#1c-cb-99-e8-54-d0

>>>>>>> e24ec888e61c92c05d8d50b75cce0275b05c29b3

import urllib2
import sys

macfile=open(sys.argv[1],'rU')
seq=0

for line in macfile:
    #跳过空行
    if line.strip() == '' :
        continue
    seq+=1
    #mac地址以':'分割
    if ':' in line :
        maclist=line.split(':')
        macstr='-'.join(maclist).strip()
    #mac地址以'-'分割
    else :
        macstr=line.strip()
    url='http://api.macvendors.com/'+macstr
    try:
        html=urllib2.urlopen(url,timeout=3).read()
    except urllib2.HTTPError:
        print '%-4d\t%-17s\t%s' %(seq,macstr,'[NOT FOUND]')
    except:
        print '%-4d\t%-17s\t%s' %(seq,macstr,'[OPEN ERROR]')
        continue
    else:
        print '%-4d\t%-17s\t%s' %(seq,macstr,html)
print 'done.'
