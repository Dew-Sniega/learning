Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = '1'
>>> print type(var)
<type 'str'>
>>> new_var = int(var) + 1
>>> print new_var
2
>>> page_num = 1
>>> print "第",page_num,"页"
第 1 页
>>> print "第"+str(page_num)+"页"
第1页
>>> import random
>>> random.Random()
<random.Random object at 0x01BB0038>
>>> random.choice("['a','b','c']")
','
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
'a'
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
']'
>>> random.choice("['a','b','c']")
'c'
>>> random.choice("['a','b','c']")
']'
>>> random.choice("['a','b','c']")
','
>>> test_list = ['a','b','c']
>>> random.choice(test_list)
'a'
>>> test_list[0]
'a'
>>> test_list[1]
'b'
>>> test_list[0:2]
['a', 'b']
>>> test_list[0:3]
['a', 'b', 'c']
>>> test_list[1:2]
['b']
>>> test_list[1:3]
['b', 'c']
>>> list1 = [2,3]
>>> list1 * 2
[2, 3, 2, 3]
>>> 3 in [1,2,3]
True
>>> if 3 in [1,2,3]
SyntaxError: invalid syntax
>>> if 3 in [1,2,3]:
	print "Ok"

	
Ok
>>> list.append("a")

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list.append("a")
TypeError: descriptor 'append' requires a 'list' object but received a 'str'
>>> lis = []
>>> list = []
>>> list.append("a")
>>> list
['a']
>>> list1
[2, 3]
>>> list2 = [1,2,3,4,5]
>>> list2
[1, 2, 3, 4, 5]
>>> cmp(list1,list2)
1
>>> len(list1)
2
>>> max(list2)
5
>>> touple1 = (1,2,3,4)
>>> touple1 = ('a','b','c')
>>> list(touple1)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list(touple1)
TypeError: 'list' object is not callable
>>> tuple1=（'a','c','e')
SyntaxError: invalid syntax
>>> tuple2=（123,'a','b')
SyntaxError: invalid syntax
>>> tuple1 =（'a','c','e')
SyntaxError: invalid syntax
>>> tuple1 =('a', 'c', 'e')
>>> list(tuple1)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list(tuple1)
TypeError: 'list' object is not callable
>>> 
