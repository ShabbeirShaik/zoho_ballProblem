def minit(n):
    ml = []
    for i in range(n):
        l=[]
        if(i==0):                         #function to initialize the matrix
            for i in range(n):
                l.append("W")
            ml.append(l)
        elif(i<n-1):
            for j in range(n):
                if(j==0 or j==n-1 ):
                    l.append("W")
                else:
                    l.append(" ")
            ml.append(l)
        else:
            for j in range(n):
                if(j==0 or j==n-1 ):
                    l.append("W")
                else:
                    l.append("G")
            ml.append(l)
    return ml
            
def printing():
    for i in range(n):
        for j in range(n):                  #function to print the matrix
            print(ml[i][j],end=" ")
        print("")
    
    
def ballmov(c,dir):
    bc=c
    for i in range(2,n,1):
        if(str(ml[-i][bc]).isnumeric()):
            ml[-i][bc]-=1
            
        if(ml[-i][bc] == 0):
            ml[-i][bc] =" "
            break 
            
    printing()

def ballmov(r,c,di,el):
    bc=c
    for i in range(2,n,1):
        if(str(ml[-i][bc]).isnumeric() ):
            (ml[-i][bc]) = int(ml[-i][bc])-1
            s(bc)
            break
        elif(str(ml[-i][bc]).upper()=="B"):
            ml[-i][bc]=" "
            if(r and c+1<6):
                r = not r
                ml[-1][c+1] = "_"
                break
            elif(not r  and c-1 >0):
                r= not r
                ml[-1][c-1] = "_"
                break
        elif(str(ml[-i][bc]).upper()=="DE"):
            ml[-i] = el
            break
        elif(str(ml[-i][bc]).upper()=="DS" and i>2):
            ml[-i] = el
            ml[-i-1] = el
            break    
    
    
    
    
n = int(input("Enter size of the NXN matrix : "))
ml= []
ml = minit(n)
el=ml[1].copy()
s = "Y"
while(s!="N"):
    l = input("Enter the brick's position and the brick type: ").split(" ")[:3]
    ml[int(l[0])][int(l[1])] = l[2]
    s = input("Do you want to continue(Y or N)? ")
bc = int(input("Enter the ball count :"))
ml[-1][bc] = "o"
right = True
di = input("Enter the direction in which the ball need to traverse: ")
right = ballmov(right,bc,di,el)    
