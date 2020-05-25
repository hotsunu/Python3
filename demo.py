print('hello world!')

iNumbers = 12345
fNumbers = 3.1415
sString = 'hello'
bTure = Ture
lLists = [12345,3.1415,'hello',Ture]
print('lLists[0]:',lLists[0]) #>>>lLists[0]:12345
print('lLists[2]:',lLists[2]) #>>>lLists[2]:12345

for x in range(10):
  print(x)
  
lLists = [[(x+1)*(y+1) for x in range(8)] for y in range(10)]

lLists = [x for x in range(10) if x%3 ==0]

lLists = [1,2,3,4,5,6,7,8,9]
print('lLists[1:3]:',lLists[1:3]) #>>>lLists[1:3]:2,3
print('lLists[:3]:',lLists[:3]) #>>>lLists[:3]:1,2,3
print('lLists[1:]:',lLists[1:]) #>>>lLists[1:]:2,3,4,5,6,7,8,9
print('lLists[1:9:2]:',lLists[1:9:2]) #>>>lLists[1:9:2]:2,4,6,8
print('lLists[::-2]:',lLists[::-2]) #>>>lLists[::-2]:9,7,6,5,3,1
