### lookup-mac.py

通过macvendors.com提供的REST API来查询。


**使用方法：** python lookup-mac.py <mac-file>,其中<mac-file>中mac地址以':'或者'-'分割，如
``` python
34:36:3b:d0:9c:66
48:74:6e:09:7a:1d
#or
34-36-3b-d0-9c-66
48-74-6e-09-7a-1d
```

运行结果:
``` bash
$ python lookup-mac.py mac.list
1   	00-f7-6f-c0-90-b3	APPLE, INC.
2   	18-4f-32-0e-dc-2f	HON HAI PRECISION IND. CO.,LTD.
3   	1c-cb-99-e8-54-d0	TCT MOBILE LTD
4   	34-36-3b-d0-9c-66	APPLE, INC.
5   	48-74-6e-09-7a-1d	APPLE, INC.
6   	4c-7c-5f-20-51-6b	APPLE, INC.
7   	4c-7c-5f-4b-19-80	APPLE, INC.
8   	52-54-00-60-32-5f	[NOT FOUND]
9   	52-54-00-8f-c0-e9	[NOT FOUND]
10  	52-54-00-ce-5d-50	[NOT FOUND]
11  	60-57-18-ff-19-e6	INTEL CORPORATE
done.
```

### lookup-mac-offline.sh

macvendors.com使用的就是IEEE官网的oui.txt来进行查询的，这个文件由IEEE来维护，记录了oui和对应的厂商，我们可以直接在这个oui文件中查询。
我们可以通过`wget http://standards-oui.ieee.org/oui/oui.txt`来获得该文件。

mac.txt同样按照上面所述，以'**:**' 或者'**-**'分割。
*运行上述脚本时需要保证脚本和oui.txt在同一目录下。*
