from array import array

#1)basic slicing 
'''arr = array('i',[10,20,30,50,60,50])
print(arr[1:6])
print(arr[3:])
print(arr[:4])'''

#2)step slicing
'''arr = array('i',[10,20,30,50,60,50])
print(arr[1::2])
print(arr[3::])
print(arr[::4])'''

#3)negative slicing
'''arr = array('i',[10,20,30,50,60,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[-5:])'''

#4)revers 
'''arr = array('i',[10,20,30,50,60,50])
print(arr[::-1])'''

#5)mofifing slice
'''arr = array('i',[10,20,30,50,60,50])
arr[1:3]=array('i',[77,88])
print(arr)'''