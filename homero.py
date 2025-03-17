x,y,z=map(int,input().split()) 
sw=(x+y==z or x+z==y or y+z==x) or (x==y and z%2==0) or (x==z and y%2==0) or (z==y and x%2==0)
if sw :
    print("SI")
else:
    print("NO")
