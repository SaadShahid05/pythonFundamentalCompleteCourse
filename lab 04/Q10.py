# Code: n=5;
#  for i in range(n):
#      for j inrange(i): 
#         print ('* ', end="") 
#     print('') 
 
# for i in range(n,0,-1):     for j in range(i): 
#         print('* ', end="") 
#     print('') 

n = 5
for i in range(n):
    for j in range(i):
        print("* ", end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("* ", end=" ")
    print()
