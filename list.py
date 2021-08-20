Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:04:37) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list=[1,'hello',3.4]
>>> my_list
[1, 'hello', 3.4]
>>> my_list=['c','s','i','t','a','c','r','o']
>>> my_list[o]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    my_list[o]
NameError: name 'o' is not defined
>>> my_list[1]
's'
>>> my_list=['c','s','i','t','a','c','r','o',[2,0,1,3]]
>>> my_list[-1][1]
0
>>> my_list[2:5]
['i', 't', 'a']
>>> my_list[-1][1]=9
>>> my_list[-1][1]
9
>>> my_list=[2,3,4,5,7,8,8]
>>> my_list[1:4]=[4,4,4]
>>> my_list
[2, 4, 4, 4, 7, 8, 8]
>>> my_list.append(10)
>>> my_list
[2, 4, 4, 4, 7, 8, 8, 10]
>>> my_list.extend([9,11,14])
>>> my_list
[2, 4, 4, 4, 7, 8, 8, 10, 9, 11, 14]
>>> print(my_list + [11,12,13])
[2, 4, 4, 4, 7, 8, 8, 10, 9, 11, 14, 11, 12, 13]
>>> print("hello"*5)
hellohellohellohellohello
>>> my_list.insert(1,90)
>>> my_list
[2, 90, 4, 4, 4, 7, 8, 8, 10, 9, 11, 14]
>>> odd=[1]
>>> my_list.append(odd)
>>> my_list
[2, 90, 4, 4, 4, 7, 8, 8, 10, 9, 11, 14, [1]]
>>> my_list=[1,2,3,4,5,6,7,8,9]
>>> my_list.remove(2)
>>> my_list
[1, 3, 4, 5, 6, 7, 8, 9]
>>> my_list=[1,2,2,3,4,5,6,7,8,9]
>>> my_list.pop(1)
2
>>> my_list=[1,2,3,4,5,6,7,8,9]
>>> my_list.pop(1)
2
>>> my_list.clear()
>>> my_list
[]
>>> my_list=[1,2,2,3,4,5,6,7,8,9]
>>> my_list.pop()
9
>>> my_list.index(3)
3
>>> my_list.count(2)
2
>>> del my_list
>>> my_list
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    my_list
NameError: name 'my_list' is not defined
>>> L = [3,2,1]
>>> L.sort()
>>> L
[1, 2, 3]
>>> l.reverse()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l.reverse()
NameError: name 'l' is not defined
>>> L.reverse()
>>> L
[3, 2, 1]
>>> #LIST COMPREHENSION
>>> #LIST COMPREHENSION-consits of expression floowed by for loop inside the square brackets
>>> power=[ x**2 for x in range(10)]
>>> power
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> power=[ x**2 for x in range(10) if(x >5)]
>>> power
[36, 49, 64, 81]
>>> power=[ 2**x for x in range(10) if(x >5)]
>>> power
[64, 128, 256, 512]
>>> odd = [ for x in range(20) if(x%2==0)]
SyntaxError: invalid syntax
>>> even = [ x for x in range(20) if(x%2==0)]
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> odd = [ x for x in range(50) if(x%2!=0)]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> l = [x+y for x in ['python' ,'c'] for y in ['language','programming']]
>>> l
['pythonlanguage', 'pythonprogramming', 'clanguage', 'cprogramming']
>>> [x+y for x in ['python' ,'c'] for y in ['language','programming']]
['pythonlanguage', 'pythonprogramming', 'clanguage', 'cprogramming']
>>> print ('hello' in l)
False
>>> for i in [0,1,2,3,4]:
	print(i)

0
1
2
3
4
>>> 