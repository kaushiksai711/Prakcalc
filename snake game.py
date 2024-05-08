import numpy as np
a=int(input('10 by 10'))
b=np.array([[' 'for i in range(a)] for j  in range(a) ])
'''location must be like its head moves in whichever direction it moves its body must move after 
it reaches that position so the whole bodys location must be always updated'''
def movement(button,location,i,j):
    if (button=='left'):
        location.append([i,j-1])
    if (button=='right'):
        location.append([i,j+1])
    if (button=='down'):
        location.append([i+1,j])
    if (button=='up'):
        location.append([i-1,j])
    return location
def fruitt(fruit,location):
    if '$' in b:
        return fruit
    else:
        while True: 
            z=np.random.choice([i for i in range(len(b))])
            y=np.random.choice([i for i in range(len(b))])
            fruit=[z,y]
            print(fruit)
            if fruit not in location:
                z,y=map(int,fruit)
                b[z][y]='$'
                break
    return fruit
    
def growth(location,fruit):
    print(fruit,location[len(location)-1])
    if fruit!=location[len(location)-1]:
        q,r=map(int,location[0])
        b[q][r]=' '
        location.remove(location[0])
    else:
        print('ate it')
def valid(location):
    for i in location[-1]:
        if 0<=i<=a:return True
        else:return False
    if len(set(location))!=len(location):
        return False
def start():
    loc=[np.random.choice([i for  i in range(a//2)]),np.random.choice([i for  i in range(a//2)])]
    location=[loc]
    print(location)
    return location
def display(b,location):

    for i in location:
        q,r=map(int,i)
        b[q][r]='*'
    print(b)
while True:
    d=input('play game?')
    if d=='no':
        break
    else:
        c=start()
        display(b,c)
        da=0
        s=[0,0]
        while True:
            
            s=fruitt(s,c)
            if da==0:
                da=1
                display(b,c)
            #take button input from graphics
            button=input('give the way')
            c=movement(button,c,c[-1][0],c[-1][-1])
            growth(c,s)
            e=valid(c)
            if e:
                display(b,c)
            else:
                print('gm over')
                break