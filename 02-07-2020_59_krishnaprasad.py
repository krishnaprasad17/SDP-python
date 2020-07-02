Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #create a tuple
>>> tip=(10,20,30,50,60)
>>> print(tip)
(10, 20, 30, 50, 60)
>>> ##diffrent datatypes
>>> star=(120,"AA",43.12)
>>> print(star)
(120, 'AA', 43.12)
>>> ##tuple to string
>>> star=("icon","AA","Bunny")
>>> my_fav=str(star)
>>> print(my_fav)
('icon', 'AA', 'Bunny')
>>> 
>>> ##slice a tuple
>>> star=(120,"icon",22.2)
>>> king=star[:2]
>>> print(king)
(120, 'icon')
>>> 
>>> ##find length of tuple
>>> star=(120,"icon",22.2)
>>> print( " tuple length : ", len(star))
 tuple length :  3
>>> 
>>> ##tuple to dictinary
>>> t=((1,'king'), (2,'queen'))
>>> a=dict((y, x) for x, y in t)
>>> print(a)
{'king': 1, 'queen': 2}
>>> 
>>> ##reverse a tuple
>>> star=(120,"icon",22.2,66,92)
>>> print(star[::-1])
(92, 66, 22.2, 'icon', 120)
>>> 
>>> ##list of tuples to dictinary
>>> my_list = [('king', 1), ('quuen', 2)]
>>> dict(my_list)
{'king': 1, 'quuen': 2}
>>> print(my_list)
[('king', 1), ('quuen', 2)]
>>> 
>>> ##list to tuple
>>> a=[123,"king",77,99]
>>> print(tuple(a))
(123, 'king', 77, 99)
>>> 